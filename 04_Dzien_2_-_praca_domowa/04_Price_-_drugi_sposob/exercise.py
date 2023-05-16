class Price23Vat:
    def __init__(self, gross_value):
        self._pretax = gross_value
        self._net = round(gross_value / 1.23, 2)
        self._tax = self._pretax - self._net
        self._count()

    def _count(self):
        self._net = round(self._pretax / 1.23, 2)
        self._tax = self._pretax - self._net

    def get_net(self):
        return self._net

    def get_pretax(self):
        return self._pretax

    def get_tax(self):
        return self._tax

    @property
    def net(self):
        return self.get_net()

    @property
    def pretax(self):
        return self.get_pretax()

    @property
    def tax(self):
        return self.get_tax()

    @net.setter
    def net(self, value):
        self._pretax = value * 1.23
        self._count()

    @pretax.setter
    def pretax(self, value):
        self._pretax = value
        self._count()

    @tax.setter
    def tax(self, value):
        self._pretax = round((value * 1.23) / 0.23, 2)
        self._count()


price = Price23Vat(123)
print(price.pretax)        # 123
print(price.tax)           # 23
print(price.net)           # 100
price.tax = 69
print(price.pretax)        # 369
print(price.tax)           # 69
print(price.net)           # 300
