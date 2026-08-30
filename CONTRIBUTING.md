# Contributing

## Ground rules

1. **Never commit normative texts.** ДСТУ/ДБН/ПУЕ wording and manufacturer
   manuals belong only in the untracked `references/local/` layer. CI and
   review should reject PRs that add them. Update
   `references/standards-index.md` (metadata only) instead.
2. **Never weaken citation integrity.** The six output classifications and
   the "no excerpt read this session → no clause citation" rule are the
   core of the plugin. Changes that let a recommendation read like a legal
   requirement will not be merged.
3. **No project state in the plugin.** Anything describing one specific
   dwelling goes to `examples/` with an explicit EXAMPLE label, or nowhere.
4. **Deterministic calculations stay stdlib-only.** Normative parameters
   are inputs, never constants. Every behavior change needs a test in
   `scripts/test_elec_calc.py`.
5. Public API (avoid breaking; document in CHANGELOG if unavoidable):
   plugin name, skill names, `templates/project-input.yaml` fields,
   `elec_calc.py` CLI, template structure, the six classifications.

## Checks before a PR

```bash
python3 scripts/test_elec_calc.py
claude plugin validate . --strict
```

## Release process (maintainers)

1. Update `version` in `.claude-plugin/plugin.json` (SemVer:
   MAJOR = breaking public API, MINOR = new capability/rules/references,
   PATCH = fixes and wording).
2. Add a section to `CHANGELOG.md`.
3. Commit, tag, push, and publish a GitHub Release:

   ```bash
   git commit -am "release: vX.Y.Z"
   git tag vX.Y.Z && git push && git push --tags
   gh release create vX.Y.Z --verify-tag --latest \
     --title "vX.Y.Z — <short summary>" --notes "<CHANGELOG section>"
   ```

4. Users receive the update via `/plugin marketplace update` (or the
   automatic check) once the pushed `plugin.json` version is higher. Do not
   add a `version` to the marketplace entry — the single authoritative
   version is `plugin.json`.
