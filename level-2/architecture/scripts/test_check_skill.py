import tempfile
import unittest
from pathlib import Path

import check_skill


class PilotRouteTests(unittest.TestCase):
    def test_migrated_selectors_replace_flat_requirements(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for branch in ('program', 'composition', 'performance'):
                index = root / 'references' / branch / 'index.md'
                index.parent.mkdir(parents=True)
                index.write_text('# Subject\n\n[Method](method.md#complete-method)\n')
                (index.parent / 'method.md').write_text('# Method\n\n## Complete method\n\nLocal reasoning.\n')
            result = check_skill.validate(root)
            relevant = [e for e in result['errors'] if any(
                part in e['path'] for part in ('program', 'composition', 'performance'))]
            self.assertEqual(relevant, [])
            (root / 'references/performance/index.md').unlink()
            self.assertIn({'path': 'references/performance/index.md',
                           'error': 'required file missing'},
                          check_skill.validate(root)['errors'])

    def test_selector_checks_target_and_fragment_not_just_file_presence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            index = root / 'index.md'
            index.write_text('# Subject\n\n[Method](method.md#complete-method)\n')
            self.assertIn({'path': 'index.md',
                           'error': 'local link missing: method.md#complete-method'},
                          check_skill.validate(root)['errors'])
            (root / 'method.md').write_text('# Method\n\n## A different question\n')
            self.assertIn({'path': 'index.md',
                           'error': 'anchor missing: method.md#complete-method'},
                          check_skill.validate(root)['errors'])
            (root / 'method.md').write_text('# Method\n\n## Complete method\n')
            self.assertFalse(any('link missing' in e['error'] or 'anchor missing' in e['error']
                                 for e in check_skill.validate(root)['errors']))


class MultilineLinkTests(unittest.TestCase):
    def test_missing_target_or_fragment_in_multiline_links(self):
        cases = (
            ('[Missing\nmethod](missing.md)', 'local link missing: missing.md'),
            ('[Existing\nmethod](method.md#missing)',
             'anchor missing: method.md#missing'),
            ('![Missing\nimage](missing.svg)', 'local link missing: missing.svg'),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'method.md').write_text('# Method\n\n## Complete method\n', encoding='utf-8')
            for text, error in cases:
                with self.subTest(text=text):
                    (root / 'index.md').write_text(text + '\n', encoding='utf-8')
                    self.assertIn({'path': 'index.md', 'error': error},
                                  [e for e in check_skill.validate(root)['errors']
                                   if e['path'] == 'index.md'])

    def test_valid_multiline_links_and_fenced_examples(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'method.md').write_text('# Method\n\n## Complete method\n', encoding='utf-8')
            (root / 'diagram.svg').write_text('<svg/>', encoding='utf-8')
            (root / 'index.md').write_text('''# Index

[Local
method](method.md#complete-method)
![Local
image](diagram.svg)
[External
source](https://example.com/source)

```markdown
[Illustrative
link](absent.md)
```
''', encoding='utf-8')
            self.assertFalse(any('local link' in error['error'] or 'anchor missing' in error['error']
                                 for error in check_skill.validate(root)['errors']))


class GraphIntegrityTests(unittest.TestCase):
    def test_reference_links_and_fenced_examples(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'method.md').write_text('# Method\n\n## Verified\n')
            (root / 'index.md').write_text('''# Index

[The selected method][method]

[method]: method.md#verified

~~~markdown
[Fenced example](absent.md)
[unused]: absent-too.md
~~~
````markdown
```nested example
[Another fenced example](also-absent.md)
```
````
''')
            def errors():
                return [e for e in check_skill.validate(root)['errors']
                        if e['path'] == 'index.md']
            self.assertEqual(errors(), [])
            (root / 'method.md').write_text('# Method\n\n## Other\n')
            self.assertEqual(errors(), [{'path': 'index.md',
                                        'error': 'anchor missing: method.md#verified'}])
            (root / 'method.md').unlink()
            self.assertEqual(errors(), [{'path': 'index.md',
                                        'error': 'local link missing: method.md#verified'}])

    def test_duplicate_heading_bases_are_reported_without_rejecting_fenced_titles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'method.md'
            path.write_text('# Method\n\n## Repeated?\n\n## Repeated!\n')
            self.assertIn({'path': 'method.md', 'error': 'duplicate heading anchor base: repeated'},
                          check_skill.validate(root)['errors'])
            path.write_text('# Method\n\n## Repeated?\n\n~~~\n## Repeated!\n~~~\n')
            self.assertFalse(any('duplicate heading' in e['error']
                                 for e in check_skill.validate(root)['errors']))

    def test_provenance_or_maintenance_cannot_be_the_only_runtime_route(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'sources').mkdir()
            (root / 'maintenance').mkdir()
            (root / 'SKILL.md').write_text('# Entry\n\n[Sources](sources/index.md)\n[Plan](maintenance/plan.md)\n')
            (root / 'sources/index.md').write_text('# Sources\n\n[Recipient](../method.md)\n')
            (root / 'maintenance/plan.md').write_text('# Plan\n\n[Future owner](../method.md)\n')
            (root / 'method.md').write_text('# Method\n\nComplete local reasoning.\n')
            expected = {'path': 'method.md',
                        'error': 'runtime document unreachable without provenance/maintenance'}
            self.assertIn(expected, check_skill.validate(root)['errors'])
            with (root / 'SKILL.md').open('a') as stream:
                stream.write('[Known method](method.md)\n')
            self.assertNotIn(expected, check_skill.validate(root)['errors'])

    def test_reciprocal_graph_and_selected_loading_have_no_hop_quota(self):
        graph = {'a': {'b', 'unselected'}, 'b': {'a', 'c'},
                 'c': {'b', 'd'}, 'd': set(), 'unselected': {'a'}}
        self.assertEqual(check_skill.reachable(graph, ['a']), set(graph))
        self.assertEqual(check_skill.reachable(graph, ['a'], {'a', 'b', 'c', 'd'}),
                         {'a', 'b', 'c', 'd'})
        self.assertEqual(check_skill.reachable(graph, ['a'], {'a', 'b'}), {'a', 'b'})


class TableContinuityTests(unittest.TestCase):
    def test_blank_breaks_leave_provenance_rows_outside_table(self):
        text = '''| Source and extent | Adaptation |
| --- | --- |
| Book A, selected pages | Bounded method |
| Museum evidence | Case analysis |

| Book B, selected pages | Another case |
| Operator evidence | Interpretation |

| Book C | Further method |
'''
        self.assertEqual(check_skill.orphan_table_rows(text), [6, 7, 9])

    def test_valid_separate_tables_and_prose(self):
        text = '''| Source | Use |
| --- | --- |
| A | One |

| Source | Use |
| :--- | ---: |
| B | Two |

## Another topic

| Source | Use |
| --- | --- |
| C | Three |

Normal prose discusses `a | b` and another line.

| This is ordinary prose with a pipe | rather than a table continuation |
'''
        self.assertEqual(check_skill.orphan_table_rows(text), [])

    def test_fenced_code_and_inline_code_are_not_orphans(self):
        text = '''| Source | Use |
| --- | --- |
| A | One |

```markdown
| an example | not a table row |
```

~~~
| another | example |
~~~

`| inline | code |` is prose.
'''
        self.assertEqual(check_skill.orphan_table_rows(text), [])

    def test_validator_reports_file_and_actual_line(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'example.md'
            path.write_text('| Source | Use |\n| --- | --- |\n| A | One |\n\n| B | Two |\n', encoding='utf-8')
            result = check_skill.validate(root)
            self.assertIn({'path': 'example.md', 'error': 'line 5: pipe row follows a blank-broken table; restore continuity or add a table header and delimiter'}, result['errors'])
            self.assertFalse(result['valid'])


if __name__ == '__main__':
    unittest.main()
