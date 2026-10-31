"""Independent analytic cases and invalid/boundary checks; stdlib unittest."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

from calculators import calculate


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.area = dict(site_area_m2=1000, gross_floor_area_m2=1500,
                         footprint_area_m2=300, net_usable_area_m2=1200)
        self.sun = dict(latitude_deg=45, declination_deg=0, solar_time_hours=12, object_height_m=10)
        self.room = dict(room_width_m=4, room_depth_m=5, room_height_m=3,
                         window_width_m=2, window_height_m=1.5, window_sill_m=1)
        self.wall = dict(layers=[dict(name="test", thickness_m=0.2, conductivity_W_mK=0.1)],
                         rsi_m2K_W=0.1, rse_m2K_W=0.4)

    def test_area_known_answer(self):
        r = calculate("area", self.area)
        self.assertEqual(r, dict(floor_area_ratio=1.5, site_coverage_pct=30, net_to_gross_ratio=0.8))

    def test_empty_area_boundary(self):
        self.area.update(gross_floor_area_m2=0, footprint_area_m2=0, net_usable_area_m2=0)
        self.assertIsNone(calculate("area", self.area)["net_to_gross_ratio"])

    def test_impossible_area(self):
        for key, value in [("footprint_area_m2", 1001), ("net_usable_area_m2", 1501), ("footprint_area_m2", 0)]:
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                calculate("area", {**self.area, key: value})

    def test_equinox_noon_shadow(self):
        r = calculate("solar", self.sun)
        self.assertAlmostEqual(r["altitude_deg"], 45)
        self.assertAlmostEqual(r["azimuth_deg_clockwise_from_north"], 180)
        self.assertAlmostEqual(r["shadow_length_m"], 10)
        self.assertAlmostEqual(r["shadow_azimuth_deg_clockwise_from_north"], 0)

    def test_east_west_quadrants(self):
        for hour, azimuth in [(9, 90), (15, 270)]:
            r = calculate("solar", {**self.sun, "latitude_deg": 0, "solar_time_hours": hour})
            self.assertAlmostEqual(r["altitude_deg"], 45)
            self.assertAlmostEqual(r["azimuth_deg_clockwise_from_north"], azimuth)

    def test_southern_noon(self):
        r = calculate("solar", {**self.sun, "latitude_deg": -45})
        self.assertAlmostEqual(r["azimuth_deg_clockwise_from_north"], 0)

    def test_zenith_horizon_and_polar_night(self):
        zenith = calculate("solar", {**self.sun, "latitude_deg": 0})
        self.assertAlmostEqual(zenith["altitude_deg"], 90)
        self.assertIsNone(zenith["azimuth_deg_clockwise_from_north"])
        self.assertAlmostEqual(zenith["shadow_length_m"], 0)
        for lat, dec, hour in [(0, 0, 6), (90, -23, 12)]:
            r = calculate("solar", {**self.sun, "latitude_deg": lat, "declination_deg": dec, "solar_time_hours": hour})
            self.assertFalse(r["sun_above_geometric_horizon"])
            self.assertIsNone(r["shadow_length_m"])

    def test_solar_bounds(self):
        for key, value in [("latitude_deg", 91), ("declination_deg", 24), ("solar_time_hours", 24), ("solar_time_hours", -1), ("object_height_m", 0)]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                calculate("solar", {**self.sun, key: value})

    def test_daylight_geometry(self):
        r = calculate("daylight", self.room)
        self.assertEqual(r["floor_area_m2"], 20)
        self.assertEqual(r["window_area_m2"], 3)
        self.assertEqual(r["room_total_internal_surface_area_m2"], 94)
        self.assertEqual(r["window_to_floor_ratio_pct"], 15)
        self.assertEqual(r["window_to_host_wall_ratio_pct"], 25)

    def test_window_fit(self):
        for key, value in [("window_width_m", 4.1), ("window_sill_m", 2), ("room_height_m", 0)]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                calculate("daylight", {**self.room, key: value})
        calculate("daylight", {**self.room, "window_width_m": 4, "window_height_m": 3, "window_sill_m": 0})

    def test_daylight_decimal_fit_and_oversize(self):
        room = {**self.room, "room_height_m": 2.4, "window_height_m": 1.6, "window_sill_m": 0.8}
        result = calculate("daylight", room)
        self.assertEqual(result["floor_area_m2"], 20)
        self.assertAlmostEqual(result["window_area_m2"], 3.2)
        self.assertAlmostEqual(result["room_total_internal_surface_area_m2"], 83.2)
        self.assertAlmostEqual(result["window_to_floor_ratio_pct"], 16)
        self.assertAlmostEqual(result["window_to_host_wall_ratio_pct"], 100 / 3)
        for height in (1.601, 1.600000000001):
            with self.subTest(height=height), self.assertRaises(ValueError):
                calculate("daylight", {**room, "window_height_m": height})

    def test_series_resistance_known_answer(self):
        r = calculate("uvalue", self.wall)
        self.assertEqual(r["layer_resistances_m2K_W"], [2])
        self.assertEqual(r["total_resistance_m2K_W"], 2.5)
        self.assertEqual(r["u_value_W_m2K"], 0.4)

    def test_multiple_layers_and_zero_surface_resistance(self):
        wall = {**self.wall, "layers": self.wall["layers"] * 2, "rsi_m2K_W": 0, "rse_m2K_W": 0}
        self.assertEqual(calculate("uvalue", wall)["u_value_W_m2K"], 0.25)

    def test_invalid_wall(self):
        for layers in [[], [None], [dict(name="x", thickness_m=0.1, conductivity_W_mK=0)],
                       [dict(name="", thickness_m=0.1, conductivity_W_mK=1)]]:
            with self.subTest(layers=layers), self.assertRaises(ValueError):
                calculate("uvalue", {**self.wall, "layers": layers})
        with self.assertRaises(ValueError):
            calculate("uvalue", {**self.wall, "rsi_m2K_W": -1})

    def test_schema_types_and_nonfinite(self):
        for value in [float("nan"), float("inf"), float("-inf"), True, "1000", None, -1, 0]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate("area", {**self.area, "site_area_m2": value})
        for data in [[], {}, {**self.area, "units": "ft2"}]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                calculate("area", data)

    def test_overflow_failure(self):
        with self.assertRaises(ValueError):
            calculate("daylight", {key: 1e300 if "sill" not in key else 0 for key in self.room})

    def run_cli(self, command, raw):
        return subprocess.run([sys.executable, str(Path(__file__).with_name("calculators.py")), command],
                              input=raw, text=True, capture_output=True, check=False)

    def test_cli_success(self):
        result = self.run_cli("area", json.dumps(self.area))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["preliminary"])
        self.assertEqual(json.loads(result.stdout)["inputs"], self.area)

    def test_cli_daylight_decimal_fit(self):
        room = {**self.room, "room_height_m": 2.4, "window_height_m": 1.6, "window_sill_m": 0.8}
        result = self.run_cli("daylight", json.dumps(room))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertAlmostEqual(json.loads(result.stdout)["results"]["window_to_host_wall_ratio_pct"], 100 / 3)

    def test_cli_bad_json_duplicates_and_nonfinite(self):
        for raw in ["{", "[]", '{"site_area_m2":1,"site_area_m2":2}', json.dumps({**self.area, "site_area_m2": float("nan")}),
                    json.dumps({**self.area, "site_area_m2": 1e309})]:
            with self.subTest(raw=raw):
                result = self.run_cli("area", raw)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("error", json.loads(result.stderr))


if __name__ == "__main__":
    unittest.main()
