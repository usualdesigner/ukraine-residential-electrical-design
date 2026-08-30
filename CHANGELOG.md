# Changelog

All notable changes to this plugin. Format: [Keep a Changelog](https://keepachangelog.com/);
versioning: [SemVer](https://semver.org/). The authoritative version is
`.claude-plugin/plugin.json`.

## [1.0.0] — 2026-08-30

First public release.

### Added
- `design` skill: greenfield design, review/audit, and standalone checks
  for Ukrainian residential LV installations, with six-label output
  classification and strict normative-citation integrity.
- `init-project` skill: scaffolds project files in the consumer repository
  (explicit invocation only).
- Topic rule files: cable selection, circuit protection, RCD/RCBO,
  grounding, bathrooms, surge protection, panel design, three-phase.
- `references/standards-index.md`: maintained index of the Ukrainian
  regulatory framework (editions, status, effective dates, supersessions).
- `references/local/` untracked layer for user-supplied normative texts
  and manufacturer data (never redistributed).
- Deterministic calculator `scripts/elec_calc.py`
  (current / vdrop / loads / balance / modules) with unit tests.
- Templates: project input schema, circuit schedule, panel schedule,
  compliance checklist.
- Example fixtures: worked single-phase apartment, three-phase balancing,
  incomplete-input behavior.
