"""Checks of original volume/exhibition studies; no legal or lighting simulation."""
from fractions import Fraction as F
import math
import unittest


def area(rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])


def intersects(a, b):
    return min(a[2], b[2]) > max(a[0], b[0]) and min(a[3], b[3]) > max(a[1], b[1])


def covered(rect, regions):
    """Exact subdivision on supplied millimetre coordinates, not endpoint sampling."""
    rect = tuple(round(v * 1000) for v in rect)
    regions = [tuple(round(v * 1000) for v in r) for r in regions]
    xs = sorted({rect[0], rect[2]} | {x for r in regions for x in (r[0], r[2]) if rect[0] < x < rect[2]})
    ys = sorted({rect[1], rect[3]} | {y for r in regions for y in (r[1], r[3]) if rect[1] < y < rect[3]})
    return all(any(r[0] <= x0 < x1 <= r[2] and r[1] <= y0 < y1 <= r[3] for r in regions)
               for x0, x1 in zip(xs, xs[1:]) for y0, y1 in zip(ys, ys[1:]))


def sweep(start, end, width, depth):
    assert start[0] == end[0] or start[1] == end[1]
    return (min(start[0], end[0]) - width / 2, min(start[1], end[1]) - depth / 2,
            max(start[0], end[0]) + width / 2, max(start[1], end[1]) + depth / 2)


def section_area(z, ridge=F(8), court=True):
    """Horizontal intersections of the actual gable, court and sloping wing."""
    width = F(8) if z <= 6 else max(F(0), 8 * (ridge - z) / (ridge - 6))
    main = 12 * width - (4 * min(F(4), width) if court else 0)
    wing_width = F(6) if z <= 4 else max(F(0), 3 * (6 - z))
    return main + 8 * wing_width


def sliced_above(ridge=F(8), court=True):
    # Knots include the court's lowest roof and both independent wing/eave changes.
    knots = sorted({F(0), F(4), F(6), (ridge + 6) / 2, ridge})
    return sum((hi - lo) * (section_area(lo, ridge, court) + section_area(hi, ridge, court)) / 2
               for lo, hi in zip(knots, knots[1:]))


def span(width, distance):
    return math.degrees(2 * math.atan(width / (2 * distance)))


def exposure(view_hours, view_lux, closed_lux=1):
    return view_hours * view_lux + (1200 - view_hours) * closed_lux + 8 * 100 + 2 * 80


class VolumeExhibitionTests(unittest.TestCase):
    def test_prism_mixed_solids_slices_and_changed_boundary(self):
        self.assertEqual(10 * 8 * 6, 480)
        self.assertAlmostEqual(9.6 * 7.6 * 5.5, 401.28)
        self.assertEqual(576 + 96 + 240 - 120 + 288, 1080)
        self.assertEqual(sliced_above(), 792)
        self.assertEqual(sliced_above() + 288, 1080)
        self.assertEqual(sliced_above(F(9)) + 288, 1116)
        self.assertEqual(sliced_above() + 96 * F('3.5'), 1128)
        self.assertEqual(sliced_above(court=False) + 288, 1200)
        reclassified = section_area(F(0)) * F('.5')
        self.assertEqual(reclassified, 64)
        self.assertEqual((792 - reclassified, 288 + reclassified), (728, 352))
        self.assertEqual(18 * 8 * 11 - 1080, 504)
        # Fresh ridge10: another full metre changes the court exclusion too.
        self.assertEqual(sliced_above(F(10)) + 288, 1152)

    def test_overview_transit_and_changed_large_exhibit(self):
        self.assertGreater(span(4, 2), 60)
        self.assertLess(span(4, 3.6), 60)
        for eye in (1.2, 1.6):
            self.assertLess(math.degrees(math.atan((3 - eye) / 3.6)), 30)
        self.assertAlmostEqual(span(1.2, 2), 33.39848846798724)
        hall = (6.2, 2, 17.8, 11.8)
        original_portal = (17.8, 3.2, 18, 6.8)
        apron = (18, 3, 24, 7)
        transit = sweep((21, 5), (12, 5), 5.2, 3.2)
        self.assertTrue(covered(transit, [hall, original_portal, apron]))
        self.assertLess(3.4, 3.8)
        self.assertTrue(intersects(transit, (16, 2, 17.5, 11.5)))  # Close H first.
        changed = sweep((21, 4.4), (12, 4.4), 5.2, 4.3)
        self.assertFalse(covered(changed, [hall, original_portal, apron]))
        self.assertGreater(4.2, 3.8)
        new_portal, new_apron = (17.8, 2.1, 18, 6.7), (18, 2, 24, 7)
        self.assertTrue(covered(changed, [hall, new_portal, new_apron]))
        self.assertFalse(intersects(changed, (0, 0, 18, 2)))
        self.assertEqual(area(new_apron) - area(apron), 6)
        self.assertLess(4.2, 4.5)
        self.assertLess(4.5 + .4, 5.5)
        new_face = 4.4 + 3.1 / 2
        self.assertGreater(math.degrees(math.atan((4 - 1.2) / (9.6 - new_face))), 30)
        self.assertLess(math.degrees(math.atan((4 - 1.2) / (10.85 - new_face))), 30)
        self.assertLess(span(4, 10.85 - new_face), 60)
        self.assertTrue(covered((11.5, 10.35, 12.5, 11.35), [hall]))
        # Fresh height-only load: room ceiling alone still cannot pass the portal.
        self.assertGreater(5.1, 4.5)

    def test_public_connections_and_once_only_outdoor_land(self):
        spine = (.2, .2, 17.8, 2)
        entrance = (8.2, 0, 9.8, .2)
        approach = (8, -8, 10, 0)
        outdoor_band = (9, -2.8, 15, -1.2)
        replica = (11, -6, 14, -3)
        g_door, g_path = (2.4, 2, 3.6, 2.2), (2.4, 2.2, 3.6, 9.7)
        g_stop = (2.5, 9.2, 3.5, 10.2)
        east = (16, 2, 17.5, 11.5)
        for stop_y in (9.6, 10.85):
            north = (11.5, stop_y - .5, 17.5, stop_y + .5)
            paths = [[(9, -7), (9, 1), (3, 1), (3, 9.7)],
                     [(9, -7), (9, 1), (16.75, 1), (16.75, stop_y), (12, stop_y)],
                     [(9, -7), (9, -2), (12.5, -2)]]
            free = [spine, entrance, approach, outdoor_band, g_door, g_path, g_stop, east, north]
            for path in paths:
                for a, b in zip(path, path[1:]):
                    transit = sweep(a, b, 1, 1)
                    self.assertTrue(covered(transit, free))
                    self.assertFalse(intersects(transit, replica))
        self.assertAlmostEqual(area(approach) + area(outdoor_band) - 1.6 + area(replica), 33)
        self.assertFalse(intersects(replica, approach))
        self.assertFalse(intersects(replica, outdoor_band))

    def test_exposure_closed_handling_and_instantaneous_limit(self):
        self.assertEqual(exposure(400, 40), 17760)
        self.assertEqual(exposure(225, 40), 10935)
        self.assertEqual(exposure(225, 45), 12060)
        self.assertEqual(exposure(200, 45), 10960)
        self.assertGreater(45, 40)  # Shorter time cannot override a fixed instant cap.
        # Fresh closed-state leakage, rather than a copied viewing-hours change.
        self.assertGreater(exposure(225, 40, closed_lux=3), 12000)
        self.assertEqual(exposure(200, 40, closed_lux=3), 11960)


if __name__ == '__main__':
    unittest.main()
