import unittest
from WindPowerSimulation.Simulation import GetPower

class MyTestCase(unittest.TestCase):
    def test_postive(self):
        self.assertAlmostEqual(0, GetPower(0,0))
        self.assertAlmostEqual(0, GetPower(1, 0))
        self.assertAlmostEqual(2, GetPower(3, 0))
        self.assertAlmostEqual(4, GetPower(5, 0))
        self.assertAlmostEqual(4, GetPower(10, 0))
    def test_negative(self):
        with self.assertRaises(ValueError):
            GetPower(-1,0)
        with self.assertRaises(ValueError):
            GetPower('nice',0)
        with self.assertRaises(ValueError):
            GetPower(100, 0)

if __name__ == '__main__':
    unittest.main()
