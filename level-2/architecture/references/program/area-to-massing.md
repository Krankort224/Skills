# Allocate housing area to footprints and storeys

Use this method when a housing-group or quarter concept has a required amount
of accommodation but no settled distribution of building lengths and heights.
An equivalent single-storey strip is an area-accounting device, not a continuous
building or a required length of facade. Choose explicit preliminary depth and
yield assumptions; develop representative sections when they can overturn them.

## Contents

- [Establish the area target](#establish-the-area-target)
- [Allocate length and storeys](#allocate-length-and-storeys)
- [Worked mixed-height allocation](#worked-mixed-height-allocation)
- [Replace assumptions with section evidence](#replace-assumptions-with-section-evidence)
- [Evidence and related decisions](#evidence-and-related-decisions)

## Establish the area target

Reuse the [area ledger](area-ledger.md) for measurement boundaries and once-only
allowances. State the source and status of each input; a density ceiling is not
an instruction to fill to it. When the brief supplies apartment area directly,
start there instead of inventing a population.

| Input | Meaning and valid basis |
| --- | --- |
| A, rho | Population calculation territory in hectares and chosen persons/ha on that same territory; not automatically the gross parcel or land available for placement |
| N, q | Population and required apartment area per person; an apartment count additionally needs a dwelling mix or stated size |
| k_h | Apartment area / residential gross floor area, with 0 < k_h <= 1; state the treatment of walls, cores, shared access and residential support |
| b | Preliminary building depth in metres on the same boundary as gross floor area; select a plausible access/dwelling family |
| G_x | Separately allocated nonresidential gross floor area outside k_h's denominator; zero only when that is the actual scenario |

The housing chain, when population is density-derived, is:

```text
N = A * rho
S_ap = N * q
G_h = S_ap / k_h
G = G_h + G_x
L = G / b
```

S_ap, G_h, G_x and G are m²; L is equivalent strip length in metres.
At k_h=0.7, divide S_ap by 0.7, not multiply it by 1.3. Do not add cores or
circulation again if the denominator already includes them. Keep housing and
nonhousing subtotals: commercial floor area cannot replace required apartments.
Separate buildings for education or other services need their own program and
land reservation; they are not silently included in this housing allocation.

## Allocate length and storeys

For nonoverlapping rectangular buildings with common depth b and identical
contributing floor plates, length l_i and floor count n_i give:

```text
G_alloc = b * sum(l_i * n_i)
sum(l_i * n_i) = L                 # when the target is exactly met
F = b * sum(l_i)
n_equiv = G_alloc / F
R = G - G_alloc                    # positive: shortfall; negative: excess
```

For different depths, conserve area directly with
G_alloc=sum(b_i*l_i*n_i). Unweighted strip lengths of different depths are not
comparable. Overlapping wings, shared podiums, voids, setbacks and different
ground/top floors require the union of actual counted polygons on each level,
then a sum across levels. Define F separately: here it is the union of horizontal
projections of the included building parts, not a legal footprint definition or
usable ground beneath an overhang. A ground-occupied footprint may differ.
G_alloc/F is then an equivalent full-floor count; it is not necessarily any
building's literal storey count. Metres of height require the actual floor
heights, ground levels and roof allowances.

1. Hold the area target and its measurement basis constant while choosing
   [building/open-space relationships](../context/urban/quarter-and-public-space.md).
   Reserve service facilities, routes and outdoor uses on their own basis.
2. Allocate lengths, depths and storeys to those spatial roles. A trial footprint
   F implies n_equiv=G/F; uniform n implies F=G/n. Neither identity proves that
   the shapes fit or determines a good composition.
3. Keep an entry for each building/segment: plate geometry, contributing floors,
   housing and nonhousing allocation, footprint and assumptions. Report R and,
   for a positive target, R/G. If rounding to section modules changes the total,
   show that residual; any accepted tolerance comes from the study brief.
4. Compare lower/extended, taller/compact or mixed allocations at the same
   target. Increasing one part's area requires a compensating change elsewhere.
   Recheck courts, fronts, entrances, service access and the affected section;
   do not fill a residual with an unusable fragment or silently lower demand.
5. Recalculate when representative sections change depth, yield or floor use.
   Preserve the failed allocation and identify the variable that resolves it.

## Worked mixed-height allocation

All following values are declared hypothetical inputs, not regulatory defaults
or an approved site's parameters: A=23.5 ha, rho=350 persons/ha,
q=30 m²/person, k_h=0.7, b=14 m and G_x=0.

N=8,225; S_ap=246,750 m²; G=352,500 m²; L=25,178.57 m.
Under the repeated-plate assumptions, alternative uniform heights give:

| Storeys | Combined physical building length L/n, m | Footprint G/n, m² |
| --- | ---: | ---: |
| 8 | 3,147.32 | 44,062.50 |
| 9 | 2,797.62 | 39,166.67 |
| 12 | 2,098.21 | 29,375.00 |

These totals still need subdivision, placement and applicable height evidence.
For a mixed arrangement, assign four 120 m long, 14 m deep, 12-storey buildings:
their floor area is 80,640 m² and footprint 6,720 m². The remaining
271,860 m² at nine storeys requires 271,860/(14*9)=2,157.62 m combined length.
The whole footprint is 6,720+271,860/9=36,926.67 m². Keep unrounded values
throughout: 80,640+271,860=352,500 and 352,500*0.7=246,750.
A 120 m building containing four 30 m sections is one building; four such
buildings contain sixteen sections. Gaps between them consume land, not floors.

## Replace assumptions with section evidence

Use [section variants](../typologies/housing/section-variants.md) for actual
unit/core/front/shaft fit. For each section and floor variant, multiply the
actual occurrence count by its dwelling count and defined apartment area.
Sum measured or explicitly reserved gross plates independently. Ground
tenancies, upper setbacks and omitted floors change their own entries.

Recompute k_h using only the residential denominator defined above; retain
k_all=S_ap/G separately if the building also contains G_x. A good total-area
match can still conceal missing housing. Compare actual S_ap with its fixed
target and revise coherent modules, floor uses or permitted heights. Changing
the coefficient on paper does not repair a shortfall. The
[housing-yield recount](../../assets/studies/housing-yield-recount.md) shows how
exceptional floors reverse a preliminary allowance without changing the footprint.

## Evidence and related decisions

These are area identities and authored hypothetical studies adapted from
[recovered local methods](../../sources/index.md#recovered-local-methods).
No current legal values, measured building geometry or new external reading
are supplied. The retained area calculator accepts totals; it does not derive
this population/strip allocation.

- Requires — [Area ledger](area-ledger.md): establish each numerator, denominator and mutually exclusive use.
- Affects — [Mass and void](../composition/massing/mass-and-void.md): redistribute the same program while comparing spatial consequences.
- Affects — [Service allocation](../context/urban/service-capacity-allocation.md): changed housing/population may change facilities, routes and land.
- Illustrated by — [Quarter alternatives](../../assets/studies/quarter-massing-comparison.md): equal floor area and footprint can create different outdoor places.
