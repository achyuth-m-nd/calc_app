import unittest
from advanced_calculator import AdvancedCalculator

class TestAdvancedCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = AdvancedCalculator()

    def test_power(self):
        self.assertEqual(self.calc.power(2, 10), 1024)

    def test_square_root(self):
        self.assertAlmostEqual(self.calc.square_root(9), 3.0)

    def test_square_root_negative(self):
        self.assertIsNone(self.calc.square_root(-4))

    def test_log(self):
        self.assertAlmostEqual(self.calc.log(100), 2.0)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(self.calc.factorial(0), 1)

    def test_factorial_negative(self):
        self.assertIsNone(self.calc.factorial(-3))

    def test_is_prime(self):
        self.assertTrue(self.calc.is_prime(7))
        self.assertFalse(self.calc.is_prime(9))
        self.assertFalse(self.calc.is_prime(1))

if __name__ == "__main__":
    unittest.main()
