# 🔗 GRASP Low Coupling - System Gry

**Poziom**: Łatwy  
**Cel**: GRASP Low Coupling

## 🎯 Zadanie
Zaimplementuj `Game` i `ScoreService` (pośrednika), aby zredukować sprzężenie między `Game` a `Database`.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `Game` używa `ScoreService` jako pośrednika (nie zna `Database`)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest tests.py -v`
3. Zaimplementuj klasę `ScoreService`
4. Zaimplementuj klasę `Game` z dependency injection
5. Uruchom testy ponownie (teraz powinny przejść)
6. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Lab XX - Low Coupling"
   git push
   ```
7. Sprawdź wynik w GitHub Actions

## 💡 GRASP Low Coupling w pigułce

**Minimalizuj zależności między klasami**

❌ **Źle** (silne sprzężenie):
```python
class Game:
    def finish_game(self, player, score):
        db = Database()  # Bezpośrednia zależność ❌
        db.connect()
        db.save(player, score)
        # Game zna szczegóły Database - silne sprzężenie
```

✅ **Dobrze** (luźne sprzężenie):
```python
class Game:
    def __init__(self, score_service):  # 1. wstrzykujemy pośrednika ✅
        self.score_service = score_service

    def finish_game(self, player, score):
        self.score_service.save_score(player, score)
        # 2. Game nie zna Database - luźne sprzężenie

# ScoreService izoluje Game od Database
```

**Korzyść**: Zmiana Database nie wpływa na Game. Łatwe testowanie (mock ScoreService).
