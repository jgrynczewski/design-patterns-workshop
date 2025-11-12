# 🔌 DIP - Database Abstraction

**Difficulty**: easy
**Time**: 10 minutes
**Focus**: Dependency Inversion Principle

## 🎯 Zadanie
Zaimplementuj bazy danych: `MySQLDatabase`, `PostgreSQLDatabase`.

## 📋 Wymagania
- [ ] `MySQLDatabase.connect()` → `"Connected to MySQL"`
- [ ] `MySQLDatabase.save(id, name)` → `"Saved {id}: {name} to MySQL"`
- [ ] `PostgreSQLDatabase` - analogicznie dla PostgreSQL
- [ ] Obie dziedziczą po `Database`

## 🚀 Jak zacząć
```bash
cd day0_principles/01_solid/05_dip
pytest test_dip.py -v
```

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

Sprawdź `solution_dip.py` po wykonaniu.
