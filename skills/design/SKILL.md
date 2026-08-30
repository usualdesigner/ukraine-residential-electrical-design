---
name: design
description: Ukrainian residential low-voltage electrical engineering - use when designing, reviewing, or checking apartment/house electrical installations in Ukraine - circuits, cables, MCB/RCD/RCBO, grounding, bathrooms, SPD, load and voltage-drop calculations, panel layout, compliance against ПУЕ / ДБН В.2.5-23:2025 / ДСТУ HD 60364.
when_to_use: Use for ANY question about Ukrainian residential electrical installations, including quick one-off checks - do not answer such questions from memory without this skill. Triggers include designing circuits for a Ukrainian apartment, reviewing a panel or design against Ukrainian standards, validating cable+breaker combinations, selecting protection for loads, bathroom electrical review, balancing three-phase loads, auditing a design for unresolved issues. Works with complete or partial project data.
---

# Ukraine Residential Electrical Design

Engineering planning and verification for residential electrical
installations under the Ukrainian regulatory framework. Priority order:

**CORRECTNESS > SAFETY > TRACEABILITY > REUSABILITY > CONTEXT EFFICIENCY > MAINTAINABILITY > CONVENIENCE**

Every important decision must be tied to a verified regulation, an explicit
calculation, a manufacturer requirement, or a clearly stated assumption.
An unimpressive honest answer beats an impressive fabricated one.

All plugin paths below are under `${CLAUDE_PLUGIN_ROOT}`. The plugin
directory is read-only capability: **project state (inputs, decisions,
reports) always lives in the user's own project, never in the plugin.**

**Local reference layer** (user-supplied normative texts, referred to as
`references/local/` throughout): check BOTH locations and use whichever
files exist — `${CLAUDE_PLUGIN_DATA}/references/local/` (survives plugin
updates; preferred for installed plugins) and
`${CLAUDE_PLUGIN_ROOT}/references/local/` (development checkouts). If a
user wants to add normative excerpts to an installed plugin, direct them
to `${CLAUDE_PLUGIN_DATA}/references/local/` and tell them its resolved
path.

## Classification labels (stable public vocabulary)

Label every requirement, decision, and check with exactly one of:

| Label | Meaning |
|---|---|
| `VERIFIED NORMATIVE REQUIREMENT` | Wording confirmed this session in a file under `references/local/` (cite standard + clause + source file) |
| `ENGINEERING RECOMMENDATION` | Sound practice justified by calculation or physics, not legally required |
| `MANUFACTURER REQUIREMENT` | From manufacturer documentation (local layer or user-supplied) |
| `COMMON INDUSTRY PRACTICE` | Widely done in Ukraine, but no verified normative source at hand |
| `ASSUMPTION` | Value or condition assumed to proceed; must be listed for confirmation |
| `UNRESOLVED` | Cannot be decided; state exactly what is missing — input data (`needs: <datum>`) or normative text (`reference required: <standard>`) |

Never present an `ENGINEERING RECOMMENDATION` or `COMMON INDUSTRY PRACTICE`
as a legal requirement. Never upgrade a label to make output look stronger.

## Iron rules (anti-hallucination)

1. **Never invent normative content**: standard names, editions, clause
   numbers, thresholds, cable sizes, RCD parameters, breaker ratings,
   bathroom zones, voltage-drop limits, grounding or installation rules.
2. Cite a clause **only after reading its wording this session** in
   `references/local/`. Remembered or "well-known" clauses do not count.
   No local excerpt → `UNRESOLVED (reference required: <standard>)`.
3. Never claim compliance without evidence for every checked item.
4. Never infer the grounding system (TN-C / TN-S / TN-C-S) from "typical
   practice". Ask, or mark UNRESOLVED.
5. Never assume: cable installation method, cable length, ambient
   temperature, grouping, available short-circuit current, upstream
   protection, existence of a building SPD, allocated power, number of
   phases, PEN separation point, or an appliance's manufacturer requirements.
6. "Commonly done in Ukraine" is never "required by ПУЕ/ДСТУ/ДБН".
7. Prefer `UNRESOLVED` over fabricated certainty.
8. When two standards conflict, surface the conflict with both citations;
   record it in the decision record. Do not silently pick one.
9. Local excerpts are user-supplied transcriptions — repeat the provenance
   caveat from the excerpt header when exact wording is load-bearing.
10. If a rule here conflicts with producing a "complete-looking" design,
    the rule wins. Deliver the design with gaps marked.

## Entry modes

Match the request; never force the full workflow:

- **Greenfield design** — from a project description/input file, produce
  circuits, protection, panel. Follow the workflow below.
- **Review / audit** — an existing design, panel schedule, or panel photo
  transcription: run the relevant checks from
  `templates/compliance-checklist.md` against it; report findings with
  labels; do not redesign unless asked.
- **Standalone check / calculation** — a single question ("is 2.5 mm² with
  C20 valid?", "balance these loads"): answer it directly with the relevant
  rule file + calculator; state what surrounding data would change the answer.

Partial input is normal. A missing datum blocks only the decisions that
depend on it — continue with everything else and mark the rest
`UNRESOLVED (needs: <exact missing datum>)`.

## Reference navigation (load only what the task needs)

First, for anything normative: read
`${CLAUDE_PLUGIN_ROOT}/references/standards-index.md` — which standards
exist and their editions — then check the local reference layer (both
locations above) for excerpts; the layer is user-populated and may be
empty — the skill still works, with more UNRESOLVED.

Then load per topic, only when the topic is actually in play:

| Topic | Read |
|---|---|
| Circuit grouping, MCB/overcurrent, AFDD | `rules/circuit-protection.md` |
| Conductor material/section, ampacity, voltage drop | `rules/cable-selection.md` |
| RCD/RCBO parameters and architecture | `rules/rcd-rcbo.md` |
| Grounding, PE/N/PEN topology | `rules/grounding.md` |
| Bathrooms / wet zones | `rules/bathrooms.md` |
| Surge protection | `rules/surge-protection.md` |
| Panel/DIN layout, module count | `rules/panel-design.md` |
| Three-phase supply, phase balancing | `rules/three-phase.md` — skip for confirmed single-phase |
| Input schema for a project | `templates/project-input.yaml` |
| Output formats | `templates/circuit-schedule.md`, `templates/panel-schedule.md` |
| Final review | `templates/compliance-checklist.md` |

Do not load bathroom rules for a dry-room lighting question, three-phase
rules for a single-phase project, or manufacturer data unless a specific
manufacturer is requested (core reasoning stays manufacturer-neutral:
ratings, curves, poles, RCD type, module widths — not SKUs).

## Deterministic calculations

Never do engineering arithmetic mentally:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/elec_calc.py" current --power-w 2300 --voltage-v 230
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/elec_calc.py" vdrop --current-a 10 --length-m 20 --section-mm2 1.5
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/elec_calc.py" loads circuits.json   # or - for stdin
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/elec_calc.py" balance loads.json
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/elec_calc.py" modules devices.json --reserve-percent 20
```

The script hard-codes physics only (Cu/Al resistivity). Normative limits
(permissible voltage drop, demand factors, ampacity) are **inputs** — take
them from verified references and show where each came from. Echoed inputs
in the JSON output are part of the deliverable: keep them visible.

## Output formats

Per circuit: the block from `templates/circuit-schedule.md` (load, cable,
protection, residual protection, normative basis, engineering rationale,
status) plus the summary table. Safety- or cost-relevant choices get a
decision record (`DECISION / NORMATIVE BASIS / ENGINEERING BASIS /
ASSUMPTIONS / ALTERNATIVES`). Citation format:

```
- Standard: <id + edition> / Clause: <n>
- Requirement: «exact quoted wording»
- Source: references/local/<file>.md
```

Write outputs into the **user's project** (their reports/ or wherever they
ask) — never into the plugin directory.

## Safety and limitations

This is a **DESIGN-TIME CHECK** tool. It never replaces a licensed
electrical designer where legally required, nor verification by a qualified
electrician. Mark as **FIELD VERIFICATION REQUIRED**: insulation
resistance, continuity, earth loop impedance, RCD trip testing, actual
grounding system confirmation, commissioning. State this in every final
deliverable.
