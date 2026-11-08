"""Independent bounded checks of site-method prose, not a vehicle/GIS engine."""
import math
import unittest


def rectangle(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]


def point_segment_distance(point, start, end):
    dx, dy = end[0] - start[0], end[1] - start[1]
    fraction = max(0, min(1, ((point[0] - start[0]) * dx +
                              (point[1] - start[1]) * dy) / (dx * dx + dy * dy)))
    return math.hypot(point[0] - start[0] - fraction * dx,
                      point[1] - start[1] - fraction * dy)


def polygon_distance(first, second):
    """Convex SAT intersection, otherwise vertex-to-edge distance."""
    separated = False
    for polygon in (first, second):
        for start, end in zip(polygon, polygon[1:] + polygon[:1]):
            nx, ny = end[1] - start[1], start[0] - end[0]
            left = [x * nx + y * ny for x, y in first]
            right = [x * nx + y * ny for x, y in second]
            separated |= max(left) < min(right) or max(right) < min(left)
    if not separated:
        return 0.0
    return min(point_segment_distance(point, start, end)
               for one, two in ((first, second), (second, first))
               for point in one
               for start, end in zip(two, two[1:] + two[:1]))


class SiteMethodsTests(unittest.TestCase):
    def test_parking_arc_against_occupied_neighbours(self):
        # Direct corner coordinates; independent of the prose's radial maximum.
        samples = 2000
        poses = []
        for step in range(samples + 1):
            angle = step * math.pi / (2 * samples)
            axle = (4 * math.sin(angle), 7.8 + 4 * (1 - math.cos(angle)))
            poses.append([(axle[0] + u * math.cos(angle) - v * math.sin(angle),
                           axle[1] + u * math.sin(angle) + v * math.cos(angle))
                          for u, v in [(-1.1, -.9), (3.5, -.9),
                                       (3.5, .9), (-1.1, .9)]])
        error = (4 + math.hypot(3.5, .9)) * math.pi / (2 * samples)
        minimums = []
        for pitch in (2.5, 3.3):
            obstacles = [rectangle(4 + k * pitch - .9, 11.5,
                                   4 + k * pitch + .9, 16.1)
                         for k in range(-3, 4) if k]
            obstacles += [rectangle(4 + k * pitch - .9, .3,
                                    4 + k * pitch + .9, 4.9)
                          for k in range(-3, 4)]
            minimums.append(min(polygon_distance(pose, obstacle)
                                for pose in poses for obstacle in obstacles))
        self.assertEqual(minimums[0], 0)
        self.assertGreater(minimums[1] - error, .20)
        self.assertAlmostEqual(minimums[1], .37837245, places=7)
        # Column blocks an otherwise straight aisle movement.
        self.assertEqual(polygon_distance(rectangle(8, 6.9, 12.6, 8.7),
                                          rectangle(9, 7.6, 9.4, 8)), 0)
        # Final northbound translation stays between the same neighbour cars.
        self.assertAlmostEqual(12.6 - 1.1 - 11.2, .30)
        self.assertAlmostEqual(16.4 - (12.6 + 3.5), .30)
        # Repeating the corrected manoeuvre at each bay stays inside end aprons.
        for bay in range(10):
            target = 6 + 1.65 + bay * 3.3
            for pose in poses:
                for x, y in pose:
                    self.assertGreater(x + target - 4, .20)
                    self.assertLess(x + target - 4, 45 - .20)
                    self.assertGreater(y, .20)
                    self.assertLess(y, 16.4 - .20)

    def test_changed_vehicle_radial_screen_and_steering(self):
        # Different values from the authored changed-van example. Check circle
        # distances directly from transformed corners, including a correction.
        outer = []
        for radius in (4.6, 4.2):
            self.assertLessEqual(math.degrees(math.atan(2.8 / radius)), 34)
            distances = []
            for step in range(361):
                angle = math.radians(step)
                axle = (radius * math.sin(angle), radius * (1 - math.cos(angle)))
                for u, v in [(-1, -.95), (3.9, -.95), (3.9, .95), (-1, .95)]:
                    x = axle[0] + u * math.cos(angle) - v * math.sin(angle)
                    y = axle[1] + u * math.sin(angle) + v * math.cos(angle)
                    distances.append(math.hypot(x, y - radius))
            outer.append(max(distances))
            self.assertGreaterEqual(radius - .95 - .10, 3.0)
        self.assertGreater(outer[0] + .10, 6.6)
        self.assertLess(outer[1] + .10, 6.6)
        self.assertAlmostEqual(outer[1], math.hypot(3.9, 5.15))
        self.assertGreater(3.5 / math.tan(math.radians(35)), 4)
        self.assertGreater(3.5 + 1 + 1.2, 5.2)

    def test_facility_cut_and_reassignment(self):
        # Enumerate individual-seat reservations rather than reuse an optimizer.
        self.assertEqual(100 - 20 + 120 - 20, 70 + 60 + 50)
        before = [b for b in [0] if 70 + b <= 80 and 60 - b + 50 <= 100]
        after = [b for b in range(61) if 70 + b <= 80 and 60 - b + 50 <= 100]
        self.assertEqual(before, [])
        self.assertEqual(after, [10])
        self.assertEqual(650 - 230 + 60, 480)
        self.assertEqual([b for b in (0, 20) if 25 + b <= 30 and
                          20 - b + 15 <= 30], [])  # Whole preschool group fails.
        # New instance: first group is flexible; nearest-first fills facility 1
        # and strands the group of 37. Six reassignments recover all 120 seats.
        feasible = [x for x in range(49) if x + 37 <= 55 and 48 - x + 35 <= 70]
        self.assertEqual(feasible, list(range(13, 19)))
        self.assertGreaterEqual(55 + 70, 48 + 37 + 35)
        self.assertEqual([x for x in [48] if x + 37 <= 55 and 35 <= 70], [])
        # Closing the flexible group's second route leaves a certified cut.
        self.assertEqual(48 + 37 - 55, 30)
        self.assertEqual(math.ceil(500 * .10), 50)
        self.assertEqual(math.ceil(500 / 30), 17)

    def test_module_parcels_and_once_only_land(self):
        angle = math.radians(60)
        width, length, available = 2.6, 5.4, 27
        pitch = width / math.sin(angle)
        depth = length * math.sin(angle) + width * math.cos(angle)
        # Count by constructing every bay's four actual corners, not by using
        # the closed-form count in the method. The ninth bay exceeds 27 m.
        spans = []
        for count in (8, 9):
            corners = [(i * pitch + u * math.cos(angle) - v * math.sin(angle),
                        u * math.sin(angle) + v * math.cos(angle))
                       for i in range(count)
                       for u, v in [(0, 0), (length, 0),
                                    (length, width), (0, width)]]
            spans.append(max(x for x, y in corners) - min(x for x, y in corners))
            self.assertAlmostEqual(max(y for x, y in corners), depth)
        self.assertLessEqual(spans[0], available)
        self.assertGreater(spans[1], available)
        self.assertEqual(math.floor(26.4 / 2.5), 10)
        self.assertEqual(math.floor(26.4 / 3.3), 8)
        self.assertAlmostEqual(45 * 16.4 - 38.4 * 16.4, 108.24)
        self.assertAlmostEqual(2200 - 738 - 81 - 60, 1321)
        school = [rectangle(0, 0, 60, 20), rectangle(0, 20, 65, 60),
                  rectangle(60, 0, 80, 20), rectangle(65, 20, 80, 40),
                  rectangle(65, 40, 80, 60)]
        area = lambda p: (p[1][0] - p[0][0]) * (p[2][1] - p[1][1])
        self.assertEqual(sum(map(area, school)), 4800)
        for i, first in enumerate(school):
            for second in school[i + 1:]:
                overlap_x = min(first[1][0], second[1][0]) - max(first[0][0], second[0][0])
                overlap_y = min(first[2][1], second[2][1]) - max(first[0][1], second[0][1])
                self.assertLessEqual(min(overlap_x, overlap_y), 0)
        self.assertGreater(min(65, 40), 30)  # Equal-area narrow parcel fails.
        self.assertEqual(9600 + 2400 + 4800 + 1600 + 600 + 1000, 20000)
        self.assertEqual(9600 + 2400 + 4800 + 1720 + 600 + 880, 20000)


if __name__ == '__main__':
    unittest.main()
