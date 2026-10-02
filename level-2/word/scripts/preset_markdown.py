"""Strict, dependency-free Markdown parameter tables for style-transfer presets."""
import math
import re


def flatten(data, prefix=''):
    for key, value in data.items():
        if any(c in key for c in '.\\\n\r'):
            raise ValueError('Parameter keys cannot contain dots, backslashes, or line breaks; rename/map the key')
        path = prefix + key
        if isinstance(value, dict):
            yield from flatten(value, path + '.')
        else:
            yield path, value


def unit_for(path):
    if path.endswith('_mm') or '.margins_mm.' in path or '.padding_mm.' in path:
        return 'mm'
    if path.endswith('_pt'): return 'pt'
    if path.endswith('.line_spacing'): return 'ratio'
    return '-'


def escape(value):
    return str(value).replace('\\', '\\\\').replace('|', '\\|').replace('\n', '\\n').replace('\r', '\\r')


def cells(line):
    if not line.startswith('|') or not line.endswith('|'):
        raise ValueError('Parameter rows require enclosing pipes')
    result, cell, escaped = [], '', False
    for char in line[1:-1]:
        if escaped:
            if char not in ('\\', '|', 'n', 'r'): raise ValueError('Unsupported table escape')
            cell += {'n': '\n', 'r': '\r'}.get(char, char); escaped = False
        elif char == '\\': escaped = True
        elif char == '|': result.append(cell.strip()); cell = ''
        else: cell += char
    if escaped: raise ValueError('Incomplete table escape')
    result.append(cell.strip())
    return result


def parameter_table(data):
    lines = ['## Parameters', '', '| Path | Value | Type | Unit |', '| --- | --- | --- | --- |']
    for path, value in flatten(data):
        kind = 'boolean' if isinstance(value, bool) else 'number' if isinstance(value, (int, float)) else 'string'
        rendered = str(value).lower() if kind == 'boolean' else str(value)
        lines.append('| ' + ' | '.join(map(escape, (path, rendered, kind, unit_for(path)))) + ' |')
    return '\n'.join(lines) + '\n'


def parse_markdown(text):
    lines = text.splitlines(); starts = [i for i, line in enumerate(lines) if line.strip() == '## Parameters']
    if len(starts) != 1: raise ValueError('Exactly one ## Parameters section required')
    section = []
    for line in lines[starts[0] + 1:]:
        if line.startswith('## '): break
        if line.strip(): section.append(line.strip())
    if len(section) < 3 or cells(section[0]) != ['Path', 'Value', 'Type', 'Unit']:
        raise ValueError('Expected Path | Value | Type | Unit table')
    if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells(section[1])) or len(cells(section[1])) != 4:
        raise ValueError('Invalid table separator')
    data = {}; seen = set()
    for line in section[2:]:
        row = cells(line)
        if len(row) != 4: raise ValueError('Expected four parameter cells')
        path, value, kind, unit = row
        parts = path.split('.')
        if any(not part or part != part.strip() for part in parts): raise ValueError('Invalid dotted path')
        if path in seen: raise ValueError('Duplicate parameter: ' + path)
        seen.add(path)
        if unit != unit_for(path): raise ValueError('Incorrect unit: ' + path)
        if kind == 'boolean':
            if value not in ('true', 'false'): raise ValueError('Boolean must be true or false')
            value = value == 'true'
        elif kind == 'number':
            if not re.fullmatch(r'-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?', value): raise ValueError('Invalid number')
            value = float(value) if any(c in value for c in '.eE') else int(value)
            if not math.isfinite(value): raise ValueError('Nonfinite number')
        elif kind != 'string': raise ValueError('Unknown parameter type')
        node = data
        for part in parts[:-1]:
            if part in node and not isinstance(node[part], dict): raise ValueError('Conflicting parameter path')
            node = node.setdefault(part, {})
        if parts[-1] in node: raise ValueError('Conflicting parameter path')
        node[parts[-1]] = value
    validate(data)
    return data


def validate(data):
    required = {'version', 'name', 'page', 'fonts', 'palette', 'styles', 'table', 'list', 'footer'}
    if set(data) != required: raise ValueError('Missing or unknown top-level preset keys')
    if type(data['version']) is not int or data['version'] != 1: raise ValueError('Unsupported preset version')
    def require(node, keys):
        if not isinstance(node, dict) or not set(keys) <= set(node): raise ValueError('Missing required preset fields: ' + ', '.join(keys))
    require(data['page'], ('width_mm', 'height_mm', 'margins_mm', 'header_mm', 'footer_mm'))
    require(data['page']['margins_mm'], ('left', 'right', 'top', 'bottom'))
    require(data['fonts'], ('body', 'code', 'fallbacks'))
    require(data['palette'], ('ink', 'muted', 'accent', 'table_header', 'table_header_text', 'alternating_row', 'border', 'note_background'))
    require(data['styles'], ('Normal',))
    require(data['table'], ('padding_mm', 'border_pt', 'repeat_header'))
    require(data['table']['padding_mm'], ('top', 'bottom', 'left', 'right'))
    require(data['list'], ('indent_mm', 'hanging_mm', 'level_step_mm', 'after_pt'))
    require(data['footer'], ('size_pt', 'color'))
    exact = [(data['page'], {'width_mm','height_mm','margins_mm','header_mm','footer_mm'}),
             (data['page']['margins_mm'], {'left','right','top','bottom'}),
             (data['fonts'], {'body','code','fallbacks'}),
             (data['palette'], {'ink','muted','accent','table_header','table_header_text','alternating_row','border','note_background'}),
             (data['table'], {'padding_mm','border_pt','repeat_header'}),
             (data['table']['padding_mm'], {'top','bottom','left','right'}),
             (data['list'], {'indent_mm','hanging_mm','level_step_mm','after_pt'}),
             (data['footer'], {'size_pt','color'})]
    if any(set(node) != keys for node, keys in exact): raise ValueError('Unknown preset field')
    if not isinstance(data['fonts']['fallbacks'], dict): raise ValueError('Font fallbacks must be a mapping')
    for role, spec in data['styles'].items():
        require(spec, ('font', 'size_pt', 'color'))
        if set(spec) - {'font', 'size_pt', 'color', 'bold', 'italic', 'before_pt', 'after_pt', 'line_spacing', 'keep_with_next'}: raise ValueError('Unknown style property')
    require(data['styles']['Normal'], ('line_spacing',))
    for path, value in flatten(data):
        leaf = path.rsplit('.', 1)[-1]
        numeric = unit_for(path) != '-'
        boolean = leaf in ('bold', 'italic', 'keep_with_next', 'repeat_header')
        if numeric:
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0: raise ValueError('Invalid nonnegative number: ' + path)
            if leaf in ('width_mm', 'height_mm', 'size_pt', 'line_spacing') and value <= 0: raise ValueError('Expected positive number: ' + path)
        elif boolean:
            if type(value) is not bool: raise ValueError('Expected boolean: ' + path)
        elif path != 'version':
            if not isinstance(value, str) or not value: raise ValueError('Expected nonempty string: ' + path)
        if path.startswith('palette.') or leaf == 'color':
            if not isinstance(value, str) or not re.fullmatch('[0-9A-Fa-f]{6}', value): raise ValueError('Invalid RGB color: ' + path)
    page = data['page']; margins = page['margins_mm']
    if page['width_mm'] <= margins['left'] + margins['right'] or page['height_mm'] <= margins['top'] + margins['bottom']: raise ValueError('Preset has no usable page area')
