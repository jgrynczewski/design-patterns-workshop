# 🎯 Strategy - Task Processing Strategies

**Poziom**: łatwy
**Cel**: Strategy - wymienne algorytmy przetwarzania

## 🎯 Zadanie
Zaimplementuj wzorzec Strategy dla systemu przetwarzania zadań. Trzy różne strategie (urgent, standard, background) przetwarzają zadania w różny sposób. `TaskManager` może zmieniać strategię w runtime.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `UrgentTaskProcessor` - natychmiastowe przetwarzanie (bez delay)
- [ ] `StandardTaskProcessor` - normalne przetwarzanie (1s delay)
- [ ] `BackgroundTaskProcessor` - przetwarzanie w tle (0.1s delay)
- [ ] `TaskManager` deleguje do strategii
- [ ] `TaskManager.set_strategy()` - zmiana strategii w runtime

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v` dla bardziej szczegółowego outputu)
3. Klasy pomocnicze (`TaskPriority`, `WorkflowTask`) i interfejs `TaskProcessor` są już gotowe
4. Zaimplementuj trzy konkretne strategie:
   - `UrgentTaskProcessor` - walidacja: priority == URGENT
   - `StandardTaskProcessor` - walidacja: len(title) >= 3
   - `BackgroundTaskProcessor` - walidacja: priority != URGENT
5. Zaimplementuj `TaskManager`:
   - Konstruktor przyjmujący opcjonalną strategię
   - Metoda `set_strategy()` - zmiana strategii
   - Metoda `execute_task()` - delegacja do `strategy.process_task()`
6. Uruchom testy ponownie (teraz powinny przejść)
7. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Strategy pattern"
   git push
   ```
8. Sprawdź wynik w GitHub Actions

## 💡 Strategy w pigułce

**Strategy enkapsuluje wymienne algorytmy i umożliwia delegację**

### Jak to działa:
1. Każdy algorytm w osobnej klasie (strategii)
2. Wszystkie strategie implementują ten sam interfejs
3. Context (TaskManager) deleguje pracę do aktualnej strategii
4. Strategię można zmienić w runtime

### Kluczowy moment:
```python
def execute_task(self, task: WorkflowTask) -> Dict[str, Any]:
    # Context deleguje do strategii
    return self.strategy.process_task(task)
```

TaskManager nie wie jak przetwarzać - deleguje to do strategii.

---

### ❌ Bez wzorca:
```python
class TaskManager:
    def execute_task(self, task):
        # Wszystkie algorytmy w jednym miejscu z if/elif
        if task.priority == "urgent":
            # Logika urgent
            pass
        elif task.priority == "standard":
            time.sleep(1)
            # Logika standard
            pass
        # Dodanie nowego algorytmu = edycja metody
```

### ✅ Z wzorcem (Strategy):
```python
# Każdy algorytm w osobnej klasie
class UrgentTaskProcessor(TaskProcessor):
    def process_task(self, task):
        # Natychmiastowe przetwarzanie
        return {"strategy_used": "urgent", ...}

# Context deleguje
class TaskManager:
    def execute_task(self, task):
        return self.strategy.process_task(task)

# Zmiana w runtime
manager.set_strategy(BackgroundTaskProcessor())
```

**Korzyść**: Nowy algorytm = nowa klasa, zero zmian w TaskManager. Wymiana w runtime.
