#!/usr/bin/env python3
"""Read-only structural/link checks; not architectural or compliance validation."""
import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
OPERATIONS = ('brief', 'concept', 'development', 'analysis', 'optimization',
              'presentation', 'documentation', 'review')
REFERENCES = ('program-and-space', 'composition-and-style',
              'performance-and-coordination', 'requirements',
              'computational-design', 'visual-delivery', 'calculators', 'sources',
              'planning-and-section', 'site-and-context',
              'envelope-and-assemblies', 'design-development')
NORMATIVE_GROUPS = ('federal-framework', 'territory-and-special-conditions',
                    'building-typologies', 'fire-and-accessibility',
                    'environment-and-interfaces')
RECORD_FIELDS = ('Identity', 'Authority', 'Scope', 'Edition/status',
                 'Application basis', 'Related', 'Verification')
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
DEFINITION = re.compile(r'^\s{0,3}\[[^\]\n]+\]:\s*<?([^\s>]+)>?', re.M)


def anchors(text):
    result, seen = set(), {}
    prose = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose, re.M):
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        count = seen.get(slug, 0)
        result.add(slug + ('-' + str(count) if count else ''))
        seen[slug] = count + 1
    return result


def orphan_table_rows(text):
    """Find outer-pipe rows immediately following a blank-broken table.

    This deliberately covers top-level tables and fenced code, not nested
    Markdown containers or every legal GFM table spelling. A new header and
    delimiter after the blank starts another table; ordinary prose ends the
    inspection. Lines are reported one-based.
    """
    lines = text.splitlines()

    def cells(line):
        # Split on pipes preceded by an even number of backslashes.
        parts, start = [], 0
        for match in re.finditer(r'\|', line):
            prefix = line[:match.start()]
            if (len(prefix) - len(prefix.rstrip('\\'))) % 2 == 0:
                parts.append(line[start:match.start()].strip())
                start = match.end()
        parts.append(line[start:].strip())
        if parts and not parts[0]:
            parts.pop(0)
        if parts and not parts[-1]:
            parts.pop()
        return parts

    def header_at(index):
        if (index + 1 >= len(lines) or '|' not in lines[index]
                or re.match(r'^(?: {4}|\s*>)', lines[index])):
            return False
        header, delimiter = cells(lines[index]), cells(lines[index + 1])
        return (len(header) >= 2 and len(header) == len(delimiter)
                and all(re.fullmatch(r':?-+:?', cell) for cell in delimiter))

    def outer_row(line):
        return bool(re.match(r'^ {0,3}\|', line) and re.search(r'(?<!\\)\|\s*$', line)
                    and len(cells(line)) >= 2)

    result, state, fence = [], 'outside', None
    index = 0
    while index < len(lines):
        line = lines[index]
        opening = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if re.fullmatch(r' {0,3}' + re.escape(fence[0]) +
                            r'{' + str(len(fence)) + r',}\s*', line):
                fence = None
            index += 1
            continue
        if opening and (opening.group(1)[0] != '`' or '`' not in opening.group(2)):
            fence, state = opening.group(1), 'outside'
        elif header_at(index):
            state = 'table'
            index += 1  # delimiter
        elif not line.strip():
            if state == 'table':
                state = 'after_blank'
        elif (state == 'table' and '|' in line
              and not re.match(r'^ {0,3}#{1,6}(?:\s|$)', line)):
            pass
        elif state == 'after_blank' and outer_row(line):
            result.append(index + 1)
        else:
            state = 'outside'
        index += 1
    return result


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []

    def error(path, message):
        errors.append({'path': str(path), 'error': message})

    required = ['SKILL.md', 'agents/openai.yaml', 'THIRD_PARTY_NOTICES.md',
                'scripts/calculators.py', 'scripts/test_calculators.py']
    required += ['operations/' + name + '.md' for name in OPERATIONS]
    required += ['references/' + name + '.md' for name in REFERENCES]
    required += ['references/normative/index.md', 'references/normative/ru/index.md',
                 'references/normative/ru/applicability.md',
                 'references/normative/ru/routes.md']
    required += ['references/normative/ru/' + name + '.md'
                 for name in NORMATIVE_GROUPS]
    for name in required:
        if not (root / name).is_file():
            error(name, 'required file missing')
    for path in sorted(root.rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        if not text.strip():
            error(path.relative_to(root), 'empty Markdown')
        if re.search(r'\b(?:TODO|TBD|FIXME)\b', text):
            error(path.relative_to(root), 'unfinished placeholder')
        if len(text.splitlines()) > 100 and '## Contents' not in text:
            error(path.relative_to(root), 'long reference needs Contents')
        for line in orphan_table_rows(text):
            error(path.relative_to(root),
                  f'line {line}: pipe row follows a blank-broken table; '
                  'restore continuity or add a table header and delimiter')
        prose = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
        for target in LINK.findall(prose) + DEFINITION.findall(prose):
            uri = urlsplit(target.strip('<>'))
            if uri.scheme or uri.netloc:
                continue
            destination = ((path.parent / unquote(uri.path)).resolve()
                           if uri.path else path)
            if not destination.is_relative_to(root):
                error(path.relative_to(root), 'local link escapes skill: ' + target)
            elif not destination.exists():
                error(path.relative_to(root), 'local link missing: ' + target)
            elif uri.fragment and destination.suffix == '.md':
                if unquote(uri.fragment) not in anchors(destination.read_text(encoding='utf-8')):
                    error(path.relative_to(root), 'anchor missing: ' + target)
    skill = root / 'SKILL.md'
    if skill.exists():
        text = skill.read_text(encoding='utf-8')
        front = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        if not front or not re.search(r'^name: architecture$', front.group(1), re.M):
            error('SKILL.md', 'expected architecture frontmatter name')
        if not front or not re.search(r'^description: .+', front.group(1), re.M):
            error('SKILL.md', 'description missing')
        if len(text.splitlines()) > 500:
            error('SKILL.md', 'root exceeds 500 lines')
        for operation in OPERATIONS:
            if 'operations/' + operation + '.md' not in text:
                error('SKILL.md', 'operation route missing: ' + operation)
    interface = root / 'agents/openai.yaml'
    if interface.exists() and not re.search(
            r'^\s+allow_implicit_invocation:\s+false\s*$',
            interface.read_text(encoding='utf-8'), re.M):
        error('agents/openai.yaml', 'explicit invocation policy missing')
    for path in sorted((root / 'scripts').glob('*.py')):
        try:
            compile(ast.parse(path.read_text(encoding='utf-8')), str(path), 'exec')
        except SyntaxError as exc:
            error(path.relative_to(root), 'Python syntax: ' + str(exc))
    calculator_reference = root / 'references/calculators.md'
    if calculator_reference.exists():
        audited = re.findall(r'^\| [AB] `([a-z_]+\.py)` \|',
                             calculator_reference.read_text(encoding='utf-8'), re.M)
        if len(audited) != 14 or len(set(audited)) != 14:
            error('references/calculators.md', 'expected 14 unique calculator audit rows')
    record_count = 0
    normative = root / 'references/normative'
    for path in sorted(normative.rglob('*.md')):
        # These pages route or explain the catalogue, rather than hold records.
        if path.name in ('index.md', 'routes.md', 'applicability.md'):
            continue
        records = 0
        for section in re.split(r'(?m)^## ', path.read_text(encoding='utf-8'))[1:]:
            title, _, body = section.partition('\n')
            # Existing record headings are stable, hyphenated identifiers with
            # a number. Recognize those even if every field has been removed;
            # fields also identify records with a different heading convention.
            has_field = any('**' + field + ':**' in body for field in RECORD_FIELDS)
            record_heading = re.fullmatch(r'(?=[a-z0-9-]*\d)[a-z0-9]+(?:-[a-z0-9]+)+', title)
            if not (has_field or record_heading):
                continue
            records += 1
            for field in RECORD_FIELDS:
                if not re.search(r'\*\*' + re.escape(field) + r':\*\*\s*\S', body):
                    error(path.relative_to(root), title + ': record field missing: ' + field)
            if not re.search(r'https?://[^\s)]+', body):
                error(path.relative_to(root), title + ': source link missing')
            if not re.search(r'Checked \d{4}-\d{2}-\d{2}', body):
                error(path.relative_to(root), title + ': verification date missing')
        if path.parent == normative / 'ru' and path.stem in NORMATIVE_GROUPS and not records:
            error(path.relative_to(root), 'no populated normative records')
        record_count += records
    return {'valid': not errors, 'operation_count': len(OPERATIONS),
            'normative_record_count': record_count, 'errors': errors}


if __name__ == '__main__':
    try:
        result = validate()
    except (OSError, UnicodeError, ValueError) as exc:
        result = {'valid': False, 'errors': [{'error': str(exc)}]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result['valid'] else 1)
