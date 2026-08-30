#!/usr/bin/env python3
"""Unit tests: python3 scripts/test_elec_calc.py"""
import math
import unittest

from elec_calc import (aggregate_loads, balance_phases, count_modules,
                       current, voltage_drop)


class TestCurrent(unittest.TestCase):
    def test_single_phase(self):
        # 2300 W at 230 V, cos phi 1 -> 10 A
        self.assertAlmostEqual(current(2300, 230), 10.0)

    def test_single_phase_cos_phi(self):
        self.assertAlmostEqual(current(2300, 230, cos_phi=0.8), 12.5)

    def test_three_phase(self):
        # 11085 W at 400 V L-L, cos phi 1 -> ~16 A
        self.assertAlmostEqual(current(11085, 400, three_phase=True), 16.0, places=1)

    def test_rejects_bad_input(self):
        for kw in ({"power_w": -1, "voltage_v": 230},
                   {"power_w": 100, "voltage_v": 0},
                   {"power_w": 100, "voltage_v": 230, "cos_phi": 1.2}):
            with self.assertRaises(ValueError):
                current(**kw)


class TestVoltageDrop(unittest.TestCase):
    def test_single_phase_copper(self):
        # dU = 2 * 0.0175 * 20 * 10 / 1.5 = 4.6667 V -> 2.029 % of 230
        r = voltage_drop(10, 20, 1.5)
        self.assertAlmostEqual(r["drop_v"], 4.6667, places=3)
        self.assertAlmostEqual(r["drop_percent"], 2.0290, places=3)

    def test_three_phase(self):
        r = voltage_drop(16, 30, 4, three_phase=True, voltage_v=400)
        expected = math.sqrt(3) * 0.0175 * 30 * 16 / 4
        self.assertAlmostEqual(r["drop_v"], expected)
        self.assertAlmostEqual(r["drop_percent"], expected / 400 * 100)

    def test_aluminium_and_rho_override(self):
        self.assertGreater(voltage_drop(10, 20, 2.5, material="al")["drop_v"],
                           voltage_drop(10, 20, 2.5, material="cu")["drop_v"])
        r = voltage_drop(10, 20, 2.5, rho=0.02)
        self.assertAlmostEqual(r["drop_v"], 2 * 0.02 * 20 * 10 / 2.5)

    def test_rejects_zero_section(self):
        with self.assertRaises(ValueError):
            voltage_drop(10, 20, 0)


class TestAggregateLoads(unittest.TestCase):
    def test_installed_vs_demand(self):
        r = aggregate_loads([{"name": "a", "power_w": 2000, "k": 0.5},
                             {"name": "b", "power_w": 1000}])
        self.assertEqual(r["installed_w"], 3000)
        self.assertEqual(r["demand_w"], 2000)

    def test_rejects_bad_k(self):
        with self.assertRaises(ValueError):
            aggregate_loads([{"name": "a", "power_w": 100, "k": 1.5}])


class TestBalancePhases(unittest.TestCase):
    def test_deterministic_greedy(self):
        loads = [{"name": "oven", "power_w": 3000},
                 {"name": "boiler", "power_w": 2000},
                 {"name": "washer", "power_w": 2000},
                 {"name": "sockets", "power_w": 1000}]
        r = balance_phases(loads)
        # oven->L1, boiler->L2, washer->L3, sockets-> tie L2/L3 -> L2 (phase order)
        self.assertEqual(r["phase_totals_w"], {"L1": 3000.0, "L2": 3000.0, "L3": 2000.0})
        # run twice -> identical (determinism)
        self.assertEqual(r, balance_phases(loads))

    def test_fixed_phase_honoured(self):
        r = balance_phases([{"name": "ac", "power_w": 2000, "phase": "L2"},
                            {"name": "x", "power_w": 500}])
        byname = {a["name"]: a for a in r["assignment"]}
        self.assertEqual(byname["ac"]["phase"], "L2")
        self.assertEqual(byname["x"]["phase"], "L1")  # least loaded, first in order

    def test_imbalance_percent(self):
        r = balance_phases([{"name": "a", "power_w": 1000, "phase": "L1"}])
        self.assertAlmostEqual(r["imbalance_percent"], 100.0)

    def test_unknown_phase_rejected(self):
        with self.assertRaises(ValueError):
            balance_phases([{"name": "a", "power_w": 1, "phase": "L9"}])


class TestCountModules(unittest.TestCase):
    def test_reserve_rounds_up(self):
        r = count_modules([{"name": "main", "modules": 2},
                           {"name": "rcbo", "modules": 10}], reserve_percent=20)
        self.assertEqual(r["modules_used"], 12)
        self.assertEqual(r["modules_required"], 15)  # 14.4 -> ceil

    def test_no_reserve(self):
        self.assertEqual(count_modules([{"name": "a", "modules": 1}])["modules_required"], 1)

    def test_rejects_negative_reserve(self):
        with self.assertRaises(ValueError):
            count_modules([{"name": "a", "modules": 1}], reserve_percent=-5)


class TestBalanceValidation(unittest.TestCase):
    def test_rejects_negative_power(self):
        with self.assertRaises(ValueError):
            balance_phases([{"name": "a", "power_w": -100}])


if __name__ == "__main__":
    unittest.main()
