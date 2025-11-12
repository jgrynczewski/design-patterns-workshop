"""
Open/Closed Principle - Shape Calculator - SOLUTION

>>> circle = Circle(5)
>>> circle.calculate_area()
78.5

>>> square = Square(4)
>>> square.calculate_area()
16

>>> triangle = Triangle(3, 4)
>>> triangle.calculate_area()
6.0

>>> shapes = [Circle(5), Square(4), Triangle(3, 4)]
>>> calculator = AreaCalculator()
>>> calculator.total_area(shapes)
100.5
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Interfejs dla wszystkich kształtów"""

    @abstractmethod
    def calculate_area(self) -> float:
        """Oblicza pole powierzchni"""
        pass


class Circle(Shape):
    """Koło"""

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius ** 2


class Square(Shape):
    """Kwadrat"""

    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2


class Triangle(Shape):
    """Trójkąt"""

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return (self.base * self.height) / 2


class AreaCalculator:
    """Oblicza łączne pole dla listy kształtów"""

    def total_area(self, shapes: list[Shape]) -> float:
        return sum(shape.calculate_area() for shape in shapes)


if __name__ == "__main__":
    # Demo OCP
    shapes = [
        Circle(5),
        Square(4),
        Triangle(3, 4)
    ]

    calculator = AreaCalculator()
    total = calculator.total_area(shapes)

    print(f"Total area: {total}")
    print("\nOCP: Możemy dodać Rectangle bez zmiany AreaCalculator:")

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def calculate_area(self):
            return self.width * self.height

    shapes.append(Rectangle(5, 3))
    print(f"With rectangle: {calculator.total_area(shapes)}")
