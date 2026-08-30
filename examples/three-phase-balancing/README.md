# EXAMPLE — three-phase load balancing

Fixture for the deterministic phase balancer. A true 3-phase load (hob)
is entered as three fixed per-phase thirds; single-phase loads are left
free for the greedy assignment.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/elec_calc.py" balance loads.json
```

Expected result (deterministic): fixed loads honoured; free loads sorted
by power desc (name asc tiebreak), each assigned to the least-loaded phase;
totals `L1: 5000 W, L2: 5300 W, L3: 4800 W`, imbalance ≈ 9.43 %.

These loads are illustrative only — they carry no defaults for real
projects and do not represent a recommended apartment configuration.
