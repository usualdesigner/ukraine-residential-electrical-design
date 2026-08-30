# ukraine-electrical

A Claude Code plugin for **Ukrainian residential low-voltage electrical
engineering**: circuit design, cable and protective-device selection,
RCD/RCBO architecture, grounding/PE/N topology, wet-zone requirements,
surge protection, load and voltage-drop calculations, three-phase
balancing, DIN panel layout, and compliance review against the Ukrainian
framework (ПУЕ, ДБН В.2.5-23:2025, ДСТУ HD 60364 series).

## What it is / what it is NOT

**This repository** is a reusable engineering capability: workflows,
compliance rules, deterministic calculators, schemas, and templates.

**Your repository** holds the actual project: your apartment's rooms,
loads, circuits, panel, decisions, and reports. The plugin provides
templates for those files; it never stores project state inside itself.

```
ukraine-electrical (plugin)     my-apartment-electrical (your repo)
  knows HOW to design/validate    contains WHAT is being designed
```

It is **not**: a CAD system, a substitute for a licensed electrical
designer where the law requires one, or a source of legal advice.

## Supported use cases

- Greenfield circuit/panel design for an apartment or house
- Review/audit of an existing design, panel schedule, or panel photo transcription
- Standalone checks: cable-vs-breaker validity, protection selection,
  bathroom review, three-phase balancing, voltage drop, module counting
- Incremental work with incomplete data — unknowns surface as `UNRESOLVED`,
  never as guesses

## Regulatory scope and citation integrity

Scope: residential LV installations under ПУЕ (ред. 2017), ДБН
В.2.5-23:2025 (чинні з 01.01.2026), the ДСТУ HD 60364 adoptions, and
related documents — see `references/standards-index.md` for the maintained
index (editions, status, supersessions, verification dates).

The skill **never invents normative content**. It cites a clause only when
the verbatim wording is present in `references/local/` of your
installation and was read in-session. Output uses six stable
classifications:

`VERIFIED NORMATIVE REQUIREMENT` · `ENGINEERING RECOMMENDATION` ·
`MANUFACTURER REQUIREMENT` · `COMMON INDUSTRY PRACTICE` · `ASSUMPTION` ·
`UNRESOLVED`

Recommendations are never presented as legal requirements.

## Normative texts are not bundled

Ukrainian standards (ДСТУ, ПУЕ, ДБН) and manufacturer manuals are
copyright/distribution-restricted, so the plugin ships an **index** of the
framework but not the texts. You supply legally obtained documents to the
untracked `references/local/` layer of your installation — see
`references/local/README.md` for the excerpt format and sources
(ДБН В.2.5-23:2025 is freely accessible on the official
e-construction.gov.ua portal). Without the local layer everything still
works; more findings are simply labelled `UNRESOLVED (reference required)`
instead of `VERIFIED`.

## Safety limitations

Design-time planning aid only. It does not replace: a licensed designer
where legally required, verification by a qualified electrician,
insulation-resistance/continuity/earth-loop-impedance/RCD testing, or
commissioning. Outputs distinguish **DESIGN-TIME CHECK** from
**FIELD VERIFICATION REQUIRED**.

## Installation

From GitHub (the repository is its own marketplace):

```
/plugin marketplace add usualdesigner/ukraine-residential-electrical-design
/plugin install ukraine-electrical@ukraine-electrical
```

### Local development install

```bash
git clone git@github.com:usualdesigner/ukraine-residential-electrical-design.git
claude --plugin-dir ./ukraine-residential-electrical-design
```

Validate after changes: `claude plugin validate . --strict`
Reload mid-session: `/reload-plugins`

### Updating

`/plugin marketplace update` (or Claude Code's automatic check) picks up
releases when the `version` in `.claude-plugin/plugin.json` is bumped.

## Skills

| Skill | Invocation | Purpose |
|---|---|---|
| `design` | `/ukraine-electrical:design` or automatic when a request concerns Ukrainian residential electrical work | Design, review/audit, standalone checks |
| `init-project` | `/ukraine-electrical:init-project [dir]` (explicit invocation only) | Scaffold project files in **your** repository |

## Example usage

```
/ukraine-electrical:init-project
# fill electrical/project.yaml with what you know, then:

Design circuits and a panel for the project in electrical/project.yaml.
Review this panel schedule against Ukrainian standards: <paste>
Is ВВГнг 3x2.5 behind a C20 breaker valid for a socket circuit?
Balance these loads across three phases: <list>
```

Worked fixtures live in `examples/` (labelled EXAMPLE; they carry no
defaults for real projects).

## Consumer-project workflow

1. Create/open your own repository (e.g. `my-apartment-electrical`).
2. Install the plugin; run `/ukraine-electrical:init-project`.
3. Fill `electrical/project.yaml` — empty fields mean UNKNOWN.
4. Ask for design/review; outputs go to your `electrical/reports/` and
   decision records to `electrical/decisions/`.
5. Optionally populate the plugin's `references/local/` with legally
   obtained normative texts to upgrade findings from UNRESOLVED to VERIFIED.

## Outputs

Stable, tool-consumable structures (see `templates/`): circuit schedule
(per-circuit block + summary table), panel schedule + text single-line
diagram, decision records, compliance checklist findings, missing-input
register. Calculator output is JSON with inputs echoed.

## Validation and testing

```bash
python3 scripts/test_elec_calc.py        # deterministic calculator tests
claude plugin validate . --strict        # plugin structure
```

CI runs both on every push (`.github/workflows/ci.yml`).

## Development and contributing

See `CONTRIBUTING.md` — including the rules for reference material
(never commit normative texts) and the release process.

## Versioning

Semantic Versioning; the single authoritative version lives in
`.claude-plugin/plugin.json`. Public API = plugin/skill names, schema
fields, calculator CLI, template structure, and the six output
classifications. See `CHANGELOG.md`.

## License

MIT (see `LICENSE`) — covers the plugin's own content. Normative documents
you place under `references/local/` are governed by their own terms and are
never redistributed by this repository.
