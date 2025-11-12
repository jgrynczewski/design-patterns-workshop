# 🔌 Adapter - Payment Systems Integration

**Difficulty**: easy \
**Time**: 12 minutes \
**Focus**: Adapter pattern core concept

## 🎯 Zadanie
Zintegruj różne systemy płatności (PayPal, Stripe, Przelewy24) z jednym wspólnym interfejsem w systemie e-commerce.

## 📋 Wymagania
- [ ] Interface `PaymentProcessor` z metodą `process_payment(amount, currency)`
- [ ] Adapter dla PayPal API (metoda `make_payment`)
- [ ] Adapter dla Stripe API (metoda `charge`)
- [ ] Adapter dla Przelewy24 API (metoda `create_transaction`)
- [ ] Wszystkie adaptery zwracają format: `{"status": "success/failed", "transaction_id": "..."}`
- [ ] Support dla różnych walut (USD, EUR, PLN)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj adaptery dla każdego systemu płatności
4. Uruchom testy: `python -m pytest test_adapter.py -v`
5. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Każdy adapter implementuje `PaymentProcessor`
- Konwertuj kwotę zgodnie z wymaganiami API (PayPal w centach)
- `transaction_id` może być generowany randomowo dla mock APIs

## 🛒 Use Cases
- **E-commerce**: Jeden kod obsługuje wszystkie płatności
- **Migracja**: Łatwa zmiana dostawcy płatności
- **A/B Testing**: Różni użytkownicy → różne systemy

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Różne interfejsy dla każdego systemu ❌
if payment_method == "paypal":
  paypal.make_payment(amount * 100, currency)  # centy
elif payment_method == "stripe":
  stripe.charge(amount, currency, "card_token")
elif payment_method == "przelewy24":
  p24.create_transaction(amount, currency, merchant_id)
# Dodanie nowego systemu = modyfikacja kodu ❌
```

### ✅ Z wzorcem:

```python
# Jeden interfejs dla wszystkich ✅
processor = get_payment_processor(payment_method)
result = processor.process_payment(amount, currency)
# Nowy system = nowy adapter (zero zmian w kodzie!) ✅
```

Korzyść: Jednolity interfejs dla różnych systemów zewnętrznych
