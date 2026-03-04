import unittest
from converter import Converter

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.conv = Converter()

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.conv.celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(self.conv.celsius_to_fahrenheit(100), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.conv.fahrenheit_to_celsius(32), 0.0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(self.conv.celsius_to_kelvin(0), 273.15)

    def test_km_to_miles(self):
        self.assertAlmostEqual(self.conv.km_to_miles(1), 0.621371)

    def test_kg_to_pounds(self):
        self.assertAlmostEqual(self.conv.kg_to_pounds(1), 2.20462)

if __name__ == "__main__":
    unittest.main()
