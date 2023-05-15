import unittest

import zadanie


class Price23VatTestCase(unittest.TestCase):
    def test_creating_instance(self):
        p = zadanie.Price(123)

    def test_reading(self):
        p = zadanie.Price(123)
        self.assertAlmostEqual(p.netto, 100)
        self.assertEqual(p.brutto, 123)
        self.assertAlmostEqual(p.tax, 23)

    def test_setting_netto(self):
        p = zadanie.Price(123)
        p.netto = 200
        self.assertEqual(p.netto, 200)
        self.assertAlmostEqual(p.brutto, 246)
        self.assertAlmostEqual(p.tax, 46)

    def test_setting_brutto(self):
        p = zadanie.Price(123)
        p.brutto = 246
        self.assertAlmostEqual(p.netto, 200)
        self.assertEqual(p.brutto, 246)
        self.assertAlmostEqual(p.tax, 46)

    def test_setting_tax(self):
        p = zadanie.Price(123)
        p.tax = 46
        self.assertAlmostEqual(p.netto, 200)
        self.assertAlmostEqual(p.brutto, 246)
        self.assertEqual(p.tax, 46)
