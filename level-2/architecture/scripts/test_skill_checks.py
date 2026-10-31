"""Examples are optional; retained links and individual artifacts still matter."""
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from check_skill import ROOT, validate


class OptionalExampleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'architecture'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__'))

    def remove_example(self, filename, remove_links=True):
        (self.root / 'assets/examples' / filename).unlink()
        if remove_links:
            for path in self.root.rglob('*.md'):
                text = path.read_text(encoding='utf-8')
                text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                              lambda match: match.group(1) if match.group(2).endswith('/' + filename)
                              else match.group(0), text)
                path.write_text(text, encoding='utf-8')

    def assert_valid(self):
        result = validate(self.root)
        self.assertTrue(result['valid'], result['errors'])

    def test_skill_without_example_files_has_no_format_gate(self):
        for filename in ('pavilion-brief.md', 'pavilion-concept.svg', 'pavilion-concept.png'):
            self.remove_example(filename)
        self.assert_valid()

    def test_svg_can_stand_alone_and_is_still_validated(self):
        self.remove_example('pavilion-concept.png')
        self.assert_valid()
        (self.root / 'assets/examples/pavilion-concept.svg').write_text('<broken', encoding='utf-8')
        result = validate(self.root)
        self.assertFalse(result['valid'])
        self.assertTrue(any(error['path'].endswith('.svg') for error in result['errors']))

    def test_png_can_stand_alone_and_is_still_validated(self):
        self.remove_example('pavilion-concept.svg')
        self.assert_valid()
        (self.root / 'assets/examples/pavilion-concept.png').write_bytes(b'not a PNG')
        result = validate(self.root)
        self.assertFalse(result['valid'])
        self.assertTrue(any(error['path'].endswith('.png') for error in result['errors']))

    def test_dangling_retained_link_is_not_ignored(self):
        self.remove_example('pavilion-concept.svg', remove_links=False)
        result = validate(self.root)
        self.assertFalse(result['valid'])
        self.assertTrue(any('local link missing' in error['error'] for error in result['errors']))
        self.assertFalse(any('required file missing' in error['error'] for error in result['errors']))


if __name__ == '__main__':
    unittest.main()
