# 🎯 Strategy - Task Processing Strategies

**Difficulty**: easy \
**Time**: 15 minutes \
**Focus**: Strategy pattern - interchangeable algorithms

## 🎯 Zadanie
Implementuj różne strategie przetwarzania zadań w workflow używając wzorca Strategy, gdzie algorytm można wybierać dynamicznie w runtime.

## 📋 Wymagania
- [ ] `TaskProcessor` interface z metodą `process_task(task)`
- [ ] `UrgentTaskProcessor` - natychmiastowe przetwarzanie (0 delay)
- [ ] `StandardTaskProcessor` - normalne przetwarzanie (1s delay)
- [ ] `BackgroundTaskProcessor` - przetwarzanie w tle (3s delay)
- [ ] `TaskManager` (context) z metodą `set_strategy()` i `execute_task()`
- [ ] Automatyczny wybór strategii na podstawie priorytetu
- [ ] Różne algorytmy validation i logging dla każdej strategii

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj TaskProcessor interface i concrete strategies
4. Zaimplementuj TaskManager z dynamiczną zmianą strategii
5. Uruchom testy: `python -m pytest test_strategy.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- TaskManager deleguje przetwarzanie do aktualnej strategii
- Każda strategia ma inny sposób validation i execution
- Użyj enum dla priorytetów: LOW, MEDIUM, HIGH, URGENT
- Strategie można zmieniać[starter.py](starter.py) w runtime bez wpływu na TaskManager

## ⚡ Use Cases
- **Payment Processing**: Różne metody płatności (card/bank/crypto)
- **Data Compression**: Różne algorytmy kompresji (zip/gzip/lz4)
- **Sorting**: Różne algorytmy sortowania (quick/merge/heap)

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Jeden wielki if/else w klasie ❌
class TaskManager:
  def execute_task(self, task):
      if task.priority == "urgent":
          # Urgent logic hardcoded ❌
          self.validate_urgent(task)
          self.process_immediately(task)
          self.log_urgent_completion(task)
      elif task.priority == "standard":
          # Standard logic hardcoded ❌
          self.validate_standard(task)
          time.sleep(1)
          self.process_task(task)
      # Adding new priority = modifying this method ❌
```

### ✅ Z wzorcem:

```python
# Elastyczne strategie ✅
manager = TaskManager()
manager.set_strategy(UrgentTaskProcessor())
manager.execute_task(urgent_task)  # Natychmiastowe przetwarzanie

manager.set_strategy(BackgroundTaskProcessor())
manager.execute_task(low_task)     # Przetwarzanie w tle
# Nowa strategia = nowa klasa (zero zmian w TaskManager) ✅
```

Korzyść: Łatwa zmiana algorytmów bez modyfikacji kodu
