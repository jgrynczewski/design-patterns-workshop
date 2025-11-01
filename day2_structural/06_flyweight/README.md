# 🪶 Flyweight - Product Data Optimization

**Difficulty**: hard \
**Time**: 20 minutes \
**Focus**: Flyweight pattern - memory optimization through shared state

## 🎯 Zadanie
Optymalizuj zużycie pamięci dla tysięcy produktów e-commerce używając wzorca Flyweight, który współdzieli powtarzające się dane między obiektami.

## 📋 Wymagania
- [ ] `ProductType` (flyweight) - współdzielone dane: category, brand, specifications
- [ ] `Product` (context) - unikalne dane: sku, price, stock_quantity
- [ ] `ProductTypeFactory` - zarządza pulą flyweights, zapobiega duplikatom
- [ ] `ProductCatalog` - przechowuje produkty z extrinsic state
- [ ] Metoda `display_product_info()` łącząca intrinsic + extrinsic data
- [ ] Demonstracja oszczędności pamięci (1000+ produktów, <50 flyweights)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj ProductType (flyweight) i Factory
4. Zaimplementuj Product (context) i Catalog
5. Uruchom testy: `python -m pytest test_flyweight.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Intrinsic state: dane niezmienne, współdzielone (category, brand, specs)
- Extrinsic state: dane zmienne, unikalne (price, stock, sku)
- Factory zwraca istniejący flyweight lub tworzy nowy
- Product przechowuje tylko extrinsic state + referencję do flyweight

## 🏪 Use Cases
- **E-commerce**: Tysiące produktów tego samego typu
- **Gaming**: Soldiers, bullets, particles (podobne obiekty)
- **Text Editors**: Characters z podobnym formatowaniem

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Każdy produkt przechowuje wszystkie dane ❌
class Product:
  def __init__(self, sku, category, brand, specs, price, stock):
      self.sku = sku
      self.category = category      # Duplikowane! ❌
      self.brand = brand            # Duplikowane! ❌
      self.specifications = specs   # Duplikowane! ❌
      self.price = price
      self.stock = stock

# 1000 laptopów = 1000 × (category + brand + specs) ❌
```

### ✅ Z wzorcem:

```python
# Flyweight współdzieli powtarzające się dane ✅
laptop_type = factory.get_product_type("Electronics", "Dell", specs)
products = [
  Product("SKU001", laptop_type, 1500, 10),  # Tylko unikalne dane
  Product("SKU002", laptop_type, 1600, 5),   # Ten sam laptop_type!
  Product("SKU003", laptop_type, 1400, 8)    # Współdzielony ✅
]

# 1000 laptopów = 1 flyweight + 1000 × (sku + price + stock) ✅
```

Korzyść: Drastyczne zmniejszenie zużycia pamięci dla podobnych obiektów
