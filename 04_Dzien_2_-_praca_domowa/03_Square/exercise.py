class Square:
    def __init__(self, side):
        self._side = side
        self._count()  # podkreślenie w tym przypadku jest istotne, inaczej dostajemy błędy atrybutów

    def _count(self):
        self._perimeter = self._side * 4
        self._area = self._side ** 2
        self._diagonal = self._side * (2 ** 0.5)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    @property
    def side(self):
        return self.get_side()

    @property
    def perimeter(self):
        return self.get_perimeter()

    @property
    def area(self):
        return self.get_area()

    @property
    def diagonal(self):
        return self.get_diagonal()

    @side.setter
    def side(self, new_length):
        self._side = new_length
        self._count()

    @perimeter.setter
    def perimeter(self, new_length):
        self._side = new_length / 4
        self._count()

    @area.setter
    def area(self, new_area):
        self._side = new_area ** 0.5
        self._count()

    @diagonal.setter
    def diagonal(self, new_length):
        self._side = new_length / (2 ** 0.5)
        self._count()


square = Square(11)
print(square.get_side())  # 11
print(square.side)        # 11
print(square.perimeter)   # 44
square.perimeter = 48
print(square.get_side())  # 12
print(square.side)        # 12
print(square.perimeter)   # 48
