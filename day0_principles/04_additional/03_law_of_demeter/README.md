# Law of Demeter

## Definicja
Obiekt powinien rozmawiać tylko ze swoimi "przyjaciółmi".

## Zasada jednej kropki
**✅ OK:** `object.method()`
**❌ Violation:** `object.field.method()`

## "Przyjaciele" obiektu:
- **Samego siebie** (`this/self`)
- **Parametry metod** (co dostałeś)
- **Pola klasy** (co masz)
- **Utworzone obiekty** (co stworzyłeś)

## ❌ Violation:
```python
order.customer.address.city.name  # Łańcuch wywołań
```
✅ Solution:

```python
order.get_customer_city()  # Delegacja
```

Dlaczego lepsze?

- Loose coupling - mniej zależności między klasami
- Enkapsulacja - ukrywanie wewnętrznej struktury
- Łatwiejsze zmiany - zmiana struktury nie łamie kodu

Sprawdź przykłady: violation_basic.py vs solution_basic.py
