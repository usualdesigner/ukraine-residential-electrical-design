# Panel (щиток) design

Layout order and content per `templates/panel-schedule.md`. Method:

1. **Device list** — from the finished circuit schedule: incoming
   switch/breaker, SPD (if justified), voltage monitoring relay (if used),
   contactors (if used, e.g. for load shedding / night tariff), RCDs, RCBOs,
   MCBs, AFDDs (Додаток Д check).
2. **Module widths** — from manufacturer data only (`references/local/manufacturers/`
   or user input): 1P MCB = 1 module, 1P+N RCBO = 1 or 2 modules depending
   on series, 2P RCD = 2, 4P = 4, SPD 1P+N = 2 … Do not guess a specific
   product's width; unknown series → use generic counts and label ASSUMPTION.
3. **Count** — `elec_calc.py modules devices.json --reserve-percent 20`.
   20 % spare is ENGINEERING RECOMMENDATION (check excerpts for any
   normative reserve requirement before citing one); round up to the next
   standard enclosure (12/18/24/36/48/54/72 modules — market sizes, COMMON
   INDUSTRY PRACTICE).
4. **Physical arrangement** — group each RCD with its MCBs on one row where
   possible; N bus per RCD group adjacent; keep SPD connection short
   (rules/surge-protection.md); PE and N terminal counts ≥ conductor counts.
5. **Labelling** — every position labelled with circuit name in the schedule
   and on the panel legend.
6. **Selectivity note** — incoming breaker vs branch breakers: full
   selectivity often unattainable with domestic MCBs; state the situation
   honestly rather than claiming selectivity.

Output: panel schedule table + text single-line diagram + module JSON.
