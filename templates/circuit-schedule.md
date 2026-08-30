# Circuit schedule — output template

## Per-circuit block

```
Circuit: <name>

Load:
  Loads served: <list>
  Estimated load: <W> (installed) / <W> (demand, k=<value, source>)
  Design current Ib: <A>  [elec_calc.py current]

Cable:
  Type: <e.g. ВВГнг-LS 3x2.5>
  Cross-section: <mm2>
  Length: <m one-way | UNRESOLVED (needs: route length)>
  Installation method: <... | UNRESOLVED (needs: installation method)>
  Ampacity Iz: <A, source of value> | UNRESOLVED
  Voltage drop: <V / %>  [elec_calc.py vdrop] vs limit <% + source | UNRESOLVED>

Protection:
  Breaker In: <A>   Curve: <B/C>   Breaking capacity: <kA | UNRESOLVED (needs: prospective fault current)>
  Coordination: Ib <In> ≤ In <In> ≤ Iz <Iz | UNRESOLVED>

Residual protection:
  RCBO/RCD: <device / covered by group RCD #n / none + reason>
  Residual current: <mA>   Type: <AC/A/F/B>   Poles: <n>

Normative basis:
  - Standard: <id> / Clause: <n> / Requirement: «<verbatim quote>» / Source: references/<file>
  (or: UNRESOLVED — normative text not in local references)

Engineering rationale: <why this grouping/cable/device>

Status: VERIFIED NORMATIVE REQUIREMENT | ENGINEERING RECOMMENDATION |
        COMMON INDUSTRY PRACTICE | ASSUMPTION | UNRESOLVED
        (label the weakest link in the chain, per element if mixed)
```

## Summary table

| # | Circuit | Load | Cable | MCB/RCBO | RCD | Phase | Modules | Status |
| - | ------- | ---: | ----- | -------- | --- | ----- | ------: | ------ |

## Decision record (for safety/cost-relevant choices)

```
DECISION
  <what was decided>
NORMATIVE BASIS
  <verified citations or "none — see engineering basis">
ENGINEERING BASIS
  <calculations, physics, coordination>
ASSUMPTIONS
  <numbered; each one the user can confirm or replace>
ALTERNATIVES
  <options considered, trade-offs: safety / nuisance trips / fault isolation / cost / modules / maintainability>
```
