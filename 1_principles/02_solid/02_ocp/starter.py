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


# TODO: Zaimplementuj interfejs Shape
# Klasa abstrakcyjna z metodą calculate_area()

class Shape:
    pass


# TODO: Zaimplementuj Circle
# Przyjmuje radius w konstruktorze
# Dziedziczy po Shape
# Pole = π * r²  (użyj 3.14 dla π)

class Circle:
    pass


# TODO: Zaimplementuj Square
# Przyjmuje side w konstruktorze
# Dziedziczy po Shape
# Pole = side²

class Square:
    pass


# TODO: Zaimplementuj Triangle
# Przyjmuje base i height w konstruktorze
# Dziedziczy po Shape
# Pole = (base * height) / 2

class Triangle:
    pass


# TODO: Zaimplementuj AreaCalculator
# Metoda total_area(shapes) przyjmuje listę kształtów
# i zwraca sumę ich pól używając polimorfizmu

class AreaCalculator:
    pass


# OCP: Open for extension, Closed for modification
# Nowy kształt = nowa klasa Shape, zero zmian w AreaCalculator
