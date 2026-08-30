# Cable selection

Decision chain per circuit — each step keeps its own status label:

1. **Design current Ib** — `elec_calc.py current` from demand load.
2. **Conductor material** — copper for apartment interior wiring. Check
   `references/local/dbn-v2.5-23-2025/` for the current normative statement on
   conductor material and minimum sections in dwellings; if found, cite it
   (VERIFIED), otherwise label the copper choice ENGINEERING RECOMMENDATION.
3. **Insulation / fire behaviour** — cable fire-performance class per
   ДСТУ 4809 / ДСТУ EN 13501-6 mapping (see ДБН В.2.5-23:2025 Додаток Ж
   excerpt if present). Typical Ukrainian choice ВВГнг(д)-LS is COMMON
   INDUSTRY PRACTICE unless a verified clause mandates a class for the case.
4. **Minimum cross-section** — only from a verified table (ДБН розділ 8 /
   ДСТУ HD 60364-5-52). No verified table → propose a section as
   ENGINEERING RECOMMENDATION with the calculation shown, and add an
   UNRESOLVED item to confirm against the normative minimum.
5. **Ampacity Iz** — depends on installation method, ambient temperature,
   grouping. **All three are inputs — never assumed.** Missing → the
   Ib ≤ In ≤ Iz check is UNRESOLVED (needs: installation method /
   grouping / ambient). Ampacity values come from verified tables
   (ДСТУ HD 60364-5-52) or manufacturer data (label MANUFACTURER REQUIREMENT).
6. **Voltage drop** — `elec_calc.py vdrop` with the actual route length
   (never assumed). Compare only against a limit whose wording was verified;
   otherwise report the % and mark the limit comparison UNRESOLVED.
7. **Protective conductor** — PE section per verified rule
   (ДСТУ HD 60364-5-54); ordinary apartment cables carry PE of the same
   section as phase up to 16 mm² — verify before citing.
8. **Short-circuit withstand** — only if prospective fault current is known;
   otherwise UNRESOLVED (needs: Ik at the panel).

Never assume: installation method, route length, ambient temperature,
grouping factor, existing riser cable, aluminium legacy wiring condition.
