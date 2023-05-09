class Square:
    def __init__(self, side):
        self._side = side
        self._count()  # podkreślenie w tym przypadku jest istotne, inaczej dostajemy błędy atrybutów

    def _count(self):
        self._perimeter = self._side * 4
        self._area = self._side ** 2
        self._diagonal = self._side * (2 ** 0.5)

    def set_side(self, new_length):
        self._side = new_length
        self._count()

    def set_perimeter(self, new_length):
        self._side = new_length / 4
        self._count()

    def set_area(self, new_area):
        self._side = new_area ** 0.5
        self._count()

    def set_diagonal(self, new_length):
        self._side = new_length / (2 ** 0.5)
        self._count()

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

