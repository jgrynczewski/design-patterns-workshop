"""
Testy dla OCP - Shape Calculator
"""

import pytest
from starter import Shape, Circle, Square, Triangle, AreaCalculator


class TestOCP:
    """Testy Open/Closed Principle"""

    def test_circle_area(self):
        """Test obliczania pola koła"""
        circle = Circle(5)
        assert circle.calculate_area() == 78.5

        circle2 = Circle(10)
        assert circle2.calculate_area() == 314.0

    def test_square_area(self):
        """Test obliczania pola kwadratu"""
        square = Square(4)
        assert square.calculate_area() == 16

        square2 = Square(7)
        assert square2.calculate_area() == 49

    def test_triangle_area(self):
        """Test obliczania pola trójkąta"""
        triangle = Triangle(3, 4)
        assert triangle.calculate_area() == 6.0

        triangle2 = Triangle(10, 5)
        assert triangle2.calculate_area() == 25.0

    def test_shapes_implement_interface(self):
        """Test czy wszystkie kształty implementują Shape"""
        circle = Circle(1)
        square = Square(1)
        triangle = Triangle(1, 1)

        assert isinstance(circle, Shape)
        assert isinstance(square, Shape)
        assert isinstance(triangle, Shape)

    def test_area_calculator_single_shape(self):
        """Test kalkulatora z jednym kształtem"""
        calculator = AreaCalculator()
        shapes = [Circle(5)]

        assert calculator.total_area(shapes) == 78.5

    def test_area_calculator_multiple_shapes(self):
        """Test kalkulatora z wieloma kształtami"""
        calculator = AreaCalculator()
        shapes = [
            Circle(5),     # 78.5
            Square(4),     # 16
            Triangle(3, 4) # 6
        ]

        total = calculator.total_area(shapes)
        assert total == 100.5

    def test_area_calculator_empty_list(self):
        """Test kalkulatora z pustą listą"""
        calculator = AreaCalculator()
        assert calculator.total_area([]) == 0

    def test_ocp_extensibility(self):
        """
        Test OCP: można dodać nowy kształt bez modyfikacji AreaCalculator
        """
        # Symulujemy dodanie nowego kształtu (Rectangle)
        class Rectangle(Shape):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def calculate_area(self):
                return self.width * self.height

        calculator = AreaCalculator()
        shapes = [
            Circle(5),
            Rectangle(5, 3)  # Nowy kształt!
        ]

        # AreaCalculator działa bez zmian
        total = calculator.total_area(shapes)
        assert total == 78.5 + 15  # Circle + Rectangle


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
