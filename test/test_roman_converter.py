import unittest 
from src.roman_converter import decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(decimal_to_roman(1), 'I')

    def test_cinco(self):
        self.assertEqual(decimal_to_roman(5), 'V')

    def test_nueve(self):
        self.assertEqual(decimal_to_roman(9), 'IX')

    def test_diez(self):
        self.assertEqual(decimal_to_roman(10), 'X')

    def test_cincuenta(self):
        self.assertEqual(decimal_to_roman(50), 'L')

    def test_cien(self):
        self.assertEqual(decimal_to_roman(100), 'C')

    def test_quinientos(self):
        self.assertEqual(decimal_to_roman(500), 'D')

    def test_mil(self):
        self.assertEqual(decimal_to_roman(1000), 'M')

if __name__ == '__main__':
    unittest.main()
