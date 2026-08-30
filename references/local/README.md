# Local reference layer (not redistributed)

Everything in `references/local/` **except this README** is excluded from
git (see `.gitignore`) and is never published with the plugin. Ukrainian
ДСТУ standards, ПУЕ, ДБН texts, and manufacturer documentation are subject
to copyright / controlled distribution — the plugin ships an index of what
exists (`../standards-index.md`) but not the texts themselves.

The skill treats this directory as its only source of citable normative
wording: **no excerpt here → no clause citation**, the affected check is
reported as `UNRESOLVED — normative text not in local references`. The
plugin remains fully usable without this layer; it just labels more of its
output as recommendation/assumption instead of verified requirement.

## How to populate it (legally obtained sources only)

1. Obtain the document yourself:
   - ДБН В.2.5-23:2025 — free official access at e-construction.gov.ua
     (search the document register); paper/PDF also sold by budstandart.
   - ДСТУ HD 60364 parts, ПУЕ — purchase from ДП «УкрНДНЦ» / budstandart
     or use a copy your organization is licensed to hold.
   - Manufacturer datasheets — download from the manufacturer.
2. Create excerpt files per document:
   - `dbn-v2.5-23-2025/<topic>.md`, `dstu-hd-60364/<part>.md`,
     `pue/<chapter>.md`, `manufacturers/<brand>/<topic>.md`
3. Each file starts with a provenance header:

   ```markdown
   # <document id> — витяги: <scope>

   > **Джерело:** <edition, publisher, how obtained>
   > **Статус:** VERIFIED — transcribed from <official text / scan>. Verify
   > exact wording against the official edition before formal use.
   > Позначка [?] — uncertain transcription; [нерозбірливо] — illegible.
   ```

4. Transcribe **verbatim** (original language), keeping clause numbers as
   printed. Mark anything uncertain with `[?]`; never guess numbers.
   You can ask Claude to transcribe from a PDF you provide — review the
   result before trusting it.
5. Add the file to the "Local excerpts" column of `../standards-index.md`
   in your local checkout.

Do not commit files from this directory to a public fork unless you have
verified you may redistribute that text.
