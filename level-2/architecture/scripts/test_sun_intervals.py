"""Bounded verification of the sun-interval method; no runtime solar engine."""
import itertools
import math
import unittest

from calculators import calculate


def coefficients(latitude, declination):
    phi, delta = map(math.radians, (latitude, declination))
    return ((-math.cos(delta), 0, 0),
            (0, -math.sin(phi) * math.cos(delta), math.cos(phi) * math.sin(delta)),
            (0, math.cos(phi) * math.cos(delta), math.sin(phi) * math.sin(delta)))


def value(coeff, hour):
    angle = math.radians(15 * (hour - 12))
    return coeff[0] * math.sin(angle) + coeff[1] * math.cos(angle) + coeff[2]


def local(point, coeffs, box):
    """box = (local bounds, horizontal origin, yaw degrees)."""
    bounds, origin, yaw = box
    cosine, sine = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
    x, y = point[0] - origin[0], point[1] - origin[1]
    receiver = (cosine * x + sine * y, -sine * x + cosine * y, point[2])
    directions = (tuple(cosine * e + sine * n for e, n in zip(coeffs[0], coeffs[1])),
                  tuple(-sine * e + cosine * n for e, n in zip(coeffs[0], coeffs[1])),
                  coeffs[2])
    return bounds, receiver, directions


def ray_hit(point, direction, bounds):
    near, far = 0.0, math.inf
    for p, s, (low, high) in zip(point, direction, bounds):
        if s == 0:
            if not low <= p <= high:
                return False
            continue
        first, second = sorted(((low - p) / s, (high - p) / s))
        near, far = max(near, first), min(far, second)
        if near > far:
            return False
    return far > 0


def roots(coeff, start, end):
    a, b, c = coeff
    radius = math.hypot(a, b)
    if radius == 0 or abs(c) > radius:
        return []  # Identity has no isolated event; a nonzero constant has no root.
    alpha, phase = math.asin(-c / radius), math.atan2(b, a)
    candidates = (12 + math.degrees(h - phase + 2 * math.pi * k) / 15
                  for h in (alpha, math.pi - alpha) for k in range(-2, 3))
    return [t for t in candidates if start < t < end]


def blocked_intervals(point, boxes, latitude, declination, window, normal=None):
    """Exact event partition in the declared constant-declination box model.

    Verification inputs below are finite, positive boxes with receiver outside;
    this is not a validated public input interface or an astronomical ephemeris.
    Returned open-cell intervals omit zero-duration boundary contacts.
    """
    coeffs = coefficients(latitude, declination)
    face = (tuple(sum(n * c[i] for n, c in zip(normal, coeffs)) for i in range(3))
            if normal is not None else None)
    events = [*window, *roots(coeffs[2], *window)]
    if face is not None:
        events += roots(face, *window)
    frames = [local(point, coeffs, box) for box in boxes]
    for bounds, receiver, directions in frames:
        for direction in directions:
            events += roots(direction, *window)
        for i, j in itertools.combinations(range(3), 2):
            for vi, vj in itertools.product(bounds[i], bounds[j]):
                distances = vi - receiver[i], vj - receiver[j]
                equation = tuple(distances[0] * sj - distances[1] * si
                                 for si, sj in zip(directions[i], directions[j]))
                events += roots(equation, *window)
    events = sorted(set(events))
    result = []
    for left, right in zip(events, events[1:]):
        hour = (left + right) / 2
        eligible = value(coeffs[2], hour) > 0 and (face is None or value(face, hour) > 0)
        blocked = eligible and any(ray_hit(p, tuple(value(c, hour) for c in directions), bounds)
                                   for bounds, p, directions in frames)
        if blocked:
            if result and result[-1][1] == left:
                result[-1] = (result[-1][0], right)
            else:
                result.append((left, right))
    return result


A = (((4, 8), (-6, -4), (0, 9)), (0, 0), 0)
B = (((2, 6), (-8, -6), (0, 11)), (0, 0), 0)


class SunIntervalTests(unittest.TestCase):
    def test_single_body_and_existing_solar_contract(self):
        expected = [12 - math.degrees(math.atan(q / math.sqrt(2))) / 15 for q in (2, 2 / 3)]
        actual = blocked_intervals((0, 0, 1), [A], 45, 0, (6, 18))
        self.assertEqual(len(actual), 1)
        for found, wanted in zip(actual[0], expected):
            self.assertAlmostEqual(found, wanted, places=10)
        for hour in (7, 9, 12, 15, 17):
            east, north, up = [value(c, hour) for c in coefficients(45, 0)]
            result = calculate('solar', {'latitude_deg': 45, 'declination_deg': 0,
                                        'solar_time_hours': hour, 'object_height_m': 8})
            self.assertAlmostEqual(math.degrees(math.asin(up)), result['altitude_deg'])
            self.assertAlmostEqual(math.degrees(math.atan2(east, north)) % 360,
                                   result['azimuth_deg_clockwise_from_north'])
            self.assertAlmostEqual(8 * math.hypot(east, north) / up, result['shadow_length_m'])

    def test_union_height_position_and_near_grid_transition(self):
        one = blocked_intervals((0, 0, 1), [A], 45, 0, (6, 18))[0]
        two = blocked_intervals((0, 0, 1), [B], 45, 0, (6, 18))[0]
        combined = blocked_intervals((0, 0, 1), [A, B], 45, 0, (6, 18))
        self.assertEqual(combined, [(one[0], two[1])])
        summed = one[1] - one[0] + two[1] - two[0]
        overlap = one[1] - two[0]
        self.assertAlmostEqual(summed - overlap, combined[0][1] - combined[0][0])
        self.assertEqual(blocked_intervals((0, 0, 6), [A, B], 45, 0, (6, 18)), [])
        west = (((-6, -2), (-8, -6), (0, 11)), (0, 0), 0)
        moved = blocked_intervals((0, 0, 1), [A, west], 45, 0, (6, 18))
        self.assertEqual(len(moved), 2)
        self.assertAlmostEqual(moved[1][0], 24 - two[1])
        self.assertAlmostEqual(moved[1][1], 24 - two[0])
        lower = (((2, 6), (-8, -6), (0, 8)), (0, 0), 0)
        changed = blocked_intervals((0, 0, 1), [A, lower], 45, 0, (6, 18))
        self.assertAlmostEqual(changed[0][1], 12 - math.degrees(math.atan((2 / 7) / math.sqrt(2))) / 15)
        self.assertLess(changed[0][1], combined[0][1])
        self.assertTrue(11.25 < two[1] < 11 + 20 / 60)
        self.assertLess((11 + 20 / 60 - two[1]) * 3600, 7)
        directions = coefficients(45, 0)
        self.assertTrue(ray_hit((0, 0, 1), tuple(value(c, two[1] - 1 / 3600)
                                                for c in directions), B[0]))
        self.assertFalse(ray_hit((0, 0, 1), tuple(value(c, two[1] + 1 / 3600)
                                                 for c in directions), B[0]))

    def test_parallel_tangent_and_face_condition(self):
        bounds = ((2, 4), (-1, 1), (0, 3))
        self.assertTrue(ray_hit((0, 0, 1), (1, 0, 0), bounds))
        self.assertFalse(ray_hit((0, 2, 1), (1, 0, 0), bounds))
        self.assertFalse(ray_hit((0, 0, 4), (1, 0, 0), bounds))
        self.assertTrue(ray_hit((0, 1, 1), (1, 0, 0), bounds))
        equator = (bounds, (0, 0), 0)
        self.assertEqual(blocked_intervals((0, 0, 1), [equator], 0, 0, (6, 18)), [(6, 9.0)])
        zenith = calculate('solar', {'latitude_deg': 0, 'declination_deg': 0,
                                    'solar_time_hours': 12, 'object_height_m': 8})
        self.assertIsNone(zenith['azimuth_deg_clockwise_from_north'])
        self.assertFalse(ray_hit((0, 0, 1), (0, 0, 1), bounds))
        self.assertEqual(set(roots((1, 0, -1), 0, 24)), {18.0})
        self.assertEqual(roots((0, 0, 0), 0, 24), [])
        self.assertEqual(blocked_intervals((0, 0, 1), [A, B], 45, 0, (6, 18), (0, 1, 0)), [])
        self.assertEqual(blocked_intervals((0, 0, 1), [A, B], 45, 0, (6, 18), (0, -1, 0)),
                         blocked_intervals((0, 0, 1), [A, B], 45, 0, (6, 18)))

    def test_changed_rotated_boxes_against_projected_silhouettes(self):
        # Independent construction: project the part of each solid above the
        # receiver onto its horizontal plane, form its convex hull, test the
        # receiver in that silhouette. No ray/slab or event equations reused.
        def cross(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        def hull(points):
            points = sorted(set(points))
            chains = []
            for ordered in (points, points[::-1]):
                chain = []
                for p in ordered:
                    while len(chain) > 1 and cross(chain[-2], chain[-1], p) <= 0:
                        chain.pop()
                    chain.append(p)
                chains += chain[:-1]
            return chains

        point = (0, 0, 1.5)
        boxes = [(((-3, 3), (-2, 2), (0, 12)), (6, -10), 25),
                 (((-2, 2), (-4, 4), (0, 9)), (-6, -9), -20),
                 (((0, 3), (0, 5), (0, 6)), (-2, -15), 40)]
        intervals = blocked_intervals(point, boxes, 37, -8, (7, 17))
        self.assertGreater(len(intervals), 1)
        coeffs = coefficients(37, -8)
        for step in range(1001):
            hour = 7 + step / 100
            sun = [value(c, hour) for c in coeffs]
            silhouettes = []
            for bounds, origin, yaw in boxes:
                cosine, sine = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
                projected = []
                for x, y, z in itertools.product(bounds[0], bounds[1],
                                                 (max(point[2], bounds[2][0]), bounds[2][1])):
                    east = origin[0] + x * cosine - y * sine
                    north = origin[1] + x * sine + y * cosine
                    projected.append((east - (z - point[2]) * sun[0] / sun[2],
                                      north - (z - point[2]) * sun[1] / sun[2]))
                silhouettes.append(hull(projected))
            shadow = any(all(cross(a, b, point) >= -1e-9
                             for a, b in zip(poly, poly[1:] + poly[:1]))
                         for poly in silhouettes)
            partition = any(left < hour < right for left, right in intervals)
            self.assertEqual(shadow, partition, (hour, intervals))


if __name__ == '__main__':
    unittest.main()
