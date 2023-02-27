class Calculator:

    def __init__(self):
        self.methods_list = []

    def __str__(self):
        return f'{self.methods_list}'

    def add(self, num1, num2):
        result = num1 + num2
        self.methods_list.append(f'added {num1} to {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.methods_list.append(f'multiplied {num1} to {num2} got {result}')
        return result

    def print_operations(self):
        return self.methods_list


cal = Calculator()  # init doesn't have args
print(cal.add(3, 4))  # 7
print(cal.add(3, 3))  # 6
print(cal.multiply(3, 3))  # 9
print(cal.multiply(3, 2))  # 6
print(cal)
print(cal.print_operations())
