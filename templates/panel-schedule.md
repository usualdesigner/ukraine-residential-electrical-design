# Panel schedule — output template

## DIN layout

Order top-to-bottom / left-to-right; state modules per device.

| Pos | Device | Rating / type | Feeds | Modules |
| --- | ------ | ------------- | ----- | ------: |
| 1   | Main switch / incoming breaker | | whole panel | |
| 2   | SPD (if justified — see rules/surge-protection.md) | Type, Up, In/Iimp | | |
| 3   | Voltage monitoring relay (if used) | | | |
| …   | RCD / RCBO / MCB groups | | | |
|     | **Spare modules** | | | |

Totals: `elec_calc.py modules devices.json --reserve-percent <n>` — attach its JSON output.

Bus/terminal plan:
- N buses: one per RCD group downstream of its RCD — a neutral downstream of an
  RCD must never be shared with another RCD's circuits.
- PE bus: single, all PE conductors; no switching devices in PE.
- Enclosure: <modules available> vs <required incl. reserve>.

## Single-line diagram (text form)

```
[Riser / meter: <data | UNRESOLVED>]
  └─ Incoming breaker <rating>
       ├─ SPD <type> ─ PE
       ├─ RCD group 1 <mA/type>
       │    ├─ MCB <rating> — circuit 1
       │    └─ MCB <rating> — circuit 2
       ├─ RCBO <rating/mA> — circuit 3
       └─ spare
```

Every element carries its status label; unknowns upstream of the panel stay
in the diagram as `UNRESOLVED` boxes rather than disappearing.
