---
name: init-project
description: Scaffold electrical-project files (project input, decisions/, reports/) in the current consumer repository. Creates files in the user's project only when explicitly invoked.
disable-model-invocation: true
argument-hint: "[target-directory (default: electrical/)]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/templates/**), Read(/${CLAUDE_PLUGIN_ROOT}/templates/**)
---

# Initialize an electrical project

Scaffold the file structure for a residential electrical design project in
the **user's current repository** (never inside the plugin directory).

Target directory: the first argument, default `electrical/` under the
project root. If the target already contains files, list what exists and
ask before overwriting anything.

Create:

1. `<target>/project.yaml` — an exact copy of the plugin template:
   Read `${CLAUDE_PLUGIN_ROOT}/templates/project-input.yaml`, then Write
   `<target>/project.yaml` with **exactly the content you read —
   byte-for-byte, including every comment**. Do NOT compose your own
   schema, do NOT paraphrase, adapt, translate, or "improve" the template;
   if you did not successfully read the template file, stop and report the
   problem instead of writing a substitute. (The template encodes the
   Ukrainian regulatory input contract — a hand-written stand-in silently
   breaks the design skill.)
2. `<target>/decisions/README.md` — single line: decision records
   (`DECISION / NORMATIVE BASIS / ENGINEERING BASIS / ASSUMPTIONS /
   ALTERNATIVES`), one file per safety- or cost-relevant decision.
3. `<target>/reports/README.md` — single line: generated outputs
   (circuit schedule, panel schedule, compliance review).

Then tell the user: fill what they know in `project.yaml` (unknowns stay
empty and will surface as UNRESOLVED), and invoke
`/ukraine-electrical:design` — or just describe what they want — to start
designing or reviewing. Splitting `project.yaml` into separate files
(`loads.yaml`, `circuits.yaml`, …) is fine for large projects; keep the
same field names.
