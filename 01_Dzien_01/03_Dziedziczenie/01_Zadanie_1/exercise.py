class Cart:
    def __init__(self):
        self.products = []

    def add(self, product_name: str, price: float):
        self.products.append((product_name, price))
        return self.products

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):
    # def __init__(self):  # wywołanie metody __init__ nie jest w tym przypadku potrzebne, z automatu jest dziedziczona
    #     super().__init__()

    # def add(self, product_name: str, price: float):
    #     super().add(product_name, price)

    def summary(self):
        products_before_discount = super().summary()
        products_after_discount = []
        for el in products_before_discount:
            products_after_discount.append((el[0], el[1] * 0.8))
        return products_after_discount


class Above3ProductsCheapestFreeCart(Cart):
    # def __init__(self):
    #     super().__init__()

    # def add(self, product_name: str, price: float):
    #     super().add(product_name, price)

    def summary(self):
        def take_second(elem):
            return elem[1]
        if len(self.products) > 3:
            sort_product_list = sorted(self.products, key=take_second)
            sort_product_list[0] = (sort_product_list[0][0], 0)
            return sort_product_list
        else:
            return self.products
