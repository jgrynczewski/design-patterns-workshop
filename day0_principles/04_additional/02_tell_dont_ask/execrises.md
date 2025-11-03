# Tell, Don't Ask - Ćwiczenia

## 🎯 Cel
Nauka rozpoznawania naruszeń Tell Don't Ask i refaktoryzacji do enkapsulacji.

## 📋 Zadanie 1: Identyfikacja (5 min)

**W `violation_basic.py` znajdź:**
1. Które metody "ASK" o stan obiektu?
2. Gdzie kod manipuluje stanem z zewnątrz?
3. Dlaczego to jest problemem?

**W `solution_basic.py` zobacz:**
4. Jak obiekt sam zarządza swoim stanem?
5. Jakie są korzyści tego podejścia?

## 🔨 Zadanie 2: Refaktoryzacja (10 min)

**Przerefaktoryzuj ten kod z ASK → TELL:**

```python
class Car:
    def __init__(self):
        self.fuel = 50
        self.engine_running = False
    
    def get_fuel(self):
        return self.fuel
    
    def set_fuel(self, amount):
        self.fuel = amount
    
    def is_engine_running(self):
        return self.engine_running
    
    def set_engine_running(self, running):
        self.engine_running = running

class Driver:
    def start_trip(self, car):
        # ASK pattern - problematyczny kod
        if car.get_fuel() > 10:
            if not car.is_engine_running():
                car.set_engine_running(True)
            new_fuel = car.get_fuel() - 10
            car.set_fuel(new_fuel)
            return "Trip started"
        return "Not enough fuel"
```

Zadanie: Zmień na TELL pattern

💡 Zadanie 3: Rozpoznawanie wzorców (5 min)

Które z tych to Tell Don't Ask violation?
```python
# A
user.activate()

# B  
if user.is_active():
    user.set_last_login(datetime.now())

# C
order.add_item(product, quantity)

# D
if order.get_total() > 100:
  order.set_discount(0.1)

# E
account.withdraw(amount)
```
Odpowiedź: B i D to violations (ASK + manipulate)

✅ Sprawdź rozwiązania

Porównaj swoje odpowiedzi z solution.py - jak Twoje refaktoryzacje wypadają?
