# Static vs Runtime - Ćwiczenia

## 🎯 Cel
Nauka rozróżniania tego co jest określone przed uruchomieniem vs podczas wykonania.

## 📋 Zadanie 1: Klasyfikacja (5 min)

**Sklasyfikuj jako STATIC lub RUNTIME:**

```python
# A
class User:
    def __init__(self, name):
        self.name = name

# B
user_input = input("Enter name: ")

# C
import json

# D
def calculate_tax(amount):
    return amount * 0.23

# E
current_time = datetime.now()

# F
class AdminUser(User):
    pass

# G
if user.is_admin():
    grant_access()

# H
@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"
```

Odpowiedzi: A,C,D,F,H-STATIC | B,E,G-RUNTIME

🔨 Zadanie 2: Polimorfizm (10 min)

Przeanalizuj ten kod:

```python
def process_shapes(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}")  # Która metoda zostanie wywołana?

circle = Circle(5)
rectangle = Rectangle(10, 20)
shapes = [circle, rectangle]
process_shapes(shapes)
```

Pytania:
1. Co jest STATIC w tym kodzie?
2. Co jest RUNTIME?
3. Kiedy Python "decyduje" którą metodę area() wywołać?

💡 Zadanie 3: Design Patterns (10 min)

Które z tych wzorców wykorzystują RUNTIME decisions?

- Strategy Pattern - wybór algorytmu w runtime
- Factory Method - tworzenie obiektów w runtime
- Singleton - kontrola instancji w runtime
- Template Method - struktura metody w static
- Observer - powiadomienia w runtime

Odpowiedź: Strategy, Factory, Singleton, Observer używają runtime decisions

🎯 Zadanie 4: Debugging context (5 min)

Kiedy łatwiej debugować?

# STATIC - błąd widoczny od razu
```python
def calculate_discount(amount: int) -> float:
    return amount * 0.1  # IDE wie że amount to int
```

# RUNTIME - błąd dopiero podczas wykonania
```python
def calculate_discount(amount):
    return amount * 0.1  # Co jeśli amount to string?
```

Pytanie: Dlaczego static typing pomaga w debugowaniu?

🔧 Zadanie 5: Optymalizacja (10 min)

Które z tych można zoptymalizować na etapie STATIC?

```python
# A: Stałe obliczenia
PI = 3.14159
CIRCLE_AREA = PI * 5 * 5  # Można przeliczyć w static time?

# B: Warunki z stałymi
DEBUG = True
if DEBUG:  # Można usunąć if w static time?
    print("Debug mode")

# C: Import optymalizacje  
import heavy_module  # Można lazy loading?

# D: Type checking
def process(data: list) -> int:  # Można sprawdzić typy w static?
    return len(data)
```

Pytanie: Które optymalizacje robi kompilator/interpreter?

✅ Sprawdź odpowiedzi

Porównaj swoje klasyfikacje z static_example.py i runtime_example.py
