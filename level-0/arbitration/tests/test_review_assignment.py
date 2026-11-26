import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'review_assignment.py'
PACKET = {'source': 'Построй мост', 'amendments': ['Без стали', 'Только расчёт'],
          'recipient': 'Engineer', 'assignment': 'Рассчитать деревянный мост.\n'}


def invoke(mode, value):
    return subprocess.run([sys.executable, str(SCRIPT), mode],
                          input=json.dumps(value, ensure_ascii=False).encode('utf-8'),
                          capture_output=True, timeout=10)


def reviewed(packet=PACKET):
    result = invoke('show', packet)
    if result.returncode:
        raise AssertionError(result.stderr.decode())
    return json.loads(result.stdout)


def decision(show, value='send'):
    return {'packet': show['packet'], 'digest': show['digest'],
            'comparison': 'Расчёт следует исходной задаче и поправкам.',
            'reason': 'Поручение в пределах задачи.', 'decision': value}


class AssignmentReviewTests(unittest.TestCase):
    def test_round_trip_preserves_unicode_and_exact_payload(self):
        show = reviewed()
        self.assertEqual(show['packet'], PACKET)
        result = invoke('decide', decision(show))
        self.assertEqual(result.returncode, 0, result.stderr)
        final = json.loads(result.stdout)
        self.assertEqual(final['packet'], PACKET)
        self.assertEqual(final['decision'], 'send')
        self.assertTrue(final['ready'])
        self.assertEqual(final['comparison'], decision(show)['comparison'])

    def test_any_changed_field_or_amendment_order_rejected(self):
        show = reviewed()
        for field in ('source', 'recipient', 'assignment', 'amendments'):
            with self.subTest(field=field):
                data = decision(copy.deepcopy(show))
                if field == 'amendments':
                    data['packet'][field].reverse()
                else:
                    data['packet'][field] += '!'
                result = invoke('decide', data)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(b'packet changed', result.stderr)

    def test_revise_and_fresh_review(self):
        show = reviewed()
        result = json.loads(invoke('decide', decision(show, 'revise')).stdout)
        self.assertFalse(result['ready'])
        changed = copy.deepcopy(PACKET)
        changed['assignment'] = 'Пересчитать.'
        next_show = reviewed(changed)
        self.assertNotEqual(show['digest'], next_show['digest'])
        self.assertTrue(json.loads(invoke('decide', decision(next_show)).stdout)['ready'])

    def test_missing_and_invalid_inputs(self):
        for field in ('source', 'recipient', 'assignment'):
            bad = copy.deepcopy(PACKET)
            bad[field] = '   '
            self.assertNotEqual(invoke('show', bad).returncode, 0)
        for amendments in (None, [''], 'new'):
            bad = dict(PACKET, amendments=amendments)
            self.assertNotEqual(invoke('show', bad).returncode, 0)
        self.assertNotEqual(invoke('show', dict(PACKET, extra='ignored?')).returncode, 0)
        for field, value in (('comparison', ''), ('reason', ' '), ('decision', 'yes'), ('digest', 'wrong')):
            bad = decision(reviewed())
            bad[field] = value
            self.assertNotEqual(invoke('decide', bad).returncode, 0)

    def test_no_amendments_and_short_valid_reasons(self):
        show = reviewed(dict(PACKET, amendments=[]))
        data = decision(show)
        data['comparison'] = 'Да'
        data['reason'] = 'Да'
        self.assertEqual(invoke('decide', data).returncode, 0)


if __name__ == '__main__':
    unittest.main()
