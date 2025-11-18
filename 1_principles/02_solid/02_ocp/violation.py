"""
❌ VIOLATION of Open/Closed Principle

Problem: AreaCalculator jest ZAMKNIĘTY na rozszerzenie
- Dodanie nowego kształtu wymaga MODYFIKACJI AreaCalculator
- Trzeba dodać kolejny if/elif w metodzie total_area()
- Naruszenie OCP: klasa powinna być otwarta na rozszerzenie, zamknięta na modyfikację
"""


class Circle:
    """Koło bez interfejsu Shape"""

    def __init__(self, radius: float):
        self.radius = radius


class Square:
    """Kwadrat bez interfejsu Shape"""

    def __init__(self, side: float):
        self.side = side


class Triangle:
    """Trójkąt bez interfejsu Shape"""

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height


class AreaCalculator:
    """
    ❌ PROBLEM: Obliczanie pola wymaga znajomości każdego kształtu

    Konsekwencje:
    1. Nowy kształt (Rectangle, Pentagon) = EDYCJA tej klasy
    2. Każdy kształt dodaje kolejny if/elif (kod rośnie linearnie)
    3. Łatwo zapomnieć dodać nowy typ
    4. Testowanie wymaga modyfikacji testów AreaCalculator
    """

    def total_area(self, shapes: list) -> float:
        """
        ❌ Sprawdzanie typu isinstance() dla każdego kształtu
        """
        total = 0

        for shape in shapes:
            # ❌ PROBLEM: if/elif dla każdego typu
            if isinstance(shape, Circle):
                total += 3.14 * shape.radius ** 2
            elif isinstance(shape, Square):
                total += shape.side ** 2
            elif isinstance(shape, Triangle):
                total += (shape.base * shape.height) / 2
            # ❌ Co z Rectangle? Pentagon? Hexagon?
            # Każdy wymaga EDYCJI tej metody!

        return total


# ❌ Przykład użycia - działa, ale narusza OCP
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Square(4),
        Triangle(3, 4)
    ]

    calculator = AreaCalculator()
    total = calculator.total_area(shapes)
    print(f"Total area: {total}")  # 100.5

    # ❌ Chcę dodać Rectangle?
    # Muszę:
    # 1. Stworzyć klasę Rectangle
    # 2. EDYTOWAĆ AreaCalculator.total_area() (dodać elif)
    # 3. Zmodyfikować testy
    #
    # To naruszenie OCP!


"""
Dlaczego to jest ZŁE?

1. ❌ Closed for extension
   - Nie można dodać Rectangle bez edycji AreaCalculator

2. ❌ Violation of OCP
   - Rozszerzenie funkcjonalności = modyfikacja istniejącego kodu

3. ❌ Trudne utrzymanie
   - Im więcej kształtów, tym dłuższa lista if/elif
   - Łatwo zapomnieć o dodaniu nowego typu

4. ❌ Naruszenie Single Responsibility
   - AreaCalculator musi ZNAĆ wszystkie typy kształtów
   - Zmiana w Circle może wymagać zmiany w AreaCalculator

Jak to naprawić?
1. Stwórz abstrakcyjną klasę Shape (ABC) z metodą calculate_area()
2. Każdy kształt (Circle, Square, Triangle) dziedziczy po Shape
3. Każdy kształt implementuje własną calculate_area()
4. AreaCalculator używa polimorfizmu - wywołuje shape.calculate_area() bez isinstance()
5. Nowy kształt = nowa klasa dziedzicząca po Shape, zero zmian w AreaCalculator
"""


# Przykład użycia
if __name__ == "__main__":
    shapes = [Circle(5), Square(4), Triangle(3, 4)]
    calculator = AreaCalculator()
    print(f"Total area: {calculator.total_area(shapes)}")
