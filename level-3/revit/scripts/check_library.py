#!/usr/bin/env python3
"""Validate blocks offline, without running snippets or accessing Revit.
Runtime evidence may be a contained local file or an explicit HTTPS artifact URL.
Remote evidence content and authenticity are not fetched or attested.
"""
import argparse
import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

FIELDS = ('id', 'group', 'status', 'runtime', 'verification', 'dependencies', 'mutation')
HEADINGS = ('Contract', 'Purpose', 'Inputs and outputs', 'Implementation',
            'Adaptation and limits', 'Verification', 'Provenance')
GROUPS = ('core', 'mep', 'views')
REQUIRED = ['SKILL.md', 'assets/blocks/catalog.md', 'assets/examples/graph-contract.dyn'] + [
    'operations/' + name + '.md' for name in
    ('creation', 'adaptation', 'diagnostics', 'borrowing')] + [
    'references/' + name + '.md' for name in
    ('runtime', 'dynamo', 'transactions', 'parameters-and-units',
     'geometry-and-connectors', 'annotations-and-references', 'error-patterns')]
PLACEHOLDER = re.compile(r'\b(TODO|TBD|FIXME)\b|\[placeholder\]', re.I)
DEFINITION = re.compile(r'^\s{0,3}\[[^\]\n]+\]:\s*<?([^\s>]+)>?', re.M)
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')


def sections(text):
    """Parse level-two headings outside fenced code, retaining duplicate headings."""
    result, active, fenced = {}, None, False
    for line in text.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            fenced = not fenced
        match = None if fenced else re.match(r'^##\s+(.+?)\s*#*$', line)
        if match:
            active = match.group(1)
            result.setdefault(active, []).append([])
        elif active:
            result[active][-1].append(line)
    return {key: ['\n'.join(part).strip() for part in parts] for key, parts in result.items()}


def metadata(text):
    parts = sections(text).get('Contract', [])
    errors, data = [], {}
    if len(parts) != 1:
        return data, ['expected exactly one ## Contract heading']
    rows = [line.strip() for line in parts[0].splitlines() if line.strip().startswith('|')]
    if len(rows) < 2 or [x.strip().lower() for x in rows[0].strip('|').split('|')] != ['field', 'value']:
        errors.append('Contract must start with a Field / Value Markdown table')
    if len(rows) < 2 or not re.fullmatch(r'\|\s*:?-+:?\s*\|\s*:?-+:?\s*\|', rows[1]):
        errors.append('Contract table requires a two-column separator row')
    for row in rows[2:]:
        cells = [x.strip() for x in row.strip('|').split('|')]
        if len(cells) != 2:
            errors.append('Contract rows require exactly two columns')
            continue
        key, value = cells
        if key in data:
            errors.append('duplicate Contract field: ' + key)
        data[key] = value
    for key in FIELDS:
        if not data.get(key):
            errors.append('missing or empty Contract field: ' + key)
    for key in data:
        if key not in FIELDS:
            errors.append('unknown Contract field: ' + key)
    return data, errors


def anchor_ids(text):
    ids, count, fenced = set(), {}, False
    for line in text.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            fenced = not fenced
        match = None if fenced else re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if match:
            slug = re.sub(r'[^\w\- ]', '', match.group(1).lower()).replace(' ', '-')
            suffix = count.get(slug, 0)
            ids.add(slug if suffix == 0 else slug + '-' + str(suffix))
            count[slug] = suffix + 1
    return ids


def link_errors(path, text, root):
    errors = []
    # Ignore code examples, where Markdown links are literal data.
    prose = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
    for target in LINK.findall(prose) + DEFINITION.findall(prose):
        try:
            uri = urlsplit(target.strip('<>'))
        except ValueError:
            errors.append('malformed link URL: ' + target)
            continue
        if uri.scheme or uri.netloc:
            continue
        local = (path.parent / unquote(uri.path)).resolve() if uri.path else path.resolve()
        if not local.is_relative_to(root.resolve()):
            errors.append('local link escapes skill root: ' + target)
        elif not local.exists():
            errors.append('local link does not exist: ' + target)
        elif uri.fragment and local.suffix.lower() == '.md':
            try:
                if unquote(uri.fragment) not in anchor_ids(local.read_text(encoding='utf-8-sig')):
                    errors.append('local link anchor does not exist: ' + target)
            except (OSError, UnicodeError) as exc:
                errors.append('cannot read local link: ' + str(exc))
    return errors


def evidence_target(target, path, root):
    """Validate an evidence location, never its contents or runtime authenticity."""
    target = target.strip('<>')
    try:
        uri = urlsplit(target)
        if uri.scheme or uri.netloc:
            host = uri.hostname or ''
            host_valid = bool(host and all(re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?',
                                                      label) for label in host.rstrip('.').split('.')))
            return (uri.scheme == 'https' and host_valid and uri.port != 0 and
                    not uri.username and not uri.password and uri.path not in ('', '/') and
                    not re.search(r'\\|\s|%(?![0-9A-Fa-f]{2})', target))
        local = (path.parent / unquote(uri.path)).resolve()
        return bool(uri.path and local.is_relative_to(root.resolve()) and local.is_file())
    except (ValueError, OSError):
        return False


def check_block(path, root):
    text = path.read_text(encoding='utf-8-sig')
    data, errors = metadata(text)
    sec = sections(text)
    for heading in HEADINGS:
        if len(sec.get(heading, [])) != 1 or not sec[heading][0]:
            errors.append('requires one nonempty ## ' + heading)
    for heading in ('Verification', 'Provenance'):
        if PLACEHOLDER.search('\n'.join(sec.get(heading, []))):
            errors.append(heading + ' contains an unfinished placeholder')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', data.get('id', '')):
        errors.append('id must be kebab-case')
    if data.get('id') != path.stem:
        errors.append('id must match filename stem')
    if data.get('group') not in GROUPS or data.get('group') != path.parent.name:
        errors.append('group must be core, mep or views and match parent folder')
    for key, allowed in [('status', ('draft', 'reviewed')),
                         ('verification', ('static', 'offline', 'runtime')),
                         ('mutation', ('read-only', 'document-write', 'view-write', 'file-write'))]:
        if data.get(key) not in allowed:
            errors.append(key + ' must be one of: ' + ', '.join(allowed))
    if PLACEHOLDER.search(data.get('runtime', '')):
        errors.append('runtime contains an unfinished placeholder')
    dep = data.get('dependencies', '')
    dependencies = [] if dep == 'none' else [d.strip() for d in dep.split(',')]
    if dep != 'none' and (not dependencies or any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', d) for d in dependencies)):
        errors.append('dependencies must be comma-separated kebab-case IDs or none')
    if len(dependencies) != len(set(dependencies)):
        errors.append('duplicate dependency')
    implementation = '\n'.join(sec.get('Implementation', []))
    fences = re.findall(r'(?ms)^```([^\n]*)\n(.*?)^```\s*$', implementation)
    if len(fences) != 1 or fences[0][0].strip() != 'python' or not fences[0][1].strip():
        errors.append('Implementation requires exactly one nonempty ```python fence')
    else:
        try:
            tree = ast.parse(fences[0][1], filename=str(path))
            compile(fences[0][1], str(path), 'exec')
            if re.search(r'2\.7|IronPython2', data.get('runtime', ''), re.I):
                py3 = (ast.JoinedStr, ast.AnnAssign, ast.AsyncFunctionDef, ast.AsyncFor,
                       ast.AsyncWith, ast.Await, ast.NamedExpr, ast.Nonlocal, ast.YieldFrom)
                for node in ast.walk(tree):
                    incompatible = isinstance(node, py3)
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        incompatible |= bool(node.returns or node.args.kwonlyargs or node.args.posonlyargs
                                             or any(a.annotation for a in node.args.args))
                    if isinstance(node, ast.Raise):
                        incompatible |= node.cause is not None
                    if incompatible:
                        errors.append('Python 3-only syntax conflicts with declared Python 2.7 runtime')
                        break
        except SyntaxError as exc:
            errors.append('Python syntax error at line {}: {}'.format(exc.lineno, exc.msg))
    verification = '\n'.join(sec.get('Verification', []))
    evidence = LINK.findall(verification) + DEFINITION.findall(verification)
    if data.get('verification') == 'runtime' and not any(
            evidence_target(t, path, root) for t in evidence):
        errors.append('runtime verification requires a linked evidence artifact in ## Verification (contained local file or valid HTTPS artifact URL)')
    errors.extend(link_errors(path, text, root))
    data['dependencies'] = dependencies
    return data, errors


def validate(root, catalog_mode=False):
    root = Path(root).resolve()
    errors, blocks = [], []
    for name in REQUIRED:
        if catalog_mode and name == 'assets/blocks/catalog.md':
            continue
        if not (root / name).is_file():
            errors.append({'path': name, 'error': 'required file missing'})
    skill = root / 'SKILL.md'
    if skill.is_file():
        text = skill.read_text(encoding='utf-8-sig')
        front = re.match(r'\A---\s*\n(.*?)\n---\s*(?:\n|$)', text, re.S)
        for key in ('name', 'description'):
            matches = re.findall(r'^' + key + r':\s*(.+)$', front.group(1), re.M) if front else []
            if len(matches) != 1 or not matches[0].strip().strip('\"\'') or PLACEHOLDER.search(matches[0]):
                errors.append({'path': 'SKILL.md', 'error': 'frontmatter needs nonempty ' + key})
    block_root = root / 'assets/blocks'
    paths = sorted(p for p in block_root.rglob('*.md') if p.name != 'catalog.md') if block_root.exists() else []
    if not paths:
        errors.append({'path': 'assets/blocks', 'error': 'library contains no blocks'})
    for path in paths:
        data, found = check_block(path, root)
        data['path'] = path.relative_to(root).as_posix()
        blocks.append(data)
        errors.extend({'path': data['path'], 'error': error} for error in found)
    by_id = {}
    for block in blocks:
        ident = block.get('id', '')
        if ident in by_id:
            errors.append({'path': block['path'], 'error': 'duplicate block id: ' + ident})
        by_id[ident] = block
        for dep in block['dependencies']:
            if dep not in {b.get('id') for b in blocks}:
                errors.append({'path': block['path'], 'error': 'unknown dependency: ' + dep})
    visited, active = set(), set()
    def visit(ident):
        if ident in active:
            errors.append({'path': by_id[ident]['path'], 'error': 'dependency cycle involving ' + ident})
        elif ident not in visited and ident in by_id:
            active.add(ident)
            for dep in by_id[ident]['dependencies']:
                visit(dep)
            active.remove(ident)
            visited.add(ident)
    for ident in sorted(by_id):
        visit(ident)
    for path in sorted(root.rglob('*.md')):
        if path not in paths and not (catalog_mode and path == block_root / 'catalog.md'):
            errors.extend({'path': path.relative_to(root).as_posix(), 'error': e}
                          for e in link_errors(path, path.read_text(encoding='utf-8-sig'), root))
    return {'valid': not errors, 'blocks': blocks, 'errors': errors}


def catalog(blocks):
    lines = ['# Block catalog', '', 'Derived from block contracts by `scripts/check_library.py --catalog`.', '']
    for group in GROUPS:
        lines += ['## ' + group, '', '| Block | Status | Runtime | Verification | Dependencies | Mutation |',
                  '| --- | --- | --- | --- | --- | --- |']
        for b in sorted((b for b in blocks if b['group'] == group), key=lambda b: b['id']):
            values = ['[{}]({}/{})'.format(b['id'], group, b['id'] + '.md'), b['status'], b['runtime'],
                      b['verification'], ', '.join(b['dependencies']) or 'none', b['mutation']]
            lines.append('| ' + ' | '.join(v.replace('|', '\\|') for v in values) + ' |')
        lines.append('')
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default=str(Path(__file__).resolve().parents[1]))
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--show-block', metavar='ID')
    modes.add_argument('--catalog', action='store_true')
    args = parser.parse_args(argv)
    try:
        root = Path(args.root).resolve()
        if args.show_block:
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.show_block):
                raise ValueError('invalid block ID')
            paths = [root / 'assets/blocks' / g / (args.show_block + '.md') for g in GROUPS]
            matches = [p for p in paths if p.is_file()]
            if len(matches) != 1:
                raise ValueError('expected one block for ID: ' + args.show_block)
            print(matches[0].read_text(encoding='utf-8-sig'), end='')
            return 0
        result = validate(root, catalog_mode=args.catalog)
        if args.catalog and result['valid']:
            print(catalog(result['blocks']))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0 if result['valid'] else 1
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(json.dumps({'valid': False, 'errors': [{'path': args.root, 'error': str(exc)}]}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
