class BankAccount:

    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount
            return f'Deposit_cash {amount}'
        elif amount <= 0:
            return "Incorrect value"

    def withdraw_cash(self, amount):
        if self.cash >= amount:
            self.cash -= amount
            return amount
        elif amount > self.cash:
            amount = self.cash
            self.cash = 0.0
            return amount
        else:
            return "Incorrect value"

    def print_info(self):
        return f"Account number {self.number}: {self.cash}"


c = BankAccount(2192030912)
print(c.deposit_cash(300))
print(c.print_info())
print(c.withdraw_cash(100))
print(c.print_info())
print(c.withdraw_cash(30))
print(c.print_info())
print(c.deposit_cash(5000))
print(c.print_info())
print(c.withdraw_cash(60000))
print(c.print_info())
print(c.deposit_cash(10000000))
print(c.print_info())
print(c.deposit_cash(-10000))
print(c.print_info())
