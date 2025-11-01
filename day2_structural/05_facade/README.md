# 🏢 Facade - Order Processing System

**Difficulty**: easy \
**Time**: 10 minutes \
**Focus**: Facade pattern - simplifying complex subsystems

## 🎯 Zadanie
Uprost złożony system składania zamówień e-commerce używając wzorca Facade, który ukrywa skomplikowane interakcje między podsystemami.

## 📋 Wymagania
- [ ] `InventoryService` - sprawdzanie dostępności produktów
- [ ] `PaymentService` - przetwarzanie płatności
- [ ] `ShippingService` - organizacja dostawy
- [ ] `NotificationService` - wysyłanie powiadomień
- [ ] `OrderFacade` - prosty interfejs `place_order(customer, items)`
- [ ] Facade koordynuje wszystkie podsystemy w prawidłowej kolejności
- [ ] Obsługa błędów - rollback gdy któryś krok się nie powiedzie

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj wszystkie podsystemy (już częściowo gotowe)
4. Zaimplementuj OrderFacade z metodą place_order()
5. Uruchom testy: `python -m pytest test_facade.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Facade wywołuje podsystemy w kolejności: Inventory → Payment → Shipping → Notification
- Sprawdź stock przed płatnością
- Jeśli płatność się nie powiedzie, nie organizuj dostawy
- Zwróć strukturalny wynik: `{"success": bool, "order_id": str, "message": str}`

## 📦 Use Cases
- **E-commerce**: Uproszczenie procesu zamówienia
- **API Gateway**: Jeden endpoint dla wielu mikrousług
- **Legacy Integration**: Ukrycie skomplikowanych starych systemów

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Klient musi znać wszystkie podsystemy ❌
inventory = InventoryService()
payment = PaymentService()
shipping = ShippingService()
notifications = NotificationService()

# Złożony workflow ❌
if inventory.check_stock(items):
  if payment.process_payment(customer, total):
      tracking = shipping.arrange_delivery(customer, items)
      if tracking:
          notifications.send_confirmation(customer, tracking)
      else:
          payment.refund(customer, total)  # Manual rollback ❌
  else:
      # Handle payment failure ❌
# Duplikacja logiki w każdym miejscu użycia ❌
```

### ✅ Z wzorcem:

```python
# Prosty interfejs ✅
facade = OrderFacade()
result = facade.place_order(customer, items)

if result["success"]:
  print(f"Order placed: {result['order_id']}")
else:
  print(f"Order failed: {result['message']}")

# Cała złożoność ukryta w Facade ✅
```

Korzyść: Jeden prosty interfejs zamiast wielu skomplikowanych
