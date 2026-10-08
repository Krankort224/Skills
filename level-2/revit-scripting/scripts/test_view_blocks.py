#!/usr/bin/env python3
"""Offline fence tests; API doubles do not validate native Revit behavior."""
import copy
import math
import re
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


BLOCKS = Path(__file__).resolve().parents[1] / 'assets/blocks/views'


def load_block(name):
    text = (BLOCKS / (name + '.md')).read_text(encoding='utf-8')
    code = re.findall(r'(?ms)^```python\n(.*?)^```\s*$', text)
    if len(code) != 1:
        raise AssertionError('Expected one canonical implementation')
    namespace = {}
    exec(compile(code[0], name, 'exec'), namespace)
    return namespace


class Eid:
    def __init__(self, value):
        self.IntegerValue = value

    def __eq__(self, other):
        return isinstance(other, Eid) and self.IntegerValue == other.IntegerValue

    def __ne__(self, other):
        return not self == other


Eid.InvalidElementId = Eid(-1)


class Color:
    def __init__(self, *rgb):
        self.rgb = rgb


class Ogs:
    def __init__(self, baseline):
        self.settings = copy.deepcopy(baseline.settings)

    def SetSurfaceForegroundPatternId(self, value):
        self.settings['surface_id'] = value

    def SetSurfaceForegroundPatternColor(self, value):
        self.settings['surface_color'] = value.rgb

    def SetSurfaceForegroundPatternVisible(self, value):
        self.settings['surface_visible'] = value


class Fill:
    def __init__(self, value, target='Drafting', solid=True):
        self.Id = Eid(value)
        self.pattern = types.SimpleNamespace(Target=target, IsSolidFill=solid)

    def GetFillPattern(self):
        return self.pattern


class Collector:
    def __init__(self, doc):
        self.doc = doc

    def OfClass(self, _class):
        return self.doc.fills


class Document:
    IsFamilyDocument = False

    def __init__(self):
        self.elements = {}
        self.fills = [Fill(2, 'Model'), Fill(7), Fill(4), Fill(1, solid=False)]

    def GetElement(self, eid):
        return self.elements.get(eid.IntegerValue)

    def add(self, value):
        item = types.SimpleNamespace(Id=Eid(value), Document=self)
        self.elements[value] = item
        return item


class View:
    IsTemplate = False

    def __init__(self, doc):
        self.Document, self.Id = doc, Eid(50)
        self.supported, self.writes = True, []
        self.baseline = types.SimpleNamespace(settings={
            'line_color': (1, 2, 3), 'cut_color': (3, 2, 1), 'background_id': 98,
            'surface_visible': False, 'surface_color': (0, 0, 0), 'surface_id': Eid(12)})

    def AreGraphicsOverridesAllowed(self):
        return self.supported

    def GetElementOverrides(self, eid):
        return self.baseline

    def SetElementOverrides(self, eid, ogs):
        self.writes.append((eid, ogs))


class Link:
    def __init__(self, doc, linked_doc, transform='transform'):
        self.Document, self.Id = doc, Eid(99)
        self.linked_doc, self.transform = linked_doc, transform

    def GetLinkDocument(self):
        return self.linked_doc

    def GetTotalTransform(self):
        return self.transform


class Ref:
    current = None

    def __init__(self, owner, linked=-1):
        self.ElementId, self.LinkedElementId = Eid(owner), Eid(linked)

    @classmethod
    def ParseFromStableRepresentation(cls, doc, stable):
        if stable == 'invalid':
            raise ValueError('Mock parse failure')
        return cls.current

    def CreateReferenceInLink(self):
        return Ref(self.LinkedElementId.IntegerValue)


def api_modules():
    db = types.ModuleType('Autodesk.Revit.DB')
    for key, value in {'ElementId': Eid, 'Color': Color, 'FillPatternElement': Fill,
                       'FillPatternTarget': types.SimpleNamespace(Drafting='Drafting'),
                       'FilteredElementCollector': Collector, 'OverrideGraphicSettings': Ogs,
                       'Reference': Ref, 'RevitLinkInstance': Link}.items():
        setattr(db, key, value)
    return {'Autodesk': types.ModuleType('Autodesk'),
            'Autodesk.Revit': types.ModuleType('Autodesk.Revit'), 'Autodesk.Revit.DB': db}


class DomainTests(unittest.TestCase):
    def setUp(self):
        self.run_domain = load_block('view-domain')['classify_view_domain']
        self.outer = [(0, 0), (10, 0), (10, 10), (0, 10)]
        self.hole = [(3, 3), (7, 3), (7, 7), (3, 7)]

    def test_holes_disjoint_regions_and_loop_order(self):
        island = [(20, 0), (22, 0), (22, 2), (20, 2)]
        loops = [self.hole[::-1], island, self.outer]
        for point, state in [((1, 1), 'INSIDE'), ((5, 5), 'OUTSIDE'),
                             ((21, 1), 'INSIDE'), ((15, 1), 'OUTSIDE')]:
            with self.subTest(point=point):
                result = self.run_domain(point, loops, 0)
                self.assertEqual(result['state'], state)
                self.assertEqual(result['inside'], state == 'INSIDE')

    def test_hole_boundary_policy_tolerance_and_closed_loop(self):
        loops = [self.outer + [self.outer[0]], self.hole]
        self.assertTrue(self.run_domain((3, 5), loops, 0)['inside'])
        result = self.run_domain((3.01, 5), loops, .02, boundary='exclude')
        self.assertEqual(result, {'state': 'BOUNDARY', 'inside': False, 'boundary_loops': [1]})

    def test_invalid_nonfinite_and_bounded_inputs(self):
        cases = [((math.nan, 0), [self.outer], 0, {}),
                 ((0, 0), [self.outer], -1, {}),
                 ((0, 0), [], 0, {}),
                 ((0, 0), [[(0, 0), (1, 1), (2, 2)]], 0, {}),
                 ((0, 0), [self.outer], 0, {'max_vertices': 3}),
                 ((0, 0), [self.outer], 0, {'boundary': 'guess'}),
                 ((True, 0), [self.outer], 0, {})]
        for point, loops, tolerance, kwargs in cases:
            with self.subTest(kwargs=kwargs, point=point):
                with self.assertRaises(ValueError):
                    self.run_domain(point, loops, tolerance, **kwargs)


class OverrideTests(unittest.TestCase):
    def setUp(self):
        self.run_overrides = load_block('graphic-overrides')['prepare_graphic_overrides']
        self.doc = Document()
        self.doc.add(10)
        self.view = View(self.doc)
        self.record = {'element_id': Eid(10), 'rgb': (255, 0, 10)}
        self.mock_api = patch.dict(sys.modules, api_modules())
        self.mock_api.start()
        self.addCleanup(self.mock_api.stop)

    def test_preserves_unrelated_settings_and_never_writes_document(self):
        baseline = copy.deepcopy(self.view.baseline.settings)
        result = self.run_overrides(self.doc, self.view, [self.record])
        self.assertEqual(result['solid_fill_id'], Eid(4))
        settings = result['entries'][0]['desired'].settings
        for key in ('line_color', 'cut_color', 'background_id'):
            self.assertEqual(settings[key], baseline[key])
        self.assertEqual(settings['surface_color'], (255, 0, 10))
        self.assertTrue(settings['surface_visible'])
        self.assertEqual(self.view.baseline.settings, baseline)
        self.assertEqual(self.view.writes, [])

    def test_invalid_records_and_fill(self):
        for records in [[self.record, self.record],
                        [{'element_id': Eid(777), 'rgb': (0, 0, 0)}],
                        [{'element_id': Eid(10), 'rgb': (True, 1, 2)}],
                        [{'element_id': Eid(10), 'rgb': (1.5, 1, 2)}],
                        [{'element_id': Eid(10), 'rgb': (256, 1, 2)}]]:
            with self.subTest(records=records):
                with self.assertRaises(ValueError):
                    self.run_overrides(self.doc, self.view, records)
        self.doc.fills = [Fill(3, 'Model')]
        with self.assertRaises(ValueError):
            self.run_overrides(self.doc, self.view, [self.record])

    def test_unsupported_scope_and_empty_input(self):
        self.assertEqual(self.run_overrides(self.doc, self.view, [])['entries'], [])
        self.view.supported = False
        with self.assertRaises(ValueError):
            self.run_overrides(self.doc, self.view, [self.record])
        with self.assertRaises(ValueError):
            self.run_overrides(Document(), self.view, [self.record])


class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.run_ref = load_block('stable-reference-preflight')['preflight_stable_reference']
        self.doc, self.linked = Document(), Document()
        self.host = self.doc.add(10)
        self.linked_owner = self.linked.add(20)
        self.link = Link(self.doc, self.linked)
        self.doc.elements[99] = self.link
        self.verdict = lambda context: {'ok': True, 'reason': 'Mock geometry accepted'}
        self.mock_api = patch.dict(sys.modules, api_modules())
        self.mock_api.start()
        self.addCleanup(self.mock_api.stop)

    def test_host_and_linked_context_resolution(self):
        Ref.current = Ref(10)
        result = self.run_ref(self.doc, 'host-stable', self.verdict)
        self.assertEqual(result['status'], 'READY')
        self.assertIs(result['owner'], self.host)
        self.assertIsNone(result['link_instance'])
        Ref.current = Ref(99, 20)
        result = self.run_ref(self.doc, 'linked-stable', self.verdict)
        self.assertEqual(result['status'], 'READY')
        self.assertIs(result['owner_document'], self.linked)
        self.assertIs(result['owner'], self.linked_owner)
        self.assertEqual(result['owner_reference'].ElementId, Eid(20))
        self.assertEqual(result['link_transform'], 'transform')

    def test_invalid_missing_unloaded_and_transform(self):
        Ref.current = Ref(999)
        self.assertEqual(self.run_ref(self.doc, 'missing', self.verdict)['status'], 'INVALID')
        self.assertEqual(self.run_ref(self.doc, 'invalid', self.verdict)['status'], 'INVALID')
        self.assertEqual(self.run_ref(self.doc, '', self.verdict)['status'], 'INVALID')
        Ref.current = Ref(99, 20)
        self.link.linked_doc = None
        self.assertEqual(self.run_ref(self.doc, 'unloaded', self.verdict)['status'], 'INVALID')
        self.link.linked_doc = self.linked
        self.link.transform = None
        self.assertEqual(self.run_ref(self.doc, 'transform', self.verdict)['status'], 'INVALID')
        self.link.transform = 'transform'
        self.linked.elements.clear()
        self.assertEqual(self.run_ref(self.doc, 'missing-linked', self.verdict)['status'], 'INVALID')

    def test_suitability_is_explicit_and_failure_is_separate(self):
        Ref.current = Ref(10)
        for callback in [lambda ctx: True, lambda ctx: {'ok': 1, 'reason': 'bad'},
                         lambda ctx: {'ok': True},
                         lambda ctx: {'ok': False, 'reason': 'Wrong geometry'}]:
            with self.subTest(callback=callback):
                result = self.run_ref(self.doc, 'host', callback)
                self.assertEqual(result['status'], 'UNSUITABLE')
        with self.assertRaises(ValueError):
            self.run_ref(self.doc, 'host', None)


if __name__ == '__main__':
    unittest.main()
