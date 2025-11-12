# Dependency Injection

## Definicja
Przekazuj zależności z **zewnątrz**, zamiast tworzyć je wewnątrz.

## Kluczowa różnica
**❌ Hard dependency:** `self.logger = FileLogger()` \
**✅ Injected dependency:** `def __init__(self, logger)`

## Rodzaje injection:
- **Constructor Injection** - przez konstruktor (najczęściej)
- **Setter Injection** - przez metodę setter
- **Interface Injection** - przez interfejs

## ❌ Problem bez DI:
```python
class OrderService:
    def __init__(self):
        self.db = PostgreSQL()  # Hard dependency!
```
✅ Rozwiązanie z DI:
```python
class OrderService:
    def __init__(self, db):  # Injected!
        self.db = db
```

Korzyści DI

- Testowanie - łatwe mockowanie zależności
- Flexibility - zmiana implementacji bez zmiany kodu
- Loose coupling - klasy nie znają konkretnych implementacji
- Konfiguracja - centralna konfiguracja zależności

Sprawdź przykłady: violation_basic.py vs solution_basic.py
