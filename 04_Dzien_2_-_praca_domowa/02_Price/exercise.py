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

    def set_net(self, value):
        self._pretax = value * 1.23
        self._count()

    def set_pretax(self, value):
        self._pretax = value
        self._count()

    def set_tax(self, value):
        self._pretax = round((value * 1.23) / 0.23, 2)
        self._count()
