# 🪶 Flyweight - Product Data Optimization

**Poziom**: Średni
**Czas**: 20 minut
**Cel**: Flyweight - optymalizacja pamięci przez współdzielenie powtarzających się danych

## 🎯 Zadanie
Zaimplementuj wzorzec Flyweight dla produktów e-commerce. Oddziel dane współdzielone (intrinsic state) od danych unikalnych (extrinsic state), aby drastycznie zmniejszyć zużycie pamięci dla tysięcy podobnych produktów.

## ✅ Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `ProductType` (flyweight) - przechowuje intrinsic state (category, brand, specifications)
- [ ] `ProductTypeFactory` - zarządza pulą flyweights, zapobiega duplikatom
- [ ] `Product` (context) - przechowuje extrinsic state (sku, price, stock) + referencję do flyweight
- [ ] Factory zwraca ten sam flyweight dla identycznych danych

## 🚀 Jak zacząć
1. Przejrzyj `problem.py` - zobacz marnowanie pamięci
   ```bash
   python problem.py
   ```
2. Otwórz `starter.py`
3. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v`)
4. Zaimplementuj:
   - `ProductType` - flyweight z intrinsic state
   - `ProductTypeFactory` - pula flyweights (sprawdź czy istnieje, zwróć lub stwórz)
   - `Product` - context z extrinsic state + referencją do flyweight
5. Uruchom testy ponownie (teraz powinny przejść)

## 💡 Podpowiedzi
- **Intrinsic state** (współdzielony): category, brand, specifications → w ProductType
- **Extrinsic state** (unikalny): sku, price, stock_quantity → w Product
- **Factory**: Sprawdza czy flyweight istnieje w puli, jeśli tak - zwraca, jeśli nie - tworzy
- **Klucz w factory**: `(category, brand, frozenset(specifications.items()))` - musi być hashable
- **Oszczędność**: 1000 produktów = 1 flyweight + 1000 lekkich kontekstów

## 📝 Przykład użycia
```python
# Stwórz factory
factory = ProductTypeFactory()

# Specyfikacje laptopa
dell_specs = {"CPU": "i7", "RAM": "16GB", "Storage": "512GB"}

# Stwórz produkty - factory zwróci TEN SAM flyweight
laptop_type1 = factory.get_product_type("Electronics", "Dell", dell_specs)
laptop_type2 = factory.get_product_type("Electronics", "Dell", dell_specs)

# To ten sam obiekt!
assert laptop_type1 is laptop_type2
assert factory.get_flyweight_count() == 1

# Stwórz produkty z tym samym flyweight
product1 = Product("DELL-001", laptop_type1, 1500.0, 10)
product2 = Product("DELL-002", laptop_type2, 1600.0, 5)

# Oba współdzielą flyweight, ale mają unikalne dane
assert product1.product_type is product2.product_type  # Ten sam!
assert product1.sku != product2.sku  # Różne!
```

## 📊 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Każdy produkt przechowuje WSZYSTKIE dane
class Product:
    def __init__(self, sku, category, brand, specs, price, stock):
        self.sku = sku
        self.category = category      # DUPLIKACJA ❌
        self.brand = brand            # DUPLIKACJA ❌
        self.specifications = specs   # DUPLIKACJA ❌
        self.price = price
        self.stock = stock

# 1000 laptopów Dell = 1000 kopii "Dell", "Electronics", specyfikacji
# Zmarnowana pamięć: ~230KB dla 1000 produktów
```

### ✅ Z wzorcem (Flyweight):
```python
# Flyweight przechowuje współdzielone dane
class ProductType:
    def __init__(self, category, brand, specs):
        self.category = category      # Współdzielone ✅
        self.brand = brand            # Współdzielone ✅
        self.specifications = specs   # Współdzielone ✅

# Context przechowuje tylko unikalne dane
class Product:
    def __init__(self, sku, product_type, price, stock):
        self.sku = sku                    # Unikalne
        self.product_type = product_type  # Referencja do flyweight
        self.price = price                # Unikalne
        self.stock = stock                # Unikalne

# 1000 laptopów Dell = 1 flyweight + 1000 lekkich kontekstów
# Oszczędność: ~90% pamięci!
```

**Korzyść**: Drastyczna redukcja zużycia pamięci przez współdzielenie powtarzających się danych.

## 🎯 Use Cases
- **E-commerce**: Tysiące produktów tego samego typu (Dell laptopy, iPhone'y)
- **Gaming**: Podobne obiekty (soldiers, bullets, particles, trees)
- **Text Editors**: Znaki z tym samym formatowaniem (font, size, color)
- **Graphics**: Ikony, sprites używane wielokrotnie
