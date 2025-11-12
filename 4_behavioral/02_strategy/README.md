# 🎯 Strategy - Task Processing Strategies

**Difficulty**: easy
**Time**: 15 minutes
**Focus**: Strategy pattern - interchangeable algorithms

## 🎯 Zadanie
Zaimplementuj `TaskManager` - dynamicznie wybiera algorytm przetwarzania zadań.

## 📋 Wymagania
- [ ] `TaskProcessor` interface z `process_task(task)`
- [ ] `UrgentTaskProcessor` - natychmiastowe (0 delay)
- [ ] `StandardTaskProcessor` - normalne (1s delay)
- [ ] `BackgroundTaskProcessor` - w tle (0.1s delay)
- [ ] `TaskManager.set_strategy()` - zmiana strategii w runtime
- [ ] `auto_select_strategy()` - wybór na podstawie priorytetu

## 🚀 Jak zacząć
```bash
cd day3_behavioral/02_strategy
pytest test_strategy.py -v
```

## 💡 Strategy w pigułce

**Wymienne algorytmy przetwarzania**

❌ **Źle** (hardcoded if/else):
```python
class TaskManager:
    def execute_task(self, task):
        if task.priority == "urgent":  # Hardcoded ❌
            self.validate_urgent(task)
            self.process_immediately(task)
        elif task.priority == "standard":
            time.sleep(1)  # Hardcoded ❌
            self.process_task(task)
        # Dodanie priorytetu = modyfikacja metody ❌
```

✅ **Dobrze** (Strategy pattern):
```python
# Interface
class TaskProcessor(ABC):
    @abstractmethod
    def process_task(self, task) -> Dict: pass

# Concrete Strategies
class UrgentTaskProcessor(TaskProcessor):
    def process_task(self, task):
        # Natychmiastowe przetwarzanie
        return {"strategy_used": "urgent", ...}

class StandardTaskProcessor(TaskProcessor):
    def process_task(self, task):
        time.sleep(1)  # Delay
        return {"strategy_used": "standard", ...}

# Context
class TaskManager:
    def __init__(self, strategy: TaskProcessor):
        self.strategy = strategy  # Delegacja ✅

    def execute_task(self, task):
        return self.strategy.process_task(task)

# Zmiana w runtime ✅
manager = TaskManager(UrgentTaskProcessor())
manager.set_strategy(BackgroundTaskProcessor())  # Wymiana strategii
```

**Korzyść**: Nowa strategia = nowa klasa (zero zmian w TaskManager).

**Kiedy stosować**:
- Różne algorytmy dla tego samego zadania
- Wymiana algorytmu w runtime
- Unikanie wielkich if/elif (open/closed principle)

Sprawdź `solution_strategy.py` po wykonaniu.
