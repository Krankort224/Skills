#!/usr/bin/env python3
"""Preliminary architectural comparisons; see ../references/calculators.md.

Revised bounded subsets of Abhinav Bhardwaj's MIT-licensed calculators.
Copyright (c) 2026 Abhinav Bhardwaj; see ../THIRD_PARTY_NOTICES.md.
No code compliance or engineering certification is performed.
"""
import argparse
import json
import math
import sys


def fields(data, required):
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    missing = set(required) - data.keys()
    extra = data.keys() - set(required)
    if missing or extra:
        raise ValueError(f"schema mismatch: missing={sorted(missing)}, unknown={sorted(extra)}")


def number(value, name, minimum=0, maximum=None, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a JSON number in the named units")
    try:
        value = float(value)
    except OverflowError:
        raise ValueError(f"{name} is outside finite numeric range") from None
    if not math.isfinite(value) or value < minimum or (positive and value <= minimum):
        raise ValueError(f"{name} must be finite and {'greater than' if positive else 'at least'} {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name} must be at most {maximum}")
    return value


def area(data):
    fields(data, ("site_area_m2", "gross_floor_area_m2", "footprint_area_m2", "net_usable_area_m2"))
    site = number(data["site_area_m2"], "site_area_m2", positive=True)
    gross = number(data["gross_floor_area_m2"], "gross_floor_area_m2")
    footprint = number(data["footprint_area_m2"], "footprint_area_m2", maximum=min(site, gross))
    net = number(data["net_usable_area_m2"], "net_usable_area_m2", maximum=gross)
    if gross > 0 and footprint == 0:
        raise ValueError("positive enclosed gross floor area requires positive enclosed footprint")
    return {"floor_area_ratio": gross / site,
            "site_coverage_pct": footprint / site * 100,
            "net_to_gross_ratio": net / gross if gross else None}


def solar(data):
    fields(data, ("latitude_deg", "declination_deg", "solar_time_hours", "object_height_m"))
    lat = number(data["latitude_deg"], "latitude_deg", -90, 90)
    dec = number(data["declination_deg"], "declination_deg", -23.5, 23.5)
    hour = number(data["solar_time_hours"], "solar_time_hours", 0, 24)
    if hour == 24:
        raise ValueError("solar_time_hours must be less than 24")
    height = number(data["object_height_m"], "object_height_m", positive=True)
    phi, delta, angle = map(math.radians, (lat, dec, 15 * (hour - 12)))
    up = math.sin(phi) * math.sin(delta) + math.cos(phi) * math.cos(delta) * math.cos(angle)
    east = -math.cos(delta) * math.sin(angle)
    north = math.cos(phi) * math.sin(delta) - math.sin(phi) * math.cos(delta) * math.cos(angle)
    altitude = math.degrees(math.asin(max(-1.0, min(1.0, up))))
    horizontal = math.hypot(east, north)
    azimuth = math.degrees(math.atan2(east, north)) % 360 if horizontal > 1e-12 and abs(lat) < 90 else None
    sun_up = up > 1e-12
    return {"altitude_deg": altitude, "azimuth_deg_clockwise_from_north": azimuth,
            "sun_above_geometric_horizon": sun_up,
            "shadow_length_m": height * horizontal / up if sun_up else None,
            "shadow_azimuth_deg_clockwise_from_north": (azimuth + 180) % 360 if sun_up and azimuth is not None else None}


def daylight(data):
    keys = ("room_width_m", "room_depth_m", "room_height_m", "window_width_m", "window_height_m", "window_sill_m")
    fields(data, keys)
    w, d, h, ww, wh = [number(data[k], k, positive=True) for k in keys[:5]]
    sill = number(data["window_sill_m"], "window_sill_m")
    if ww > w or sill + wh > h:
        raise ValueError("single rectangular window must fit the width-facing room wall")
    floor = w * d
    window = ww * wh
    surfaces = 2 * (floor + w * h + d * h)
    return {"floor_area_m2": floor, "window_area_m2": window,
            "room_total_internal_surface_area_m2": surfaces,
            "window_to_floor_ratio_pct": window / floor * 100,
            "window_to_host_wall_ratio_pct": window / (w * h) * 100}


def uvalue(data):
    fields(data, ("layers", "rsi_m2K_W", "rse_m2K_W"))
    layers = data["layers"]
    if not isinstance(layers, list) or not layers:
        raise ValueError("layers must be a nonempty array")
    rsi = number(data["rsi_m2K_W"], "rsi_m2K_W")
    rse = number(data["rse_m2K_W"], "rse_m2K_W")
    resistances = []
    thicknesses = []
    for i, layer in enumerate(layers):
        fields(layer, ("name", "thickness_m", "conductivity_W_mK"))
        if not isinstance(layer["name"], str) or not layer["name"].strip():
            raise ValueError(f"layer {i}: name must be a nonempty string")
        thickness = number(layer["thickness_m"], f"layer {i} thickness_m", positive=True)
        conductivity = number(layer["conductivity_W_mK"], f"layer {i} conductivity_W_mK", positive=True)
        thicknesses.append(thickness)
        resistances.append(thickness / conductivity)
    total = math.fsum([rsi, *resistances, rse])
    if total <= 0:
        raise ValueError("total resistance is below numeric range")
    return {"layer_resistances_m2K_W": resistances, "total_resistance_m2K_W": total,
            "u_value_W_m2K": 1 / total, "total_thickness_m": math.fsum(thicknesses)}


CALCULATORS = {"area": area, "solar": solar, "daylight": daylight, "uvalue": uvalue}


def calculate(command, data):
    try:
        result = CALCULATORS[command](data)
        # Fail closed if finite inputs overflow intermediate/output arithmetic.
        json.dumps(result, allow_nan=False)
        return result
    except (OverflowError, ZeroDivisionError):
        raise ValueError("calculation exceeds supported numeric range") from None


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Preliminary comparisons; JSON object on stdin; explicit SI units; no compliance checks.")
    parser.add_argument("command", choices=CALCULATORS)
    args = parser.parse_args(argv)
    try:
        data = json.load(sys.stdin, object_pairs_hook=unique_object,
                         parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"nonfinite JSON token: {value}")))
        result = calculate(args.command, data)
        print(json.dumps({"calculator": args.command, "preliminary": True, "inputs": data, "results": result}, allow_nan=False, indent=2))
        return 0
    except (ValueError, TypeError, RecursionError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
