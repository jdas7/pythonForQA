from math import pi


class GeometricFigures:
    def area(self):
        pass


class Square(GeometricFigures):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Circle(GeometricFigures):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2


# crear listas
forms = [Square(5), Circle(3)]

for form in forms:
    print(f"Area: {form.area()}")
