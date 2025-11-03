# Separation of Concerns - Ćwiczenia

## 🎯 Cel
Identyfikacja concerns zmieszanych w jednej klasie i praktyczne rozdzielenie.

## 📋 Zadanie 1: Code Review (10 min)

### Analiza `violation.py`:
1. **Ile różnych concerns ma klasa User?**
- Wymień każdy typ odpowiedzialności
- Który concern powinien być w domain layer?

2. **Problemy w UserController:**
- Jakie warstwy architektoniczne są zmieszane?
- Co się stanie gdy zmienisz format bazy danych?

### Analiza `solution.py`:
3. **Jak są rozdzielone concerns?**
- Ile klas odpowiada za persistence?
- Gdzie jest business logic?

## 🔨 Zadanie 2: Hands-on Refactoring (15 min)

**Dany kod naruszający SoC:**

```python
import json

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def calculate_tax(self):
        return self.price * 0.23  # Business rule
    
    def save_to_json(self):
        with open(f'{self.name}.json', 'w') as f:
            json.dump({'name': self.name, 'price': self.price}, f)
    
    def send_notification(self):
        print(f"Product {self.name} updated!")  # Should be email/SMS
    
    def validate_price(self, new_price):
        if new_price < 0:
            raise ValueError("Invalid price")
        return True
```

Zadania:
1. Zidentyfikuj wszystkie concerns w klasie Product
2. Podziel na warstwy: Domain, Infrastructure, Presentation
3. Stwórz osobne klasy dla każdego concern
4. Zastanów się: gdzie umieścić validation logic?

💡 Zadanie 3: Discussion (10 min)

Pytania do dyskusji:
- Czy validation to business logic czy presentation concern?
- Gdzie umieścić logikę "Product musi mieć cenę > 0"?
- Jak odróżnić technical validation od business rules?
- Kiedy można złamać SoC dla prostoty?

✅ Rozwiązania

Sprawdź swoje odpowiedzi z solution.py - czy Twój podział jest podobny?
