# EXAMPLE output — design for `input.yaml`

Produced with the `ukraine-electrical` plugin's `design` skill in an
installation whose `references/local/` layer had been populated with
ДБН В.2.5-23:2025 excerpts (transcribed from a scanned copy — exact wording
must be verified against the official edition before formal use). In an
installation without that local material, the quoted citations would
instead read `UNRESOLVED (reference required: ДБН В.2.5-23:2025)`.
Abridged for publication: three circuits are worked in full, the rest
appear in the summary table, and verbatim normative quotes are replaced by
clause references with paraphrases (a real report quotes the exact wording
from the local excerpts). This is illustrative material, not a reference
design.

## 1. Missing information register

| # | Missing datum | Blocks |
|---|---|---|
| M1 | Grounding system (TN-S / TN-C-S / …) — `unknown` | RCD protection guarantees, SPD connection scheme, PE origin |
| M2 | Building-level SPD — `unknown` | SPD type/coordination |
| M3 | Cable route lengths | Voltage-drop verification per circuit |
| M4 | Cable installation method (conduit in wall / screed / …) | Ampacity Iz → Ib ≤ In ≤ Iz check |
| M5 | Prospective fault current at panel | Breaking-capacity verification |
| M6 | Hob manufacturer manual | Connection mode, dedicated-circuit parameters |
| M7 | Incoming breaker "C40 2P" unverified | Supply capacity, selectivity |

Design continues below; every decision touched by M1–M7 carries UNRESOLVED.

## 2. Supply assessment

- Declared: 1-phase 230 V, 8 kW allocated.
- Design load per norm: apartment in a building with electric stoves up to
  8,5 кВт → питоме розрахункове навантаження **10,00 кВт** for 1 dwelling.
  - Standard: ДБН В.2.5-23:2025 / Clause: таблиця 6.1, рядок 1.3, колонка «1»;
    примітка 2 (metering and input protection of a single dwelling are
    selected from the one-dwelling specific design load)
  - Source: `references/local/dbn-v2.5-23-2025/04-06-supply-and-loads.md`
    *(in the real report the exact wording is quoted from the local
    excerpt; quotes are omitted in this published example)*
  - Status: VERIFIED NORMATIVE REQUIREMENT
- **CONFLICT SURFACED**: 8 kW allocation < 10 kW normative design load.
  Options (user decision): renegotiate allocated power; load-management
  (hob power limiting per manufacturer — needs M6); or document the
  discrepancy with the utility. Not silently resolvable.
- ASSUMPTION A1: dwelling classified as житло 1-го виду, III рівень
  електрифікації (row 1.3). Classification criteria are in 6.1.3–6.1.4 —
  confirm; a 7 kW hob + 3,5 kW oven may push the installed stove power
  above 8,5 кВт depending on how «електроплита» is counted → if so, row
  1.4 (12,00 кВт) applies. UNRESOLVED (needs: classification decision).
- Aggregate check (`elec_calc.py loads`, per-appliance k are ASSUMPTIONS
  listed in the JSON): installed 21,7 kW, naive demand ≈ 16 kW — confirms
  the allocation problem regardless of method.

## 3. Circuits (worked examples)

### Circuit K1 — Induction hob

```
Load:            hob-induction 7000 W (installed); Ib = 30.43 A [elec_calc.py current]
Cable:           Cu, 3x6 mm2 (phase/N/PE)
                 - Single-phase electric-stove line: copper, minimum 6 mm2 —
                   ДБН В.2.5-23:2025, п. 7.23 — VERIFIED NORMATIVE REQUIREMENT
                 - Dedicated group line for the stove required — п. 7.23 —
                   VERIFIED NORMATIVE REQUIREMENT
                 Length: UNRESOLVED (M3). Illustrative: at 12 m, drop = 2.13 V =
                 0.93 % ≤ 5 % limit (voltage-drop caps: 3 % lighting / 5 % other
                 loads, п. 5.11 — VERIFIED) [elec_calc.py vdrop]
                 Installation method: UNRESOLVED (M4) → Iz unknown → Ib ≤ In ≤ Iz
                 check UNRESOLVED
Protection:      C32 1P+N; Ib 30.43 ≤ In 32 ✓; In ≤ Iz UNRESOLVED (M4)
                 Curve C: ENGINEERING RECOMMENDATION (no inrush data — M6)
                 Breaking capacity: 6 kA product class, COMMON INDUSTRY PRACTICE;
                 verification vs fault current UNRESOLVED (M5)
Residual:        RCBO 30 mA type A — ENGINEERING RECOMMENDATION (fixed appliance;
                 the verified 30 mA mandate in п. 7.24 covers socket lines; type A
                 for inverter electronics). If connected via 32 A socket per
                 п. 7.66 — 30 mA becomes VERIFIED per п. 7.24.
Status:          Mixed — cable/dedicated line VERIFIED; ampacity, vdrop, Icn UNRESOLVED
```

### Circuit B1 — Bathroom sockets (washing machine)

```
Load:            washing-machine 2200 W; Ib = 9.57 A
Cable:           Cu 3x2.5 mm2 (≥ 1,5 мм² min for group lines, таблиця 8.1 —
                 VERIFIED; 2.5 chosen for margin — ENGINEERING RECOMMENDATION)
Protection:      C16 1P+N; Ib 9.57 ≤ 16 ✓; Iz UNRESOLVED (M4)
Residual:        ПЗВ ≤ 30 mA MANDATORY + ПВДП (AFDD) MANDATORY on bathroom
                 socket lines; combined ПЗВ+ПВДП devices recommended —
                 п. 7.25, VERIFIED NORMATIVE REQUIREMENT
                 Type A — ENGINEERING RECOMMENDATION (inverter motor drive)
Zones/IP:        Equipment placement per ДСТУ HD 60364-7-701 (п. 7.67 requires it —
                 VERIFIED); zone dimensions/IP text NOT in local references →
                 UNRESOLVED (needs: 60364-7-701 excerpt + fixture positions)
Status:          Residual protection VERIFIED; zoning UNRESOLVED
```

### Circuit S1 — General sockets (living + bedroom + hallway)

```
Load:            general-sockets 2000 W, k=0.5 (ASSUMPTION A2); Ib ≈ 8.7 A
Sockets count:   living 22 m2 → ≥6; bedroom 16 m2 → ≥4; hallway 8 m2 → ≥1
                 (≥1 socket per full/partial 4 m² of living-room area;
                 per 10 m² in apartment corridors — п. 7.66, VERIFIED)
Cable:           Cu 3x2.5 mm2 (min 1,5 мм², таблиця 8.1 — VERIFIED; 2.5 for
                 socket circuits — COMMON INDUSTRY PRACTICE)
Protection:      C16 1P+N; Iz UNRESOLVED (M4)
Residual:        ПЗВ ≤ 30 mA MANDATORY on group lines feeding socket
                 outlets — п. 7.24, VERIFIED NORMATIVE REQUIREMENT
AFDD:            Recommended (not mandated) for this circuit — таблиця 7.1
                 places new multi-apartment residential buildings in the
                 "recommended" (not "mandatory") ПВДП column — VERIFIED;
                 see conflict C1 below.
Status:          RCD VERIFIED; ampacity/vdrop UNRESOLVED (M3, M4)
```

## 4. Circuit schedule (summary)

| # | Circuit | Load | Cable (Cu) | MCB/RCBO | RCD | Phase | Modules | Status |
|---|---------|-----:|-----------|----------|-----|-------|--------:|--------|
| K1 | Hob (dedicated) | 7000 W | 3x6 | RCBO C32 | 30mA A | L | 2 | partial-UNRESOLVED |
| K2 | Oven (dedicated) | 3500 W | 3x2.5 | RCBO C16 | 30mA A | L | 2 | partial-UNRESOLVED |
| K3 | Kitchen sockets (≥5, п.7.66) | 2300 W | 3x2.5 | RCBO C16 | 30mA A | L | 2 | partial-UNRESOLVED |
| B1 | Bathroom sockets | 2200 W | 3x2.5 | RCBO C16 | 30mA A + ПВДП | L | 2 | zoning UNRESOLVED |
| B2 | Boiler + towel warmer (fixed) | 2600 W | 3x2.5 | RCBO C16 | 30mA A | L | 2 | partial-UNRESOLVED |
| S1 | General sockets | 2000 W | 3x2.5 | RCBO C16 | 30mA A | L | 2 | partial-UNRESOLVED |
| A1 | AC living + bedroom | 1600 W | 3x2.5 | RCBO C16 | 30mA A | L | 2 | partial-UNRESOLVED |
| L1 | Lighting (incl. bathroom) | 500 W | 3x1.5 | MCB B10 + ПВДП* | via ПЗВ* | L | 2 | see C1 |

\* Bathroom lighting residual/AFDD treatment depends on conflict C1.

## 5. Conflict register

**C1 — AFDD scope for bathroom lighting.** Додаток Д п. Д.3.6
(обов'язковий) mandates ПВДП in group networks feeding socket outlets and
lighting systems of bath/shower rooms — but its Ukrainian syntax (see the
exact wording in the local excerpt) supports two readings:
(a) all socket circuits + bathroom lighting;
(b) sockets and lighting of bathrooms/showers only. Таблиця 7.1 lists new
multi-apartment buildings under *recommended* AFDD, and п. 7.25 mandates
ПВДП for bathroom *socket* lines. Reading (b) is consistent with both;
reading (a) would make AFDD mandatory on every socket circuit. Also note:
**таблиця Д.1 is missing from the local scan** (its own gap note). →
Presented to the user; safest interpretation until officially clarified:
AFDD on B1 and on bathroom lighting. UNRESOLVED as to reading (a).

**C2 — Allocation vs design load** — see §2.

## 6. Panel

`elec_calc.py modules` (RCBOs assumed 2-module — ASSUMPTION A3, series
unknown): devices 21 modules, +20 % reserve → **26 → 36-module enclosure**
(next market size, COMMON INDUSTRY PRACTICE).

```
[Floor board: meter + "C40 2P" (M7, unverified)]
  └─ In-apartment panel
       ├─ Main switch 2P 40A                       (2 mod)
       ├─ Voltage monitoring relay                 (3 mod) ENGINEERING RECOMMENDATION
       ├─ SPD: UNRESOLVED (M1, M2 — system + building SPD unknown)
       ├─ RCBO K1, K2, K3, B1(+ПВДП), B2, S1, A1  (14 mod)
       ├─ MCB B10 L1 + ПВДП combined              (2 mod)
       └─ spare                                    (≥5 mod)
N per RCBO handled at the device; PE bus single, unswitched.
```

**Grounding warning (always applies):** grounding system is UNKNOWN (M1).
Never bridge N to PE or to plumbing inside the apartment; if the riser
turns out to be TN-C without PE, resolution goes through the building
owner/ОСББ and a qualified designer.

## 7. Compliance checklist verdicts (abridged)

- Cable vs breaker: In ≥ Ib everywhere ✓; Iz UNRESOLVED (M4) on all circuits
- RCD coverage: all socket circuits 30 mA (VERIFIED п. 7.24/7.25); fixed-appliance circuits 30 mA (ENGINEERING RECOMMENDATION)
- AFDD: B1 VERIFIED-mandatory; scope beyond → C1
- Voltage drop: limits VERIFIED (п. 5.11: 3 % lighting / 5 % other); per-circuit checks UNRESOLVED (M3)
- Load vs allocation: **FAIL / C2** — must be resolved with the utility
- Panel capacity: 36-module enclosure proposed, 10+ spare ✓
- SPD, breaking capacity, neutral topology: UNRESOLVED (M1, M2, M5, M7)

## 8. Field verification required

Actual grounding system and riser arrangement; insulation resistance; PE
continuity; loop impedance / fault current; RCD trip tests; upstream
protection and building SPD; commissioning. **This design is a planning
document — it does not replace a licensed designer where legally required,
nor acceptance by a qualified electrician.**
