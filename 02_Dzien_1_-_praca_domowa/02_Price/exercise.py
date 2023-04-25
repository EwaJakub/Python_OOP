class Price:
    def __init__(self, value: float):
        self.value = round(float(value), 2)

    @classmethod
    def from_usd(cls, value_usd: float):
        value_pln = value_usd*3.8
        return cls(value_pln)

    @classmethod
    def from_eur(cls, value_eur: float):
        value_pln = value_eur*4.5
        return cls(value_pln)

    def __str__(self):
        return f"{self.value} PLN"


some_price = Price.from_usd(25)
some_other_price = Price.from_eur(80)
print(some_price)  # 95.0 PLN
print(some_other_price)  # 360.0 PLN
