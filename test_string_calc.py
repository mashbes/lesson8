import unittest
import string_calc


class StringCalcTest(unittest.TestCase):
    def test_empty_string(self):
        test_data = ''
        correct_data = 0
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_one_number(self):
        test_data = '7'
        correct_data = 7
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_sum_two_numbers_comma(self):
        test_data = '7,3'
        correct_data = 10
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_sum_two_numbers_new_line(self):
        test_data = '1\n2'
        correct_data = 3
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_sum_three_numbers_comma_new_line(self):
        test_data = '1\n2, 3\n4'
        correct_data = 10
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_negative_numbers(self):
        test_data = '-10,7,-17'
        correct_data = 'negative numbers are forbidden:-10,-17'
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_big_numbers(self):
        test_data = '30\n10, 1500\n2'
        correct_data = 42
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_new_one_separator(self):
        test_data = '//#\n1#2'
        correct_data = 3
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)

    def test_new_several_separators(self):
        test_data = '//###\n2###3'
        correct_data = 5
        obj = string_calc.StringCalculator()
        self.assertEqual(obj.add(test_data), correct_data)





