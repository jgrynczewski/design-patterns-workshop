# 🔌 Adapter - Payment Systems Integration

**Poziom**: średni  
**Cel**: Adapter - konwersja niekompatybilnych interfejsów

## 🎯 Zadanie
Zaimplementuj wzorzec Adapter dla systemu płatności e-commerce. Trzy różne systemy (PayPal, Stripe, Przelewy24) mają niekompatybilne interfejsy. Stwórz adaptery które konwertują je do wspólnego interfejsu `PaymentProcessor`.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `PayPalAdapter` - adaptuje `make_payment()` do `process_payment()`
- [ ] `StripeAdapter` - adaptuje `charge()` do `process_payment()`
- [ ] `Przelewy24Adapter` - adaptuje `create_transaction()` do `process_payment()`
- [ ] Wszystkie adaptery implementują `PaymentProcessor`
- [ ] Standardowy format zwrotny: `{"status": "success/failed", "transaction_id": "..."}`

## 🚀 Jak zacząć
1. Przejrzyj `problem.py` - zobacz problem bez adaptera
   ```bash
   python problem.py
   ```
2. Otwórz `starter.py`
3. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest tests.py -v`
4. Zaimplementuj trzy adaptery:
   - Każdy dziedziczy z `PaymentProcessor`
   - Zawiera instancję zewnętrznego serwisu (kompozycja)
   - Konwertuje parametry, wywołuje API, standaryzuje odpowiedź
5. Uruchom testy ponownie (teraz powinny przejść)

## 💡 Adapter w pigułce

**Adapter konwertuje niekompatybilne interfejsy na wspólny interfejs**

### Jak to działa:
1. Zewnętrzne API mają różne interfejsy (różne nazwy metod, parametry, formaty)
2. Każdy adapter implementuje wspólny interfejs (`PaymentProcessor`)
3. Adapter zawiera instancję zewnętrznego serwisu (kompozycja)
4. Adapter tłumaczy wywołania: interfejs klienta → interfejs serwisu

### Kluczowy moment:
```python
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_service: PayPalService):
        self.paypal_service = paypal_service  # Kompozycja

    def process_payment(self, amount, currency):
        # 1. Konwersja parametrów (amount → amount_cents)
        # 2. Wywołanie API serwisu
        response = self.paypal_service.make_payment(...)
        # 3. Standaryzacja odpowiedzi (status_code → status)
        return {"status": ..., "transaction_id": ...}
```

Adapter **tłumaczy** między dwoma niekompatybilnymi interfejsami.

---

### ❌ Bez wzorca:
```python
# Wszystkie systemy w jednym miejscu z if/elif
def process_payment(provider, amount, currency):
    if provider == "paypal":
        # Konwersja dla PayPal...
        response = paypal.make_payment(...)
    elif provider == "stripe":
        # Konwersja dla Stripe...
        response = stripe.charge(...)
    elif provider == "przelewy24":
        # Dodanie nowego systemu = edycja tej funkcji
```

### ✅ Z wzorcem (Adapter):
```python
# Każdy system w osobnym adapterze
class PayPalAdapter(PaymentProcessor):
    def process_payment(self, amount, currency):
        # Konwersja + wywołanie + standaryzacja
        ...

# Klient używa tylko interfejsu
processor = PayPalAdapter(PayPalService())  # lub StripeAdapter, Przelewy24Adapter
result = processor.process_payment(100, "USD")
```

**Korzyść**: Nowy system = nowy adapter. Klient nie zmienia się, używa tylko `PaymentProcessor`.

## 🛒 Use Cases
- **E-commerce**: Jeden kod obsługuje wszystkie płatności
- **Migracja**: Łatwa zmiana dostawcy płatności
- **A/B Testing**: Różni użytkownicy → różne systemy
- **Integracja legacy code**: Dostosowanie starych API do nowych
