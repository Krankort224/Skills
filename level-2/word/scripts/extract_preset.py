"""Capture a bounded style/layout draft without copying source document text."""
import copy
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from preset_markdown import flatten, parameter_table, escape
from document_tools import load_preset


def extract_preset(input_path, base='technical', section_index=0):
    doc = Document(input_path)
    if section_index < 0 or section_index >= len(doc.sections):
        raise ValueError('Selected section does not exist')
    config = copy.deepcopy(load_preset(base)); config['name'] = 'borrowed-draft'
    observed = set(); section = doc.sections[section_index]
    for key, attr in [('width_mm','page_width'), ('height_mm','page_height'), ('header_mm','header_distance'), ('footer_mm','footer_distance')]:
        val = getattr(section, attr)
        if val is not None: config['page'][key] = round(val.mm, 6); observed.add('page.' + key)
    for side in ('left','right','top','bottom'):
        val = getattr(section, side + '_margin')
        if val is not None: config['page']['margins_mm'][side] = round(val.mm, 6); observed.add('page.margins_mm.' + side)
    omitted_styles = []
    for style in doc.styles:
        if style.type != WD_STYLE_TYPE.PARAGRAPH: continue
        if any(c in style.name for c in '.\\\n\r'):
            omitted_styles.append(style.name); continue
        # Only borrow existing semantic roles; custom roles need an explicit mapping.
        if style.name not in config['styles']: continue
        spec = config['styles'][style.name]; font = style.font; pf = style.paragraph_format
        props = {'font': font.name, 'size_pt': font.size.pt if font.size else None,
                 'bold': font.bold, 'italic': font.italic,
                 'color': str(font.color.rgb) if font.color.rgb else None,
                 'before_pt': pf.space_before.pt if pf.space_before is not None else None,
                 'after_pt': pf.space_after.pt if pf.space_after is not None else None,
                 'keep_with_next': pf.keep_with_next}
        if isinstance(pf.line_spacing, float): props['line_spacing'] = pf.line_spacing
        for key, value in props.items():
            if value is not None: spec[key] = value; observed.add('styles.' + style.name + '.' + key)
    # Record direct-property presence, never the source wording or numeric duplication.
    direct = []
    for index, paragraph in enumerate(doc.paragraphs):
        ppr = paragraph._p.pPr
        pkeys = sorted({el.tag.rsplit('}',1)[-1] for el in ppr}) if ppr is not None else []
        rkeys = sorted({el.tag.rsplit('}',1)[-1] for run in paragraph.runs if run._r.rPr is not None for el in run._r.rPr})
        if pkeys or rkeys:
            direct.append({'paragraph_index': index, 'style': paragraph.style.name,
                           'paragraph_properties': pkeys, 'run_properties': rkeys})
    unobserved = sorted(path for path, _ in flatten(config) if path not in observed and path not in ('name','version'))
    diagnostics = {'status': 'draft', 'base': str(base), 'section_index': section_index,
                   'observed_paths': sorted(observed), 'defaulted_paths': unobserved,
                   'direct_formatting': direct, 'omitted_style_names': omitted_styles,
                   'limitations': ['Only selected section geometry and explicitly defined properties of matching semantic paragraph styles are borrowed.',
                                   'Inherited/theme fonts, exact line heights, custom style mappings, numbering, table styles, columns, headers/footers, objects, and direct formatting are not transferred.',
                                   'Body paragraphs are inspected for direct property names; tables, headers, footers and other stories need manual inspection.',
                                   'Source text and media are not copied. Render and compare before marking ready.']}
    lines = ['# Borrowed style draft', '', 'Status: draft', '', '## Purpose', '',
             'A bounded borrowing draft; finish review of defaults and render against the reference before changing Status to ready.', '',
             '## Semantic roles', '', 'Matching named paragraph styles are reused. Map custom styles manually.', '',
             '## Composition', '', 'Selected section geometry is borrowed. Other composition details require inspection.', '',
             '## Adaptation', '', 'Review every defaulted path, reconcile direct overrides, and visually compare a representative result.', '',
             '## Dependencies', '', 'Uses the toolkit and fonts named in Parameters. No source binary is required to apply the finished preset.', '',
             '## Provenance', '', 'Extracted from a supplied DOCX without retaining its text or filename. Explicit base: ' + escape(base) + '.', '',
             '## Capture observations', '', 'Observed paths:', '']
    lines.extend('- `' + escape(p) + '`' for p in sorted(observed))
    lines += ['', '## Unobserved defaults', '', 'These paths retain values from the nominated base; they are not captured evidence.', '']
    lines.extend('- `' + escape(p) + '`' for p in unobserved)
    lines += ['', '## Direct formatting observations', '', 'Source body order only; property names record overrides without copying text. Details are also returned by the CLI.', '']
    for item in direct:
        # ordinal is an observation, not a reusable design parameter
        lines.append('- Body paragraph index ' + str(item['paragraph_index']) + ': style `' + escape(item['style']) + '`; paragraph properties ' + ', '.join(item['paragraph_properties']) + '; run properties ' + ', '.join(item['run_properties']) + '.')
    lines += ['', '## Limitations', ''] + ['- ' + s for s in diagnostics['limitations']]
    if omitted_styles: lines += ['', 'Style names containing dots, backslashes, or line breaks require manual renaming/mapping; omitted names are returned by the CLI.']
    return '\n'.join(lines) + '\n\n' + parameter_table(config), diagnostics
