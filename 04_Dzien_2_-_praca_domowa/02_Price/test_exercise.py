import unittest

import exercise


class Price23VatTestCase(unittest.TestCase):
    def test_creating_instance(self):
        p = exercise.Price(123)

    def test_reading(self):
        p = exercise.Price(123)
        self.assertAlmostEqual(p.get_netto(), 100)
        self.assertEqual(p.get_brutto(), 123)
        self.assertAlmostEqual(p.get_tax(), 23)

    def test_setting_netto(self):
        p = exercise.Price(123)
        p.set_netto(200)
        self.assertEqual(p.get_netto(), 200)
        self.assertAlmostEqual(p.get_brutto(), 246)
        self.assertAlmostEqual(p.get_tax(), 46)

    def test_setting_brutto(self):
        p = exercise.Price(123)
        p.set_brutto(246)
        self.assertAlmostEqual(p.get_netto(), 200)
        self.assertEqual(p.get_brutto(), 246)
        self.assertAlmostEqual(p.get_tax(), 46)

    def test_setting_tax(self):
        p = exercise.Price(123)
        p.set_tax(46)
        self.assertAlmostEqual(p.get_netto(), 200)
        self.assertAlmostEqual(p.get_brutto(), 246)
        self.assertEqual(p.get_tax(), 46)
