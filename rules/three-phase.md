# Three-phase supplies and phase balancing

Only applicable when `supply.phases: 3` is stated — never inferred from
allocated power.

1. **Identify fixed-phase constraints**: true 3-phase loads (hob/oven in
   3N~ mode, some HVAC, EV chargers per manufacturer docs), and any loads
   the user has already pinned to a phase.
2. **Balance deterministically**: `elec_calc.py balance` — greedy
   assignment, fixed phases honoured, reproducible output. Feed it circuit
   demand loads (not installed watts) so simultaneity is reflected.
3. **Report imbalance %** and per-phase totals. There is no verified
   local normative imbalance limit unless present in the excerpts — report
   the number, flag large unavoidable single-phase loads (e.g. a 7 kW
   single-phase EV charger dominates a phase; alternatives: 3-phase
   appliance version, load management).
4. **Simultaneity caveat**: balancing on averages can still leave momentary
   imbalance; note which large loads coincide (e.g. hob + oven at dinner).
5. **Per-phase breaker/cable checks** run per phase with that phase's
   current, not the average.
6. **Neutral**: unbalanced 3-phase means working neutral current — never
   undersize N; distortion-heavy loads increase it. Voltage monitoring
   relay per phase is common practice for обрив нуля exposure
   (see rules/surge-protection.md).
