# 🌳 Composite - Product Categories Tree

**Difficulty**: medium \
**Time**: 18 minutes \
**Focus**: Composite pattern - tree structures with uniform interface

## 🎯 Zadanie
Zbuduj hierarchiczne drzewo kategorii produktów używając wzorca Composite, gdzie można wykonywać operacje na produktach i kategoriach jednakowo.

## 📋 Wymagania
- [ ] `ProductComponent` interface z metodami `get_price()`, `get_product_count()`, `display()`
- [ ] `Product` (leaf) - konkretny produkt z nazwą i ceną
- [ ] `Category` (composite) - kategoria mogąca zawierać produkty i podkategorie
- [ ] `Category.add_item()` i `Category.remove_item()` do zarządzania dziećmi
- [ ] Recursive operations: suma cen, liczba produktów, wyświetlanie drzewa
- [ ] Support dla zagnieżdżonych kategorii (Electronics → Laptops → Gaming)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj ProductComponent interface
4. Zaimplementuj Product (leaf) i Category (composite)
5. Uruchom testy: `python -m pytest test_composite.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Category przechowuje listę children (produkty + podkategorie)
- Operacje na Category wywołują rekurencyjnie operacje na children
- Product zwraca własne wartości, Category agreguje wartości children
- Użyj isinstance() do rozróżnienia Product vs Category

## 🛒 Use Cases
- **E-commerce**: Hierarchia kategorii produktów
- **File System**: Folders i files z jednolitym interfejsem
- **Organization**: Działy, zespoły, pracownicy

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Różne klasy, różne interfejsy ❌
def calculate_total(items):
  total = 0
  for item in items:
      if isinstance(item, Product):
          total += item.price  # Różny interfejs
      elif isinstance(item, Category):
          total += item.get_category_total()  # Różny interfejs
          for subcat in item.subcategories:
              total += calculate_total(subcat.items)  # Skomplikowane!
  return total
```

### ✅ Z wzorcem:

```python
# Jednolity interfejs dla wszystkich ✅
electronics = Category("Electronics")
electronics.add_item(laptop)  # Product
electronics.add_item(phones_category)  # Category

total = electronics.get_price()  # Działa dla wszystkich! ✅
count = electronics.get_product_count()  # Rekurencyjnie ✅
```

Korzyść: Jednolite traktowanie obiektów prostych i złożonych
