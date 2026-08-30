# Circuit grouping and overcurrent protection

## Grouping

Default groups: lighting (1+ circuits), general sockets per zone, kitchen
sockets (separate), each wet zone, dedicated fixed appliances (oven, hob,
boiler, washer/dryer, dishwasher, AC, underfloor heating), networking/smart
home, spare. A dedicated circuit per appliance only when at least one holds:

- verified normative requirement for that load class;
- manufacturer requirement (from real documentation);
- Ib of the appliance close to circuit capacity;
- functional isolation need (e.g. fridge kept on during trips elsewhere).

Otherwise combining is fine — say why. Avoid one-circuit-per-socket sprawl.

## Overcurrent devices (MCB / RCBO overcurrent part)

Per circuit verify and state:

- **Coordination: Ib ≤ In ≤ Iz.** Ib from calculation, Iz from verified
  ampacity (see cable-selection.md). Any member missing → UNRESOLVED.
- **Rated current In** — standard ratings (6/10/13/16/20/25/32 A…).
- **Trip curve** — B vs C: justify from load inrush; label ENGINEERING
  RECOMMENDATION unless a verified clause applies.
- **Breaking capacity (Icn)** — compare with prospective fault current at
  the board; unknown fault current → state the chosen Icn (commonly 6 kA
  product class, COMMON INDUSTRY PRACTICE) and mark verification UNRESOLVED.
- **Poles** — 1P vs 1P+N vs 2P for single phase; 3P/3P+N/4P for three phase;
  note interaction with RCD neutral handling (rules/rcd-rcbo.md).
- **AFDD (ПВДП)** — check ДБН В.2.5-23:2025 Додаток Д (mandatory annex)
  excerpt for whether the case requires arc-fault detection.

Explain every selection; a rating without a reason is not a deliverable.
