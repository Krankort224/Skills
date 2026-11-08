"""Bounded geometry/graph checks of housing and air-interface prose, not MEP."""
import math
import unittest


def area(rect):
    x0, y0, x1, y1 = rect
    return (x1 - x0) * (y1 - y0)


def overlap(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[2] <= outer[2] and outer[1] <= inner[1] <= inner[3] <= outer[3]


def transformed(rect, transform):
    """Bounding rectangle for these axis-aligned 90-degree/reflection cases."""
    x0, y0, x1, y1 = rect
    points = [transform(x, y) for x, y in [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]]
    return min(x for x, y in points), min(y for x, y in points), max(x for x, y in points), max(y for x, y in points)


def reachable(graph, start):
    seen, todo = set(), [start]
    while todo:
        node = todo.pop()
        if node not in seen:
            seen.add(node)
            todo.extend(graph.get(node, ()))
    return seen


def air_graph(owners):
    graph = {}
    for owner in owners:
        def edge(first, second):
            graph.setdefault(first, set()).add(second)
        for room in ('living', 'bed1', 'bed2'):
            edge('outside:' + owner, owner + ':' + room)
            edge(owner + ':' + room, owner + ':hall')
        for room in ('kitchen', 'bath'):
            chain = [owner + ':' + node for node in
                     ('hall', room, room + '-extract', room + '-branch', room + '-duct', room + '-roof')]
            chain.append('outside:' + owner + ':' + room)
            for first, second in zip(chain, chain[1:]):
                edge(first, second)
    return graph


def interior_components(graph):
    # Potential reverse paths; outdoor boundaries do not make one shared plenum.
    interior = {}
    for first, seconds in graph.items():
        for second in seconds:
            if first.startswith('outside:') or second.startswith('outside:'):
                continue
            interior.setdefault(first, set()).add(second)
            interior.setdefault(second, set()).add(first)
    remaining, result = set(interior), []
    while remaining:
        component = reachable(interior, next(iter(remaining)))
        result.append(component)
        remaining -= component
    return result


class HousingAirInterfacesTests(unittest.TestCase):
    def test_fitted_unit_end_wall_and_room_ledger(self):
        rooms = [(0.2, 0.2, 5.8, 4.8), (6, 0.2, 9.8, 4.8),
                 (0.2, 7.2, 4.2, 11.8), (4.4, 7.2, 7.4, 11.8),
                 (7.6, 7.2, 9.8, 9.4), (7.6, 9.6, 9.8, 11.8),
                 (0.2, 5, 9.8, 7)]
        self.assertAlmostEqual(sum(map(area, rooms)), 104.32)
        for i, first in enumerate(rooms):
            for second in rooms[i + 1:]:
                self.assertEqual(overlap(first, second), 0)
        self.assertAlmostEqual(104.32 + 8.64 + 7.04, 120)
        shaft = (7.8, 9.7, 8.85, 10.75)
        self.assertTrue(contains(rooms[5], shaft))
        self.assertAlmostEqual(104.32 - area(shaft), 103.2175)
        end = [(max(.45, x0), y0, x1, y1) for x0, y0, x1, y1 in rooms]
        self.assertAlmostEqual(sum(map(area, end)), 101.52)
        self.assertAlmostEqual(101.52 + 11.54 + 6.94, 120)
        original_side_action = (.2, 8.2, .8, 10.2)
        self.assertGreater(overlap(original_side_action, (.2, .2, .45, 11.8)), 0)
        self.assertTrue(contains(end[2], (.6, 8.2, 3.4, 10.2)))
        self.assertLess((5.8 - .65) * 4.6, 24)
        self.assertGreaterEqual((6 - .65) * 4.6, 24)
        self.assertAlmostEqual((9.8 - 6.2) * 4.6, 16.56)
        thick_end_bedroom = (.65, 7.2, 4.2, 11.8)
        self.assertTrue(contains(thick_end_bedroom, (.7, 8.2, 3.5, 10.2)))
        self.assertTrue(contains(thick_end_bedroom, (.7, 10.4, 3.9, 11.8)))
        self.assertAlmostEqual(99.28 + 13.86 + 6.86, 120)
        # Supplied furniture/actions and door sweeps, not just area sums.
        settings = [(rooms[0], (.8, 1, 3, 2.7)), (rooms[0], (3.1, .5, 5.5, 2.3)),
                    (rooms[1], (6.2, .4, 9, 3.6)), (rooms[2], (.2, 7.6, 3, 10.2)),
                    (rooms[2], (.5, 10.4, 3.7, 11.8)), (rooms[3], (4.4, 10.2, 6.6, 11.8))]
        for shell, setting in settings:
            self.assertTrue(contains(shell, setting))
        self.assertEqual(overlap((7.6, 10.85, 8.5, 11.75), shaft), 0)

    def test_regular_turn_end_and_changed_view_requirement(self):
        unit = (0, 0, 10, 12)
        regular_b = transformed(unit, lambda u, v: (24 - u, v))
        core = (10, 0, 14, 12)
        naive = transformed(regular_b, lambda x, y: (14 + y - 6, 6 - (x - 14)))
        self.assertEqual(overlap(unit, naive), 12)
        self.assertEqual(overlap(core, naive), 24)
        turn_b = transformed(unit, lambda u, v: (10 + v, -10 + u))
        turn_core = (10, 0, 18, 12)
        for first, second in [(unit, turn_b), (unit, turn_core), (turn_b, turn_core)]:
            self.assertEqual(overlap(first, second), 0)
        self.assertEqual(sum(map(area, [unit, turn_b, turn_core])), 336)
        self.assertEqual(sum(map(area, [unit, regular_b, core])), 288)
        self.assertTrue(15.55 >= turn_core[0] and 16.45 <= turn_core[2])
        self.assertEqual((10 + 6, -10 + 10), (16, 0))  # Entire 0.9 portal lies on shared edge.
        self.assertTrue(8.4 + 3 > 10)  # Initial fan hits the other wing.
        self.assertTrue(6.9 + 3 < 10)
        self.assertTrue(-10 + 6.9 + 3 < 0)
        self.assertEqual(area((22, -12, 24, 7)) + area((18, 5, 22, 7)), 46)
        self.assertEqual(overlap((22, -12, 24, 7), turn_b), 0)
        # Fresh condition: 3.5 m diagnostic and 1.2 m opening cannot both fit
        # the fixed bedroom frontage: centre must be >=6.6 and <6.5.
        self.assertGreater(6 + 1.2 / 2, 10 - 3.5)
        # A permitted nonbearing partition shift of 0.25 m recovers the test
        # without dropping the household or 24 m2 living-room requirement.
        self.assertGreaterEqual(6.4 - .6, 5.75)
        self.assertLess(6.4 + 3.5, 10)
        self.assertGreaterEqual((5.55 - .2) * 4.6, 24)
        self.assertGreaterEqual((9.8 - 5.75) * 4.6, 12)
        self.assertEqual((24 - 8.125, 10.025), (15.875, 10.025))
        self.assertEqual((10 + 10.025, -10 + 8.125), (20.025, -1.875))

    def test_supply_transfer_roof_and_cross_dwelling_isolation(self):
        owners = ('A1', 'B1', 'A2', 'B2')
        graph = air_graph(owners)
        for owner in owners:
            for room in ('living', 'bed1', 'bed2'):
                self.assertIn(owner + ':' + room, reachable(graph, 'outside:' + owner))
                paths = reachable(graph, owner + ':' + room)
                self.assertIn(owner + ':kitchen-roof', paths)
                self.assertIn(owner + ':bath-roof', paths)
        self.assertEqual(len(interior_components(graph)), 4)
        graph['A2:bed2'].remove('A2:hall')
        self.assertNotIn('A2:bath-roof', reachable(graph, 'A2:bed2'))
        graph['A2:bed2'].add('A2:hall')  # Physically reserved transfer required.
        graph['A1:bath-duct'].add('B2:bath-branch')
        self.assertTrue(any(len({node.split(':')[0] for node in c}) > 1
                            for c in interior_components(graph)))
        graph['A1:bath-duct'].remove('B2:bath-branch')
        self.assertTrue(all(len({node.split(':')[0] for node in c}) == 1
                            for c in interior_components(graph)))
        # Fresh failure: a room still reaches its exhaust, but loses its inlet.
        graph['outside:B1'].remove('B1:bed1')
        self.assertIn('B1:bath-roof', reachable(graph, 'B1:bed1'))
        self.assertNotIn('B1:bed1', reachable(graph, 'outside:B1'))

    def test_channel_growth_bath_refit_and_pressure_boundary(self):
        enclosure = (7.8, 9.7, 8.85, 10.75)
        channels = [(u, v, u + .25, v + .25) for u in (8, 8.4) for v in (9.9, 10.3)]
        for channel in channels:
            self.assertTrue(contains(enclosure, channel))
        self.assertEqual(len(channels), 4)
        taller = (7.8, 9.7, 8.85, 11.15)
        self.assertGreater(overlap(taller, (7.6, 10.85, 8.5, 11.75)), 0)
        self.assertLess(9.8 - 9.25, .8)
        corrected = (7.8, 9.3, 8.85, 10.75)
        for channel in [(u, v, u + .25, v + .25) for u in (8, 8.4) for v in (9.5, 9.9, 10.3)]:
            self.assertTrue(contains(corrected, channel))
        self.assertEqual(overlap(corrected, (7.6, 10.85, 8.5, 11.75)), 0)
        self.assertAlmostEqual(area(corrected) - area(enclosure), .42)
        bath = (7.6, 7.2, 9.8, 9.02)
        self.assertGreaterEqual(area(bath), 4)
        solids = [(8.7, 8.1, 9.6, 9), (7.8, 8.3, 8.4, 9), (9.3, 7.25, 9.8, 7.75)]
        for solid in solids:
            self.assertTrue(contains(bath, solid))
        for standing in [(7.8, 7.5, 8.4, 8.3), (8.65, 7.3, 9.25, 8.1)]:
            self.assertTrue(contains(bath, standing))
            for solid in solids:
                self.assertEqual(overlap(standing, solid), 0)
        self.assertAlmostEqual(2.2 * 2.58 - area(corrected), 4.1535)
        # Fresh five-floor case: ten independent ducts cannot fit the former
        # two-column utility-height reservation, even before the door check.
        rows = math.ceil((5 * 2) / 2)
        required = rows * .25 + (rows - 1) * .15 + 2 * .2
        self.assertGreater(required, 11.8 - 9.6)
        self.assertAlmostEqual(9.81 * 5 * (1.25 - 1.20), 2.4525)
        self.assertAlmostEqual(9.81 * 2 * (1.25 - 1.20), .981)
        self.assertLess(9.81 * 5 * (1.25 - 1.20) - 3, 0)
        self.assertLess(9.81 * 2 * (1.25 - 1.20) - 3, 0)
        self.assertLess(9.81 * 8 * (1.18 - 1.22), 0)  # Connected does not imply upward flow.


if __name__ == '__main__':
    unittest.main()
