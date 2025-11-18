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


# TODO: Zaimplementuj interfejs Shape
# Klasa abstrakcyjna z metodą calculate_area()

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Metoda abstrakcyjna - każdy kształt musi ją zaimplementować"""
        pass


# TODO: Zaimplementuj Circle
# Przyjmuje radius w konstruktorze
# Dziedziczy po Shape
# Pole = π * r²  (użyj 3.14 dla π)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius ** 2


# TODO: Zaimplementuj Square
# Przyjmuje side w konstruktorze
# Dziedziczy po Shape
# Pole = side²

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2


# TODO: Zaimplementuj Triangle
# Przyjmuje base i height w konstruktorze
# Dziedziczy po Shape
# Pole = (base * height) / 2

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return (self.base * self.height) / 2


# TODO: Zaimplementuj AreaCalculator
# Metoda total_area(shapes) przyjmuje listę kształtów
# i zwraca sumę ich pól używając polimorfizmu

class AreaCalculator:
    def total_area(self, shapes: list) -> float:
        """Polimorfizm - każdy kształt wie jak obliczyć swoje pole"""
        return sum(shape.calculate_area() for shape in shapes)


# OCP: Open for extension, Closed for modification
# Nowy kształt = nowa klasa Shape, zero zmian w AreaCalculator


# Przykład użycia
if __name__ == "__main__":
    shapes = [Circle(5), Square(4), Triangle(3, 4)]
    calculator = AreaCalculator()
    print(f"Total area: {calculator.total_area(shapes)}")
