#!/usr/bin/env python3
"""Deterministic electrical calculations for apartment design.

Pure arithmetic only. No normative limits are hard-coded: permissible
voltage drop, demand coefficients, cable ampacities etc. must be supplied
by the caller from verified sources — this module only computes.

Physics constants (not normative):
  resistivity at 20 C, ohm*mm^2/m: Cu 0.0175, Al 0.028
Conductor reactance is neglected (acceptable for S <= 50 mm^2 apartment
wiring; state this assumption in output documents).

Usage: elec_calc.py <command> [options]   (see --help per command)
All commands print JSON to stdout. Inputs echo back in the result so the
assumptions stay visible.
"""
import argparse
import json
import math
import sys

RESISTIVITY = {"cu": 0.0175, "al": 0.028}  # ohm*mm^2/m at 20 C


def current(power_w, voltage_v, cos_phi=1.0, three_phase=False):
    """Design current, A. voltage_v is L-N for 1-ph, L-L for 3-ph balanced."""
    if power_w < 0 or voltage_v <= 0 or not 0 < cos_phi <= 1:
        raise ValueError("power_w >= 0, voltage_v > 0, 0 < cos_phi <= 1 required")
    div = voltage_v * cos_phi * (math.sqrt(3) if three_phase else 1)
    return power_w / div


def voltage_drop(current_a, length_m, section_mm2, material="cu",
                 cos_phi=1.0, voltage_v=230.0, three_phase=False, rho=None):
    """Voltage drop along a radial line, volts and percent.

    length_m is the one-way route length; the two-way path for single
    phase (factor 2) and sqrt(3) for three phase are applied here.
    """
    if rho is None:
        rho = RESISTIVITY[material]
    if current_a < 0 or length_m < 0 or section_mm2 <= 0 or voltage_v <= 0:
        raise ValueError("non-negative I/L, positive S/U required")
    k = math.sqrt(3) if three_phase else 2.0
    dv = k * rho * length_m * current_a * cos_phi / section_mm2
    return {"drop_v": dv, "drop_percent": dv / voltage_v * 100.0}


def aggregate_loads(loads):
    """loads: [{name, power_w, k?}] where k = simultaneity/demand factor
    (default 1.0, i.e. no reduction unless the caller justifies one)."""
    installed = sum(l["power_w"] for l in loads)
    demand = sum(l["power_w"] * l.get("k", 1.0) for l in loads)
    for l in loads:
        if l["power_w"] < 0 or not 0 <= l.get("k", 1.0) <= 1:
            raise ValueError(f"bad load {l.get('name')}: power_w >= 0, 0 <= k <= 1")
    return {"installed_w": installed, "demand_w": demand}


def balance_phases(loads, phases=("L1", "L2", "L3")):
    """Deterministic greedy phase assignment.

    loads: [{name, power_w, phase?}]; a preset "phase" is honoured
    (fixed single-phase loads, or thirds of a 3-ph load entered per phase).
    Unassigned loads are sorted by power desc (name asc as tiebreak) and
    each goes to the currently least-loaded phase (first by phase order).
    """
    totals = {p: 0.0 for p in phases}
    result = []
    for l in loads:
        if l["power_w"] < 0:
            raise ValueError(f"negative power on {l.get('name')}")
    fixed = [l for l in loads if l.get("phase")]
    free = sorted((l for l in loads if not l.get("phase")),
                  key=lambda l: (-l["power_w"], l["name"]))
    for l in fixed:
        if l["phase"] not in totals:
            raise ValueError(f"unknown phase {l['phase']} on {l['name']}")
        totals[l["phase"]] += l["power_w"]
        result.append({"name": l["name"], "power_w": l["power_w"],
                       "phase": l["phase"], "fixed": True})
    for l in free:
        p = min(phases, key=lambda ph: (totals[ph], phases.index(ph)))
        totals[p] += l["power_w"]
        result.append({"name": l["name"], "power_w": l["power_w"],
                       "phase": p, "fixed": False})
    hi, lo = max(totals.values()), min(totals.values())
    imbalance = 0.0 if hi == 0 else (hi - lo) / hi * 100.0
    return {"assignment": result, "phase_totals_w": totals,
            "imbalance_percent": imbalance}


def count_modules(devices, reserve_percent=0.0):
    """devices: [{name, modules}]; reserve on top of used modules."""
    used = sum(d["modules"] for d in devices)
    if any(d["modules"] < 0 for d in devices) or reserve_percent < 0:
        raise ValueError("modules and reserve_percent must be >= 0")
    with_reserve = math.ceil(used * (1 + reserve_percent / 100.0))
    return {"modules_used": used, "reserve_percent": reserve_percent,
            "modules_required": with_reserve}


def _read_json(path):
    with (sys.stdin if path == "-" else open(path)) as f:
        return json.load(f)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("current", help="design current from power")
    c.add_argument("--power-w", type=float, required=True)
    c.add_argument("--voltage-v", type=float, required=True,
                   help="L-N for single phase (e.g. 230), L-L for three phase (e.g. 400)")
    c.add_argument("--cos-phi", type=float, default=1.0)
    c.add_argument("--three-phase", action="store_true")

    v = sub.add_parser("vdrop", help="voltage drop on a radial line")
    v.add_argument("--current-a", type=float, required=True)
    v.add_argument("--length-m", type=float, required=True, help="one-way route length")
    v.add_argument("--section-mm2", type=float, required=True)
    v.add_argument("--material", choices=RESISTIVITY, default="cu")
    v.add_argument("--cos-phi", type=float, default=1.0)
    v.add_argument("--voltage-v", type=float, default=230.0)
    v.add_argument("--three-phase", action="store_true")
    v.add_argument("--rho", type=float, help="override resistivity, ohm*mm^2/m")
    v.add_argument("--limit-percent", type=float,
                   help="compare against a limit YOU obtained from a verified source")

    for name, hlp in [("loads", "aggregate installed/demand load"),
                      ("balance", "greedy 3-phase balancing"),
                      ("modules", "DIN module count with reserve")]:
        p = sub.add_parser(name, help=hlp)
        p.add_argument("input", help="JSON file or - for stdin")
        if name == "modules":
            p.add_argument("--reserve-percent", type=float, default=0.0)

    a = ap.parse_args(argv)
    if a.cmd == "current":
        out = {"inputs": {"power_w": a.power_w, "voltage_v": a.voltage_v,
                          "cos_phi": a.cos_phi, "three_phase": a.three_phase},
               "current_a": current(a.power_w, a.voltage_v, a.cos_phi, a.three_phase)}
    elif a.cmd == "vdrop":
        r = voltage_drop(a.current_a, a.length_m, a.section_mm2, a.material,
                         a.cos_phi, a.voltage_v, a.three_phase, a.rho)
        out = {"inputs": {"current_a": a.current_a, "length_m": a.length_m,
                          "section_mm2": a.section_mm2, "material": a.material,
                          "cos_phi": a.cos_phi, "voltage_v": a.voltage_v,
                          "three_phase": a.three_phase,
                          "rho": a.rho or RESISTIVITY[a.material]},
               "assumption": "conductor reactance neglected; resistivity at 20 C",
               **r}
        if a.limit_percent is not None:
            out["limit_percent"] = a.limit_percent
            out["within_limit"] = r["drop_percent"] <= a.limit_percent
    elif a.cmd == "loads":
        out = aggregate_loads(_read_json(a.input))
    elif a.cmd == "balance":
        out = balance_phases(_read_json(a.input))
    elif a.cmd == "modules":
        out = count_modules(_read_json(a.input), a.reserve_percent)
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
