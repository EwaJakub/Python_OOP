from math import sqrt


class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"

    def describe(self):
        return f"kolor: {self.color}, środek w punkcie {self.x}, {self.y}"

    def distance(self, obj):
        a = obj.x - self.x
        b = obj.y - self.y
        return sqrt(a**2 + b**2)  # albo (a**2 + b**2)**0.5


shape1 = Shape(2, 3, 'red')
shape2 = Shape(3, 7, 'blue')
print(shape1)
print(shape1.describe())
print(shape1.distance(shape2))
