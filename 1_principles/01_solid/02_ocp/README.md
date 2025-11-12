# 📐 OCP - Shape Calculator

**Difficulty**: easy
**Time**: 10 minutes
**Focus**: Open/Closed Principle

## 🎯 Zadanie
Zaimplementuj kształty: `Circle`, `Square`, `Triangle`.

## 📋 Wymagania
- [ ] `Circle(radius)` - pole = π × r² (użyj 3.14)
- [ ] `Square(side)` - pole = side²
- [ ] `Triangle(base, height)` - pole = (base × height) / 2
- [ ] Wszystkie dziedziczą po `Shape`

## 🚀 Jak zacząć
```bash
cd day0_principles/01_solid/02_ocp
pytest test_ocp.py -v
```

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
class Shape(ABC):
    @abstractmethod
    def calculate_area(self): pass

class Circle(Shape):
    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Nowy kształt = nowa klasa, zero zmian w AreaCalculator ✅
class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
```

**Korzyść**: `AreaCalculator` nie zmienia się przy dodaniu Rectangle.

Sprawdź `solution_ocp.py` po wykonaniu.
