class Product:

    obj_list = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.obj_list.append(self.name)
        self.obj_id = Product.obj_list.index(self.name) + 1


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        self.products[product.obj_id] = product
        if product.obj_id in self.quantities:
            self.quantities[product.obj_id] = self.quantities[product.obj_id] + 1
        else:
            self.quantities[product.obj_id] = 1

    def remove_product(self, product):
        if product.obj_id in self.products:
            del self.products[product.obj_id]
            del self.quantities[product.obj_id]
        else:
            pass

    def change_product_quantity(self, product, new_quantity):
        if product.obj_id in self.products:
            if new_quantity == 0:
                del self.products[product.obj_id]
                del self.quantities[product.obj_id]
            if new_quantity < 0:
                raise ValueError("błędna ilość!")
            else:
                self.quantities[product.obj_id] = new_quantity


    def get_receipt(self):
        total_value = []
        for product in self.products.values():
            value = round(product.price * self.quantities[product.obj_id], 2)
            if self.quantities[product.obj_id] >= 3:
                total_value.append(value * 0.7)
                print(f"Rabat w wysokości {round(value - value*0.7, 2)}")
            else:
                total_value.append(value)
            print(f"{product.name}- "
                  f"amount: {self.quantities[product.obj_id]}, "
                  f"price: {product.price} zł, "
                  f"total: {value}zł")
        return f"Suma: {sum(total_value)}zł"



bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chive = Product('Chive', 1.50)
pepper = Product('Pepper', 2.35)
print(bread.obj_id)  # 1
print(pepper.obj_id)  # 5
print(pepper.name)  # 'Pepper'
print(pepper.price)  # 2.35

cart = ShoppingCart()
print(cart.products)   # {}
print(cart.quantities)  # {}
print(cart.get_receipt())  # Suma: 0zł

cart.add_product(bread)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(pepper)
cart.add_product(chive)
cart.change_product_quantity(pepper, 2)
print(cart.products)  # {1: <...Product object...>, 5: <...Product object...>, 4: <...Product object...>}
print(cart.quantities)  # {1: 3, 5: 2, 4: 1}
print(cart.get_receipt())
cart.remove_product(bread)
print(cart.get_receipt())
"""
Order MAY be different 
Pepper - amount: 2, price: 2.35zł, total: 4.7zł
Chive - amount: 1, price: 1.5zł, total: 1.5zł
Total: 6.2zł
"""