"""
Open/Closed Principle - Shape Calculator

>>> circle = Circle(5)
>>> circle.calculate_area()
78.5

>>> square = Square(4)
>>> square.calculate_area()
16

>>> triangle = Triangle(3, 4)
>>> triangle.calculate_area()
6.0

>>> # Test AreaCalculator
>>> shapes = [Circle(5), Square(4), Triangle(3, 4)]
>>> calculator = AreaCalculator()
>>> total = calculator.total_area(shapes)
>>> total
100.5
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Interfejs dla wszystkich kształtów"""

    @abstractmethod
    def calculate_area(self) -> float:
        """Oblicza pole powierzchni"""
        pass


# TODO: Zaimplementuj Circle
# Hint: Przyjmuje radius w konstruktorze
# Hint: Pole = π * r²  (użyj 3.14 dla π)

class Circle:
    pass


# TODO: Zaimplementuj Square
# Hint: Przyjmuje side w konstruktorze
# Hint: Pole = side²

class Square:
    pass


# TODO: Zaimplementuj Triangle
# Hint: Przyjmuje base i height w konstruktorze
# Hint: Pole = (base * height) / 2

class Triangle:
    pass


class AreaCalculator:
    """Oblicza łączne pole dla listy kształtów"""

    def total_area(self, shapes: list[Shape]) -> float:
        """
        Oblicza sumę pól wszystkich kształtów

        OCP: Możemy dodać nowy kształt (Rectangle, Pentagon)
        bez modyfikacji tej klasy!
        """
        return sum(shape.calculate_area() for shape in shapes)


# OCP: Open for extension, Closed for modification
# Nowy kształt = nowa klasa Shape, zero zmian w AreaCalculator
