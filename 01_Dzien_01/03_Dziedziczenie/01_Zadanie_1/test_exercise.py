import unittest

import exercise


class CartTestCase(unittest.TestCase):
    def test_instance_has_products_attribute(self):
        c = exercise.Cart()
        self.assertCountEqual(c.products, [])

    def test_adding_product(self):
        c = exercise.Cart()
        c.add('Potato', 10)
        self.assertCountEqual(c.products, [('Potato', 10)])
        c.add('Tomato', 30)
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30)])

    def test_summary(self):
        c = exercise.Cart()
        c.add('Potato', 10)
        c.add('Tomato', 30)
        self.assertCountEqual(c.summary(), [('Potato', 10), ('Tomato', 30)])

    def test_summary_does_not_modify_original_list(self):
        c = exercise.Cart()
        c.add('Potato', 10)
        c.add('Tomato', 30)
        c.summary()
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30)])


class Discount20PercentCartTestCase(unittest.TestCase):
    def test_instance_has_products_attribute(self):
        c = exercise.Discount20PercentCart()
        self.assertCountEqual(c.products, [])

    def test_adding_product(self):
        c = exercise.Discount20PercentCart()
        c.add('Potato', 10)
        self.assertCountEqual(c.products, [('Potato', 10)])
        c.add('Tomato', 30)
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30)])

    def test_summary(self):
        c = exercise.Discount20PercentCart()
        c.add('Potato', 10)
        c.add('Tomato', 30)
        self.assertCountEqual(c.summary(), [('Potato', 8), ('Tomato', 24)])

    def test_summary_does_not_modify_original_list(self):
        c = exercise.Discount20PercentCart()
        c.add('Potato', 10)
        c.add('Tomato', 30)
        c.summary()
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30)])


class Above3ProductsCheapestFreeCartTestCase(unittest.TestCase):
    def test_instance_has_products_attribute(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        self.assertCountEqual(c.products, [])

    def test_adding_product(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        c.add('Potato', 10)
        self.assertCountEqual(c.products, [('Potato', 10)])
        c.add('Tomato', 30)
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30)])
        c.add('Beer', 50)
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30), ('Beer', 50)])

    def test_summary(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        c.add('Potato', 10)
        c.add('Tomato', 30)
        c.add('Beer', 50)
        self.assertCountEqual(c.summary(), [('Potato', 10), ('Tomato', 30), ('Beer', 50)])
        c.add('Bread', 15)
        self.assertCountEqual(c.summary(), [('Potato', 0), ('Tomato', 30), ('Beer', 50), ('Bread', 15)])

    def test_summary_does_not_modify_original_list(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        c.add('Potato', 10)
        c.add('Beer', 50)
        c.add('Tomato', 30)
        c.add('Bread', 15)
        c.summary()
        self.assertCountEqual(c.products, [('Potato', 10), ('Tomato', 30), ('Beer', 50), ('Bread', 15)])
