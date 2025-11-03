# Business Logic - Ćwiczenia

## 🎯 Cel
Nauka rozróżniania business logic od technical logic.

## 📋 Zadanie 1: Identyfikacja (5 min)

**W `violation.py` znajdź:**
1. Które linie zawierają **business logic**?
2. Które linie zawierają **technical logic**?
3. Dlaczego nie można testować business rules w izolacji?

**Podpowiedź:** Zadaj pytanie "Czy to istniałoby bez komputera?"

## 🔨 Zadanie 2: Klasyfikacja (5 min)

**Sklasyfikuj te przykłady:**

```python
# A
def calculate_tax(amount):
    return amount * 0.23

# B
def save_to_database(data):
    conn = sqlite3.connect('db.sqlite')
    # ...

# C
def is_adult(age):
    return age >= 18

# D
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# E
def apply_student_discount(price):
    return price * 0.90
```

Które to business logic? Które technical?

💡 Zadanie 3: Refactoring (10 min)

Dany kod:
```python
import sqlite3

class Product:
    def get_price_with_tax(self):
        conn = sqlite3.connect('config.db')
        cursor = conn.cursor()
        cursor.execute("SELECT tax_rate FROM settings")
        tax_rate = cursor.fetchone()[0]
        conn.close()
        
        return self.price * (1 + tax_rate)
```

Zadanie: Rozdziel business logic od technical logic

Pytania:
- Co to business logic w tym kodzie?
- Co to technical logic?
- Jak byś to rozdzielił?

✅ Sprawdź rozwiązania

Porównaj swoje odpowiedzi z solution.py
