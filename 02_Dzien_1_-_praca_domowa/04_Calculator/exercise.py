class Calculator:

    def add_numbers(self, a, b):
        return a + b

    def sub_numbers(self, a, b):
        return a - b

    def mul_numbers(self, a, b):
        return a * b

    def div_numbers(self, a, b):
        return a / b


class LoggingCalculator(Calculator):
    def __init__(self):
        self.history = []

    def add_numbers(self, a, b):
        result = super().add_numbers(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub_numbers(self, a, b):
        result = super().sub_numbers(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def mul_numbers(self, a, b):
        result = super().mul_numbers(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def div_numbers(self, a, b):
        result = super().div_numbers(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result


calc = LoggingCalculator()
print(calc.add_numbers(2, 3))
print(calc.mul_numbers(3, 3))
print(calc.sub_numbers(7, 4))
print(calc.div_numbers(5, 2))
print(calc.history)