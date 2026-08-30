# Standards index — Ukrainian residential electrical design

Single source of truth for which standards govern this domain, their
editions and status. Normative **texts are not shipped with the plugin**
(copyright/distribution — see `local/README.md`): verbatim excerpts live in
the untracked `references/local/` layer of each installation. A standard
listed here is NOT citable by clause unless a file under `local/` contains
its wording and that wording has been read in the current session — check
the "Local excerpts location" column against your installation.

Research date: 2026-08-30 (web verification of titles/status). Editions
marked *(unconfirmed)* were not independently verified — confirm before
relying on the edition year.

## Core documents

| Document | Scope | Status | Local excerpts location |
|---|---|---|---|
| **ДБН В.2.5-23:2025** «Проєктування електроустановок житлових будинків та громадських будівель і споруд» | Primary design code for dwellings | Approved by наказ Мінрозвитку 25.08.2025 № 1301; **effective 2026-01-01**; replaces ДБН В.2.5-23:2010; free official access via e-construction.gov.ua | `local/dbn-v2.5-23-2025/` |
| **ПУЕ** «Правила улаштування електроустановок» | General installation rules (incl. глава 1.7 заземлення) | Consolidated Ukrainian edition, наказ Міненерговугілля 21.07.2017 № 476; chapter-based revisions | `local/pue/` |
| **ДСТУ HD 60364-1:2022** | LV installations — fundamental principles | Adopted (HD 60364-1:2008 IDT) | none |
| **ДСТУ HD 60364-4-41:2022** | Protection against electric shock | Adopted (HD 60364-4-41:2017 IDT) | none |
| **ДСТУ HD 60364-4-43:2022** | Protection against overcurrent | Adopted (HD 60364-4-43:2010 IDT) | none |
| **ДСТУ HD 60364-5-52:2021** | Wiring systems (ampacity, methods) | Adopted (HD 60364-5-52:2011 IDT) | none |
| **ДСТУ HD 60364-5-53** | Switchgear/protective device selection (incl. SPD section) | *(edition unconfirmed — verify adoption/year)* | none |
| **ДСТУ HD 60364-5-54** | Earthing arrangements, PE conductors | *(edition unconfirmed — verify adoption/year)* | none |
| **ДСТУ HD 60364-6:2022** | Verification | Adopted (HD 60364-6:2016 IDT) | none |
| **ДСТУ HD 60364-7-701:2022** | Baths/showers — zones, IP, equipment | Adopted (HD 60364-7-701:2007 IDT; IEC 2006 MOD); listed in ДБН В.2.5-23:2025 розділ 2 | none |

## Supporting documents (all listed in ДБН В.2.5-23:2025 розділ 2 — list read from scan)

| Document | Why it matters here |
|---|---|
| ДСТУ ГОСТ 30331.11:2004 | Old bathroom standard (МЭК 364-7-701:1984) — **still referenced by ДБН alongside HD 60364-7-701:2022; potential conflict, surface it** |
| ДСТУ Б В.2.5-82:2016 | Electrical safety in buildings — protective measures against electric shock |
| ДБН В.2.5-24:2012 | Electric cable heating systems (underfloor heating) |
| ДБН В.2.5-56:2014 | Fire protection systems (supply to fire equipment) |
| ДСТУ 4809:2007 + ДСТУ EN 13501-6:2023 | Cable fire-performance classes (ДБН Додаток Ж maps them) |
| ДСТУ EN 60898-1:2019 | MCB product standard |
| ДСТУ EN 61008-1:2019 / 61009-1:2019 | RCCB / RCBO product standards |
| ДСТУ EN 50160:2023 | Voltage quality at supply terminals |
| ДСТУ 7308:2013 | Ввідно-розподільчі пристрої (input distribution devices) |
| ДСТУ 9222:2023 | Fire safety of EV charging (with ДБН Додаток И) |
| ДСТУ EN 62305 series | Lightning protection — context for SPD Type 1 decisions *(adoption status unconfirmed)* |
| НПАОП 40.1-1.32-01 | Electrical equipment of special installations |
| ПТЕЕС (наказ 25.07.2006 № 258) | Operation rules for consumer installations |

## Local excerpt files (ДБН В.2.5-23:2025)

Transcribed from an **unofficial scanned copy** (pozhezhni-systemy.org.ua
mirror; scan has no text layer). Each file header carries the provenance
caveat; `[?]`/`[нерозбірливо]` mark uncertain OCR. Known gaps:

- `04-06-supply-and-loads.md` — розділи 4, 5 (dwelling-relevant), 6.1 with
  tables 6.1–6.8 and formulas (1)–(11). Public-building content skipped.
- `07-08-internal-networks-protection.md` — розділи 7–8 in full (internal
  networks incl. 7.23–7.26 group lines/ПЗВ/ПВДП, 7.66–7.67 sockets/bathrooms,
  таблиці 7.1, 8.1) plus розділ 9 (ВРП/групові щитки placement).
- `13-16-annexes-d-e-i.md` — розділи 13, 14, 16, додатки Д (ПВДП/AFDD —
  **обов'язковий**), Е (wiring installation), Ж (cable classes), И (EV
  charging — **обов'язковий**). **Таблиця Д.1 is missing from the scan** —
  the list of buildings where AFDD is mandatory must be obtained from
  another copy before citing Д.3.6 applicability.

## Versioning and conflicts

- Effective-date rule: ДБН В.2.5-23:2025 governs designs started from
  2026-01-01; earlier projects may lawfully be under ДБН В.2.5-23:2010 —
  ask which regime applies before reviewing an existing design.
- ПУЕ predates and coexists with the ДСТУ HD 60364 adoptions; where their
  provisions diverge, quote both and record the conflict (iron rule 8) —
  do not silently prefer either.
- When adding new excerpt files, name them `<standard-dir>/<topic>.md`,
  reuse the provenance header format, and update this index.
