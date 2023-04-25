import unittest

import exercise


class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(exercise.Calculator().add_numbers(2, 3), 5)
        self.assertEqual(exercise.Calculator().add_numbers(4, 6), 10)

    def test_sub(self):
        self.assertEqual(exercise.Calculator().sub_numbers(6, 4), 2)
        self.assertEqual(exercise.Calculator().sub_numbers(12, 8), 4)

    def test_mul(self):
        self.assertEqual(exercise.Calculator().mul_numbers(2, 3), 6)
        self.assertEqual(exercise.Calculator().mul_numbers(4, 6), 24)

    def test_div(self):
        self.assertEqual(exercise.Calculator().div_numbers(12, 3), 4)
        self.assertEqual(exercise.Calculator().div_numbers(24, 2), 12)


class LoggingCalculatorTestCase(unittest.TestCase):
    def test_add(self):
        lc = exercise.LoggingCalculator()
        self.assertEqual(lc.add_numbers(2, 3), 5)
        self.assertEqual(lc.add_numbers(4, 6), 10)
        self.assertEqual(lc.history[0], '2 + 3 = 5')
        self.assertEqual(lc.history[1], '4 + 6 = 10')

    def test_sub(self):
        lc = exercise.LoggingCalculator()
        self.assertEqual(lc.sub_numbers(6, 4), 2)
        self.assertEqual(lc.sub_numbers(12, 8), 4)
        self.assertEqual(lc.history[0], '6 - 4 = 2')
        self.assertEqual(lc.history[1], '12 - 8 = 4')

    def test_mul(self):
        lc = exercise.LoggingCalculator()
        self.assertEqual(lc.mul_numbers(2, 3), 6)
        self.assertEqual(lc.mul_numbers(4, 6), 24)
        self.assertEqual(lc.history[0], '2 * 3 = 6')
        self.assertEqual(lc.history[1], '4 * 6 = 24')

    def test_div(self):
        lc = exercise.LoggingCalculator()
        self.assertEqual(lc.div_numbers(12, 3), 4)
        self.assertEqual(lc.div_numbers(24, 2), 12)
        self.assertEqual(lc.history[0], '12 / 3 = 4.0')
        self.assertEqual(lc.history[1], '24 / 2 = 12.0')
