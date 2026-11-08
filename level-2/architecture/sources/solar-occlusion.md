# Primary evidence for geometric solar occlusion

These records support [multi-building sun intervals](../references/performance/comfort/multi-building-sun.md).
They are maintenance provenance, not a runtime dependency, an ephemeris or a
normative-insolation source. Selected reading date: 2026-11-08.

## Ray and box intersection

Identity: Matt Pharr, Wenzel Jakob and Greg Humphreys, *Physically Based
Rendering: From Theory to Implementation*, third-edition online text,
[3.1 Basic Shape Interface](https://pbr-book.org/3ed-2018/Shapes/Basic_Shape_Interface),
especially 3.1.1 Bounding and 3.1.2 Ray–Bounds Intersections. The
[online contents/footer](https://pbr-book.org/3ed-2018/contents) identifies the
authors, copyright 2004–2021 and CC BY-NC-ND 4.0 book-text licence.

Inspected: object/world bounds and transformations; three-slab intersection,
parameter ordering, parallel directions and numerical roundoff/NaN discussion;
licence footer. Selected page text was readable through web retrieval. A raw
HTTP download returned 403; no live byte hash, full-book inspection or image/
formula-rendering validation is claimed. No software was installed or executed.

Adapted mechanism: intersect a ray's parameter intervals in an actual solid's
local frame. A bounding-box miss can exclude a contained solid, while a hit is
not evidence of an arbitrarily shaped solid's actual intersection. The local
method uses original algebra/prose and an explicit zero-direction branch, not
the source's floating-point reciprocal implementation. The fixed-declination
event partition, proof of event completeness, interval/uncertainty accounting,
architectural examples and tests are original synthesis, not source assertions.

Excluded: all renderer implementation/code, acceleration structures, shading/
radiometry, figures and book prose. No CC licence permission to redistribute
modified book text or images is inferred. Only bibliographic links and original
explanations/mathematics are installed; the book licence does not cover or impose
an imported code component because none was imported.

## Solar geometry and time basis

The existing [NOAA record](index.md#noaa-solar-equations) owns the primary URL
and formula provenance. Pass C reinspection covers both PDF pages: fractional
year/declination and equation-of-time approximations, true solar time, longitude/
UTC-offset conventions, hour angle, zenith/azimuth and the distinct sunrise
correction. The retrieved 208,947-byte PDF has SHA-256
`7fa1fdb5f6b5c05ab1ec3ffde92e6fb2d5df98bf1a87055075ae2c3c1240a627`.
Text was checked through web retrieval and `pdftotext`; no source diagram is used.

Adapted boundary: the existing four-input solar calculator requires supplied
declination and apparent solar time; no date/time converter or astronomical
accuracy claim is added. The new interval proof freezes declination explicitly
and uses the same spherical geometry. Its exactness is conditional on that
model, the actual prisms and input precision. It does not adopt NOAA's date
approximation, atmospheric/sunrise correction or a legal test date/duration.
The PDF is primary technical provenance, not normative approval. No explicit
media-reuse permission was selected or needed for the installed original
derivations; no source text, PDF or illustration is redistributed.

## Verification extent

Local checks compare a single body to an independent special-case construction,
overlapping intervals to their union, high/low receivers, moved/lowered bodies,
front-face/parallel/tangent cases and the retained calculator. A changed latitude,
declination and three rotated prisms are also checked against independently
projected convex shadow silhouettes. These are bounded mathematical evaluations,
not a validated annual daylight/solar application or statutory insolation test.
Actual geometry, ephemeris/time conversion, uncertainty and legal aggregation
remain separate evidence. Rights/notices and the four calculator contracts remain
at their existing owners.
