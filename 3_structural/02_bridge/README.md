# 🌉 Bridge - Payment Platform Abstraction

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Bridge pattern - separating abstraction from implementation

## 🎯 Zadanie
Oddziel abstrakcję systemu płatności od implementacji konkretnej platformy (web/mobile/API) używając wzorca Bridge.

## 📋 Wymagania
- [ ] `PaymentGateway` (abstraction) z metodami `process_payment()`, `get_fees()`
- [ ] `Platform` interface (implementor) z metodami `authenticate()`, `send_request()`, `handle_response()`
- [ ] `WebPlatform` - implementacja dla przeglądarki web
- [ ] `MobilePlatform` - implementacja dla aplikacji mobilnych
- [ ] `APIPlatform` - implementacja dla integracji API
- [ ] `PayPalGateway` i `StripeGateway` używające różnych platform
- [ ] Każda platforma ma inne zachowanie (fees, authentication)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj Platform interface i konkretne platformy
4. Zaimplementuj PaymentGateway abstrakcję
5. Uruchom testy: `python -m pytest test_bridge.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Bridge łączy PaymentGateway z Platform
- Każda platforma ma inne fees: Web(2%), Mobile(1.5%), API(1%)
- Authentication różni się: Web(cookies), Mobile(biometrics), API(tokens)
- Gateway deleguje platform-specific operacje do Platform

## 💳 Use Cases
- **Multi-platform**: Ten sam payment provider, różne platformy
- **A/B Testing**: Różne UX dla różnych platform
- **Scaling**: Dodanie nowej platformy bez zmiany gateway

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Mieszanie logiki płatności z platformą ❌
class PayPalWebGateway:
  def process_web_payment(self): # Web-specific
      # PayPal logic + Web logic mixed ❌

class PayPalMobileGateway:
  def process_mobile_payment(self): # Mobile-specific
      # PayPal logic duplicated ❌

# Każda kombinacja = nowa klasa ❌
```

### ✅ Z wzorcem:

```python
# Oddzielenie abstrakcji od implementacji ✅
paypal_web = PayPalGateway(WebPlatform())
paypal_mobile = PayPalGateway(MobilePlatform())
stripe_api = StripeGateway(APIPlatform())
```

# Ta sama logika PayPal, różne platformy ✅

Korzyść: Niezależne rozwijanie abstrakcji i implementacji
