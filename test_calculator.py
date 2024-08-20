import unittest
from calculator import CalculatorApp

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorApp(None)  # We pass None as the root for testing

    def test_addition(self):
        self.calc.entry.insert(0, "2+3")
        self.calc.click_event("=")
        self.assertEqual(self.calc.entry.get(), "5")

    def test_subtraction(self):
        self.calc.entry.insert(0, "5-2")
        self.calc.click_event("=")
        self.assertEqual(self.calc.entry.get(), "3")

    def test_multiplication(self):
        self.calc.entry.insert(0, "4*3")
        self.calc.click_event("=")
        self.assertEqual(self.calc.entry.get(), "12")

    def test_division(self):
        self.calc.entry.insert(0, "10/2")
        self.calc.click_event("=")
        self.assertEqual(self.calc.entry.get(), "5.0")

    def test_clear(self):
        self.calc.entry.insert(0, "12345")
        self.calc.clear_entry()
        self.assertEqual(self.calc.entry.get(), "")

if __name__ == "__main__":
    unittest.main()
