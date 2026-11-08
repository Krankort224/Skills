# Calculator audit and supported interface

## Contents

- [Pinned sources and license](#pinned-sources-and-license)
- [Per-script decisions](#per-script-decisions)
- [Invocation and common contract](#invocation-and-common-contract)
- [Schemas, definitions and limitations](#schemas-definitions-and-limitations)
- [Verification](#verification)

These bundled tools make preliminary numeric comparisons for architectural design. Their results do not certify compliance, predict occupied-building performance or establish structural sizing; they provide numeric outputs rather than geometric models. Python 3 with the standard library is sufficient. No native daylight, thermal, structural, or solar simulation has been run.

## Pinned sources and license

All fourteen source scripts below were retrieved and inspected at these immutable revisions. Findings are static source-review findings; the upstream scripts were not executed. This table owns the per-calculator adoption decisions.

- **A**: [Abhinavbwj/Skills-Architects](../sources/upstream-packs.md#pack-a), pin `30a0845dddcaebd765fc396059573d02e99c5b63`. Script prefix `skills/architect-calculator/scripts/`.
- **B**: [Abhinavbwj/Claude-skills-for-Computational-Designers](../sources/upstream-packs.md#pack-c), pin `7a090c9ddc92e441b1419910673edbcfa7a962ed`. Script prefix `skills/cd-calculator/scripts/`.

Both [A LICENSE](../sources/upstream-packs.md#a-001) and [B LICENSE](../sources/upstream-packs.md#c-001) contain the MIT License and `Copyright (c) 2026 Abhinav Bhardwaj`. Revised subsets retain attribution in the script; redistribution must include the full copyright and permission notice in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). Do not replace the notices with only a hyperlink.

## Per-script decisions

Each filename combines with its pack's exact prefix above to identify the original path. Function names below identify inspected computational or validation entry points, rather than every formatting helper.

| Pack / original script | Original functions | Actual findings | Decision and rationale |
| --- | --- | --- | --- |
| A `area_calculator.py` | `validate_inputs`, `calculate` | GFA = site × FAR and net area = GFA × ratio are straightforward. `site_coverage_pct = (gfa / far) / site * 100` collapses to 100% for all valid inputs: footprint is absent. Residential unit, population, and parking defaults add unverified program assumptions. Float comparisons do not generally reject nonfinite inputs. | **Revise**: `area` compares explicit, consistently measured site/GFA/enclosed footprint/net usable area; compute FAR, real footprint coverage, and net-to-gross. Drop residential and parking assumptions and ambiguous "net gross area" label. |
| A `cost_calculator.py` | `validate_inputs`, `calculate` | `COST_DATABASE` claims 2025 North American USD/m²; region multipliers span continents without locality, date, or evidence. Quality controls fees and contingency as fixed percentages; output calls subtotal "total development cost" despite missing land/taxes and scope. | **Reference-only**: area × a documented current local rate is useful arithmetic, but source rates and scope are unsuitable for an executable architectural comparison default. No cost command. |
| A `daylight_calculator.py` | `validate_inputs`, `calculate` | Rectangular room/window areas are transparent. Claimed BRE DF uses a normalized angle derived from room depth and window head, not measured external sky obstruction; `window_mid` is unused. Assessment hardcodes 1/2/5% bands. This does not establish real daylight performance. | **Revise**: `daylight` retains window/floor/host-wall geometric ratios and dimensional fit validation only. Drop claimed DF, transmittance/reflectance defaults, sky inference, and performance labels. |
| A `egress_calculator.py` | `validate_inputs`, `calculate` | Fixed IBC occupancy/travel tables, width factors and a blanket sprinkler multiplier embed jurisdiction assumptions. `max(1, num_exits)` cannot reduce the initialized two exits to one, despite the single-exit comment. Net/gross flag in occupancy data is not used. | **Exclude**: a life-safety/compliance engine needs the actual adopted edition, occupancy/use, exceptions and qualified review. Never ship this table as a generic compliance check. |
| A `energy_calculator.py` | `validate_inputs`, `calculate` | Fixed 3 m ceiling height; heating/cooling season hours inferred from degree-days; fixed 15 W/m² solar gain; labels heating/cooling EUI ≤15 as Passive House compliance. No weather, schedule or system simulation. | **Exclude**: unsupported energy predictions and certification flags cannot be justified by this workflow. Use an appropriate validated tool and declared climate/schedule. |
| A `structural_load_calculator.py` | `validate_inputs`, `calculate` | Occupancy load table, 1.2D+1.6L combination, assumed 35 MPa concrete and minimum 300 mm RC column dimension turn gravity sums into member sizing. No stability, lateral load, detailing, or project-specific combinations. | **Exclude**: structural sizing belongs to qualified structural analysis; no member sizes or structural default loads are imported. |
| A `uvalue_calculator.py` | `validate_layers`, `calculate_wall_uvalue`, `generate_layout`, `validate_facade`, `calculate_facade`, `draw_facade_elevation` | Homogeneous-layer series resistance is useful. Facade mode auto-positions openings, assumes psi/sill/pier limits, clamps negative opaque area to zero, and assigns generic 0.15/0.30 compliance targets. Opening heights/sills are not checked against facade height. ASCII elevation is symbolic output, not a verified visual deliverable. | **Revise**: `uvalue` retains only explicit homogeneous plane-layer resistance; requires both surface resistances and named SI properties. Exclude facade authoring, bridges, default targets, structural pier claims and compliance labels. |
| B `fabrication_calculator.py` | `estimate_cnc`, `estimate_3d_print`, `interpolate_speed`, `estimate_laser` | Inventories of speeds/prices plus fixed setup times; CNC material volume assumes 6×5 mm cut; print model fixes 30% shell and unattended factor; laser material area inferred from cut length. Truthy defaults override legitimate zero inputs, e.g. infill. | **Exclude**: manufacturing estimation is out of the architectural/2D numeric scope and lacks machine/material-specific evidence. |
| B `geometry_calculator.py` | `compute_rectangle`, `compute_circle`, `compute_triangle`, `compute_i_beam`, `compute_hollow_rect`, `compute_hollow_circle`, `compute_l_shape`, `compute_t_shape`, `compute_polygon` | Primarily structural section properties in mm. Triangle `Sy = hb²/24` is labeled approximate; T perimeter expression `2b+2h+2(b-tw)` overcounts the boundary. Polygon shoelace processing does not validate a simple nonintersecting boundary. | **Reference-only**: elementary area/perimeter concepts can inform manual 2D work, but no section-property/structural package or unvalidated arbitrary-polygon engine is imported. |
| B `material_estimator.py` | `estimate_parametric`, `estimate_direct`, `compute_embodied_carbon` | Unsourced building-type concrete/steel/glass/timber rates, densities and waste factors; floors mainly derive a reported floorplate. Fixed carbon factors include negative timber storage with no lifecycle boundary or EPD. Direct mode silently supplies rebar ratio. | **Reference-only**: project-specific quantities × sourced factors can support a future estimate, but benchmarks/carbon totals are not defensible defaults. No material command. |
| B `mesh_analyzer.py` | `parse_obj_file`, `extract_edges`, `compute_face_area`, `compute_aspect_ratio`, `analyze_mesh`, `count_boundary_loops` | OBJ reader subtracts one from all face indices, rejecting legitimate negative OBJ indices later. Manifold flag only checks >2 faces per edge, missing vertex-manifold conditions. Genus formula assumes a connected orientable surface; boundary tracing stores one successor per vertex. | **Exclude**: mesh processing is outside scope; do not import topology certifications or mesh workflow. |
| B `panel_optimizer.py` | `parse_panels`, `cluster_panels`, `compute_waste`, `compute_cost_impact`, `optimize_panels` | Greedy moving centroids are order-dependent and not a global optimum. `max(fit_a, fit_b, 1)` falsely fits an oversized panel into a sheet and can yield negative waste. Centroid dimensions are rounded; neither kerf nor packing feasibility is established. | **Exclude**: manufacturing/nesting inference is outside scope and the false-fit defect makes the provided waste output unsafe to reuse. |
| B `solar_calculator.py` | `solar_declination`, `equation_of_time`, `hour_angle`, `solar_altitude`, `solar_azimuth`, `sunrise_sunset`, `shadow_length`, `compute_position`, `compute_annual_summary`, `compute_shadow_analysis`, `compute_pv_tilt` | `compute_position` treats time as solar time: longitude is echoed but unused; equation-of-time helper is unused. Azimuth's final 180° flip reverses morning/afternoon quadrants (equator, zero declination, 09:00 gives west). Zenith returns an arbitrary 180°. Radiation assumes latitude-band clearness; PV gains are heuristic cosine factors, not climate-backed optimization. | **Revise**: `solar` keeps geometric hour-angle/altitude/shadow relations, corrects azimuth with east/north components, and explicitly requires apparent solar time plus supplied declination. Return undefined azimuth/shadows as null. Drop civil-time/date conversion, sunrise predictions, radiation, and PV optimization. |
| B `structural_checker.py` | `find_suitable_section`, `parse_deflection_limit`, `check_beam`, `check_column`, `check_deflection` | Small IPE/grade database and simplified bending/shear/Euler checks produce PASS/FAIL; missing phenomena include lateral torsional buckling and member imperfection effects. Invalid deflection limit silently falls back to 250. Largest section returned when none meets required modulus. | **Exclude**: structural verification and section selection are outside scope; labels must not become architectural compliance judgments. |

## Invocation and common contract

From the skill directory:

```sh
python3 scripts/calculators.py area <<'JSON'
{"site_area_m2":1000,"gross_floor_area_m2":1500,"footprint_area_m2":300,"net_usable_area_m2":1200}
JSON
```

Only subcommands `area`, `solar`, `daylight`, `uvalue` exist. Every command reads exactly one JSON object from stdin and prints JSON to stdout. There is no network, dependency installation, file mutation, or unit conversion. The Python API is `calculate(command, data)`, returning the result object or raising `ValueError` for invalid data/numeric range. CLI output wraps it as:

```json
{"calculator":"area","preliminary":true,"inputs":{"site_area_m2":1000,"gross_floor_area_m2":1500,"footprint_area_m2":300,"net_usable_area_m2":1200},"results":{"floor_area_ratio":1.5,"site_coverage_pct":30.0,"net_to_gross_ratio":0.8}}
```

All listed fields are required, with exact spelling and named SI units. Unknown/missing fields, duplicate JSON keys, null/string/bool numeric values, NaN/Infinity, nonfinite arithmetic results, negative dimensions/resistances, impossible dimensional relationships, and overflow fail. No jurisdiction, code edition, efficiency, transmittance, household size, target or material properties are silently assumed. Invalid input/calculation yields exit 2, no stdout result and `{"error":"..."}` on stderr. Argument-parser usage errors also exit 2 using argparse's usage text. Results retain floating-point precision; round only for display with an appropriate tolerance. Very small/large numbers can exceed supported floating-point range and must be rescaled in the stated units before use.

## Schemas, definitions and limitations

### `area`

| Required input | Definition / admissible values |
| --- | --- |
| `site_area_m2` | One measured site/parcel area, >0. |
| `gross_floor_area_m2` | Sum of enclosed floor areas, measured consistently across levels; ≥0. This is an explicitly declared comparison definition, not statutory GFA. |
| `footprint_area_m2` | Union of enclosed floor plan projections onto the site, ≥0 and ≤both site and GFA; >0 for positive GFA. Exclude canopies/overhangs unless the entire comparison definition is revised outside this tool. |
| `net_usable_area_m2` | Usable portion of the stated GFA, ≥0 and ≤GFA; state separately which circulation/services/walls are excluded. |

Outputs: `floor_area_ratio = GFA/site`, `site_coverage_pct = footprint/site × 100`, `net_to_gross_ratio = net/GFA` (null for zero GFA). No conversion among statutory definitions, developable site area, land coverage, internal/external measurement conventions, or FAR exemptions occurs. Confirm the project definitions before comparing schemes. Empty site is supported with all three building areas zero. No units, population or parking quantities are inferred.

### `solar`

| Required input | Definition / admissible values |
| --- | --- |
| `latitude_deg` | Degrees north positive, −90 through +90. |
| `declination_deg` | Solar declination for the design instant, −23.5 through +23.5 degrees; obtain from a documented ephemeris. No date-to-declination approximation is hidden. |
| `solar_time_hours` | Local apparent/true solar time in decimal hours, 0 inclusive to 24 exclusive; apparent solar noon =12. **Not** civil clock time, standard time, daylight-saving time or UTC. |
| `object_height_m` | Positive vertical height above a horizontal receiving plane. |

Uses hour angle `15(time−12)` and spherical solar geometry. Output keys: `altitude_deg`, `azimuth_deg_clockwise_from_north` (north=0/east=90/south=180/west=270), `sun_above_geometric_horizon`, `shadow_length_m`, `shadow_azimuth_deg_clockwise_from_north`. Shadow length is height/tan(altitude). Shadows are null at/below the geometric horizon (numerical tolerance: sine altitude ≤1e−12). Azimuth is null at zenith/nadir (horizontal component ≤1e−12) and at geographic poles where local north is undefined. Zenith shadow length tends to zero and its direction is null.

The corrected relations were checked against [NOAA General Solar Position Calculations](../sources/index.md#noaa-solar-equations), especially its hour-angle, zenith and north-clockwise azimuth conventions. Solar time is required because clock conversion needs longitude, equation of time and UTC offset. This tool does not perform that conversion. It ignores refraction, solar disk size, terrain, nearby obstruction, sloped surfaces, receiver elevation, diffuse light and weather. It is geometric early-design comparison, not a surveyed solar-access finding or irradiance simulation.

```json
{"latitude_deg":45,"declination_deg":0,"solar_time_hours":12,"object_height_m":10}
```

### `daylight`

Required JSON numbers: `room_width_m`, `room_depth_m`, `room_height_m`, `window_width_m`, `window_height_m` all >0; `window_sill_m` ≥0. A single rectangular window must fit the wall of width `room_width_m` and height `room_height_m`: window width ≤room width and sill+height ≤room height. Inputs describe already known 2D dimensions, without creating a room/window model.

For the sill-plus-height comparison only, an excess of at most two units in the last place (ULPs) of the floating-point room height is treated as equality to accommodate binary representation and addition rounding. This is a numerical tolerance, not a physical fitting allowance; width is compared directly. Inputs and outputs still use floating-point arithmetic.

Outputs: `floor_area_m2 = width×depth`; `window_area_m2 = window width×height`; `room_total_internal_surface_area_m2 = 2(width×depth+width×height+depth×height)` including floor, ceiling and all wall surfaces with glazing counted once in the enclosing wall; `window_to_floor_ratio_pct`; `window_to_host_wall_ratio_pct`. Window area is the declared comparison aperture; state whether it includes frames and keep that convention fixed. **These are geometry proxies, not daylight factor, illuminance, daylight autonomy, glare, useful daylight or regulatory pass/fail.** No visibility/sky-angle, glass, reflection or obstruction simulation occurs. The source's unsupported DF formula has deliberately not been reproduced.

```json
{"room_width_m":4,"room_depth_m":5,"room_height_m":3,"window_width_m":2,"window_height_m":1.5,"window_sill_m":1}
```

### `uvalue`

Required object fields: `layers` is a nonempty array; `rsi_m2K_W` and `rse_m2K_W` are explicit finite nonnegative internal/external surface resistances in m²K/W. Every layer is exactly `{"name": "nonempty material label", "thickness_m": positive number, "conductivity_W_mK": positive number}`. Conductivity is in W/(m·K). Source material properties and surface resistances for the intended orientation, heat-flow direction and conditions outside this tool; no catalog/code values are supplied.

Outputs: `layer_resistances_m2K_W` in input order, `total_resistance_m2K_W`, `u_value_W_m2K`, `total_thickness_m`. Each homogeneous plane layer contributes thickness/conductivity; total includes both explicit surface resistances; U=1/total. This is steady one-dimensional series conduction through uniform layers. Excludes cavities requiring equivalent resistance, repeated framing/parallel paths, fixings, thermal bridges, openings, moisture effects and transient performance; do not treat its result as a composite facade U-value or certification.

```json
{"layers":[{"name":"comparison layer","thickness_m":0.2,"conductivity_W_mK":0.1}],"rsi_m2K_W":0.1,"rse_m2K_W":0.4}
```

## Verification

Run `python3 -B -m unittest discover -s level-2/architecture/scripts -p test_calculators.py -v` from the repository root (or `python3 -B -m unittest discover -s scripts -p test_calculators.py -v` from the skill directory). The local suite contains independently worked arithmetic/analytic answers, solar morning/afternoon and hemisphere directions, zero/zenith/horizon/polar boundaries, geometry fit, series resistance and CLI/schema/nonfinite/overflow failures. This validates the bounded arithmetic and interface; it does not validate a native simulation or any regulatory outcome.
