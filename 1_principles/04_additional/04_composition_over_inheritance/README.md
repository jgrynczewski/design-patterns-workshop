# Composition over Inheritance

## Definicja
Buduj zachowanie przez **składanie obiektów**, nie dziedziczenie.

## Kluczowa różnica
**Inheritance (IS-A):** `ElectricCar extends Car`
**Composition (HAS-A):** `Car has Engine`

## Problem z dziedziczeniem
Sztywna hierarchia - trudno kombinować zachowania:
- `ElectricCar` + `FlyingCar` = `ElectricFlyingCar`? 🤔
- Każda kombinacja = nowa klasa w hierarchii

## Rozwiązanie przez kompozycję
```python
car = Car(engine=ElectricMotor(), flight=FlightSystem())
```

Korzyści kompozycji

- Elastyczność - łatwe kombinowanie zachowań
- Reużywalność - komponenty w różnych kontekstach
- Testowanie - izolowane testy komponentów
- Zmiana w runtime - wymiana silnika bez nowej klasy

Kiedy dziedziczenie OK?

- Prawdziwa relacja IS-A (Dog IS-A Animal)
- Stabilna hierarchia (nie zmienia się często)

Sprawdź przykłady: violation_basic.py vs solution_basic.py
