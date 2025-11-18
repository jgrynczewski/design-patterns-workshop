# 📐 OCP - Kalkulator Kształtów

**Poziom**: łatwy  
**Cel**: Open/Closed Principle

## 🎯 Zadanie
Zaimplementuj rodzinę kształtów: `Circle`, `Square`, `Triangle`.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] Wszystkie kształty dziedziczą po `Shape` i implementują `calculate_area()`

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v` dla bardziej szczegółowego outputu)
3. Zaimplementuj klasy `Circle`, `Square`, `Triangle`
4. Uruchom testy ponownie (teraz powinny przejść)
5. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Lab 03 - OCP"
   git push
   ```
6. Sprawdź wynik w GitHub Actions

## 💡 OCP w pigułce

**Open for extension, Closed for modification**

❌ **Źle** (modyfikacja przy nowym kształcie):
```python
class AreaCalculator:
    def total_area(self, shapes):
        total = 0
        for shape in shapes:
            if isinstance(shape, Circle):
                total += 3.14 * shape.radius ** 2
            elif isinstance(shape, Square):
                total += shape.side ** 2
            # Nowy kształt = edycja if/elif ❌
        return total
```

✅ **Dobrze** (rozszerzenie bez modyfikacji):
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Nowy kształt = nowa klasa, zero zmian w AreaCalculator ✅
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
```

**Korzyść**: `AreaCalculator` nie zmienia się przy dodaniu Rectangle.
