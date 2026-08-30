# Changelog

All notable changes to this plugin. Format: [Keep a Changelog](https://keepachangelog.com/);
versioning: [SemVer](https://semver.org/). The authoritative version is
`.claude-plugin/plugin.json`.

## [1.0.1] — 2026-08-30

### Fixed
- Automatic (model-initiated) invocation of the `design` skill was broken:
  a Claude Code bug causes any `allowed-tools` frontmatter to make
  model-initiated skill invocation return empty content (user `/` invocation
  is unaffected). Removed `allowed-tools` from `design`; reading plugin
  reference files may now prompt for permission once per session.
  `init-project` (user-invoked only) keeps its grants.
- Local reference layer now survives plugin updates: the `design` skill
  checks `${CLAUDE_PLUGIN_DATA}/references/local/` (persistent, preferred
  for marketplace installs) in addition to
  `${CLAUDE_PLUGIN_ROOT}/references/local/` (dev checkouts);
  `references/local/README.md` documents both locations.

### Changed
- Published example output no longer contains verbatim normative quotes;
  provisions are referenced by clause number with paraphrases (a real
  report still quotes exact wording from the user's local excerpts).
- Standards index: confirmed editions ДСТУ HD 60364-5-53:2022 and
  ДСТУ HD 60364-5-54:2022 (наказ № 285 від 28.12.2022; 5-54 Зміна № 1:2023),
  removing the *(unconfirmed)* markers.

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
