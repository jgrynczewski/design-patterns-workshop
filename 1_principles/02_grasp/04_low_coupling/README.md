# 🔗 GRASP Low Coupling - Game System

**Difficulty**: easy  
**Focus**: GRASP Low Coupling

## 🎯 Zadanie
Zaimplementuj `Game` - używa `ScoreService` zamiast bezpośrednio Database (low coupling).

## 📋 Wymagania
- [ ] `Game.__init__(score_service)` - przyjmuje ScoreService
- [ ] `finish_game(player, score)` - wywołuje score_service.save_score()
- [ ] Zwraca: `"Game finished. {result}"`

## 🚀 Jak zacząć
```bash
cd 2_principles/02_grasp/04_low_coupling
pytest test_coupling.py -v
```

## 💡 GRASP Low Coupling w pigułce

**Minimalizuj zależności między klasami**

❌ **Źle** (wysokie sprzężenie):
```python
class Game:
    def finish_game(self, player, score):
        db = Database()  # Bezpośrednia zależność ❌
        db.connect()
        db.save(player, score)
        # Game zna szczegóły Database - silne sprzężenie
```

✅ **Dobrze** (niskie sprzężenie):
```python
class Game:
    def __init__(self, score_service):  # Pośrednik ✅
        self.score_service = score_service

    def finish_game(self, player, score):
        self.score_service.save_score(player, score)
        # Game nie zna Database - luźne sprzężenie

# ScoreService izoluje Game od Database
```

**Korzyść**: Zmiana Database nie wpływa na Game. Łatwe testowanie (mock ScoreService).

Sprawdź `solution_coupling.py` po wykonaniu.
