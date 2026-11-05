import tempfile
import unittest
from pathlib import Path

import check_skill


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
