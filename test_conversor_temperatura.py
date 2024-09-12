import coverage
import unittest
from conversor_temperatura import ConversorTemperatura

class TestConversorTemperatura(unittest.TestCase):

    def setUp(self):
        self.conversor = ConversorTemperatura()

    def test_celsius_para_fahrenheit(self):
        self.assertAlmostEqual(self.conversor.celsius_para_fahrenheit(0), 32)
        self.assertAlmostEqual(self.conversor.celsius_para_fahrenheit(100), 212)

    def test_fahrenheit_para_celsius(self):
        self.assertAlmostEqual(self.conversor.fahrenheit_para_celsius(32), 0)
        self.assertAlmostEqual(self.conversor.fahrenheit_para_celsius(212), 100)

    def test_celsius_para_kelvin(self):
        self.assertAlmostEqual(self.conversor.celsius_para_kelvin(0), 273.15)
        self.assertAlmostEqual(self.conversor.celsius_para_kelvin(100), 373.15)

if __name__ == '__main__':
    unittest.main()