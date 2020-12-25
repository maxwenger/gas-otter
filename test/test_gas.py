import unittest
import gas_otter
from gas_otter.gas import Gas


class TestGas(unittest.TestCase):
    def test_gas_not_equal_to_one(self):
        self.assertRaises(ValueError, Gas, 0, 0, 0)
        self.assertRaises(ValueError, Gas, 0.5, 0, 0)
        self.assertRaises(ValueError, Gas, 0, 0.5, 0)
        self.assertRaises(ValueError, Gas, 0, 0, 0.5)
        self.assertRaises(ValueError, Gas, 0.25, 0.25, 0.25)
        self.assertRaises(ValueError, Gas, 0.75, 0.25, 0.25)

    def test_gas_without_oxygen(self):
        self.assertRaises(ValueError, Gas, 0, 0.5, 0.5)

    def test_valid_nitrox(self):
        f_o2 = 0.7
        f_n = 0.2
        f_he = 0.1
        gas = Gas(f_o2, f_n, f_he)

        self.assertEqual(gas.o2, f_o2)
        self.assertEqual(gas.n, f_n)
        self.assertEqual(gas.he, f_he)


    def test_pressure_at_ppo2(self):
        gas = Gas(0.21, 0.79, 0)

        self.assertAlmostEqual(gas.pressure_at_ppo2(1.4), 6.66666666)
        self.assertAlmostEqual(gas.pressure_at_ppo2(1.6), 7.61904761)
