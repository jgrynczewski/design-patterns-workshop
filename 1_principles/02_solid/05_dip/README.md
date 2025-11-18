# 🔌 DIP - Abstrakcja Bazy Danych

**Poziom**: łatwy  
**Cel**: Dependency Inversion Principle

## 🎯 Zadanie
Zaimplementuj system baz danych z abstrakcją: `Database` i konkretnymi klasami `MySQLDatabase`, `PostgreSQLDatabase`, `UserService`.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `UserService` zależy od abstrakcji `Database`, nie od konkretnej implementacji

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest tests.py -v`
3. Zaimplementuj interfejs `Database` (ABC)
4. Zaimplementuj `MySQLDatabase` i `PostgreSQLDatabase`
5. Zaimplementuj `UserService` z dependency injection
6. Uruchom testy ponownie (teraz powinny przejść)
7. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Lab XX - DIP"
   git push
   ```
8. Sprawdź wynik w GitHub Actions

## 💡 DIP w pigułce

**Depend on abstractions, not concretions**

❌ **Źle** (zależność od konkretnej klasy):
```python
class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Silna zależność ❌

    def save_user(self, user):
        self.db.save(user)  # Nie można zmienić na PostgreSQL
```

✅ **Dobrze** (zależność od abstrakcji):
```python
class UserService:
    def __init__(self, database: Database):  # Zależność od interfejsu ✅
        self.database = database

    def save_user(self, user):
        self.database.save(user)  # Działa z dowolną implementacją

# Użycie:
service1 = UserService(MySQLDatabase())
service2 = UserService(PostgreSQLDatabase())
service3 = UserService(MongoDB())  # Nowa baza, zero zmian!
```

**Korzyść**: `UserService` nie wie o MySQL/PostgreSQL - łatwa zmiana DB.
