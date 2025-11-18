# 🎁 Decorator - Discount System

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Decorator pattern - adding behavior dynamically

## 🎯 Zadanie
Implementuj system rabatów i promocji używając wzorca Decorator, gdzie można dynamicznie opakowywać produkty różnymi rodzajami zniżek.

## 📋 Wymagania
- [ ] `Product` interface z metodami `get_price()`, `get_description()`
- [ ] `BaseProduct` - podstawowy produkt z nazwą i ceną
- [ ] `DiscountDecorator` - bazowy dekorator implementujący Product
- [ ] `PercentageDiscount` - rabat procentowy (np. 10% off)
- [ ] `FixedAmountDiscount` - rabat kwotowy (np. $50 off)
- [ ] `FreeShipping` - darmowa dostawa (dodaje info, nie zmienia ceny)
- [ ] Możliwość stackowania wielu decoratorów

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj Product interface i BaseProduct
4. Zaimplementuj DiscountDecorator i konkretne dekoratory
5. Uruchom testy: `python -m pytest test_decorator.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- **Dziedziczenie**: Decorator implementuje ten sam interfejs co Product
- **Kompozycja**: Decorator wrappuje Product (przechowuje referencję)
- **Delegacja**: Decorator wywołuje metody wrappowanego Product
- Concrete decorators modyfikują wynik przed zwróceniem
- Opakowywanie: każdy decorator wrappuje poprzedni

## 🛒 Use Cases
- **E-commerce**: Kombinowanie różnych promocji
- **Seasonal Sales**: Black Friday + Member discount + Coupon
- **Dynamic Pricing**: A/B testing różnych strategii

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Eksplozja kombinacji klas ❌
class ProductWith10PercentAnd50OffAndFreeShipping:
  def get_price(self):
      return (self.base_price * 0.9) - 50  # Hardcoded logic ❌

class ProductWith5PercentAndFreeShipping:
  def get_price(self):
      return self.base_price * 0.95  # Duplikacja kodu ❌

# n promocji = 2^n klas! ❌
```

✅ Z wzorcem:

```python
# Dynamiczne opakowywanie ✅
laptop = BaseProduct("Gaming Laptop", 1000)
discounted = PercentageDiscount(laptop, 10)    # 10% off
with_coupon = FixedAmountDiscount(discounted, 50)  # $50 off  
final = FreeShipping(with_coupon)               # Free shipping

final.get_price()  # $850 (1000 * 0.9 - 50) ✅
# Dowolne kombinacje bez nowych klas! ✅
```

Korzyść: Elastyczne kombinowanie funkcjonalności w runtime
