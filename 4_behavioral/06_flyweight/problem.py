"""
❌ PROBLEM: Marnowanie pamięci przez duplikację współdzielonych danych

Rozwiązanie bez wzorca Flyweight:
- Każdy produkt przechowuje WSZYSTKIE dane (współdzielone + unikalne)
- Tysiące produktów tego samego typu = tysiące kopii tych samych danych
- Ogromne zużycie pamięci dla category, brand, specifications
- Brak mechanizmu współdzielenia powtarzających się danych
"""


class Product:
    """
    ❌ PROBLEM: Każdy produkt przechowuje wszystkie dane

    Nawet jeśli mamy 1000 identycznych laptopów Dell,
    każdy przechowuje kopię "Dell", "Electronics", specyfikacji
    """

    def __init__(self, sku: str, category: str, brand: str,
                 specifications: dict, price: float, stock_quantity: int):
        # ❌ Dane współdzielone (intrinsic) - DUPLIKOWANE!
        self.category = category  # Np. "Electronics" - powtórzone 1000x
        self.brand = brand  # Np. "Dell" - powtórzone 1000x
        self.specifications = specifications  # Np. {"CPU": "i7"} - powtórzone 1000x

        # Dane unikalne (extrinsic) - OK, każdy produkt ma inne
        self.sku = sku  # Unikalny SKU
        self.price = price  # Różne ceny
        self.stock_quantity = stock_quantity  # Różne stany magazynowe

    def display_info(self) -> str:
        """Wyświetl informacje o produkcie"""
        specs_str = ", ".join(f"{k}: {v}" for k, v in self.specifications.items())
        return (
            f"SKU: {self.sku} | "
            f"{self.brand} {self.category} | "
            f"Price: ${self.price} | "
            f"Stock: {self.stock_quantity} | "
            f"Specs: {specs_str}"
        )


# ❌ Przykład użycia - pokazuje problem
if __name__ == "__main__":
    # Specyfikacje laptopa Dell - BĘDĄ DUPLIKOWANE!
    dell_laptop_specs = {
        "CPU": "Intel i7-12700H",
        "RAM": "16GB DDR5",
        "Storage": "512GB NVMe SSD",
        "Display": "15.6 FHD",
        "GPU": "RTX 3060"
    }

    # Tworzymy 5 laptopów Dell (wyobraź sobie 1000!)
    products = []
    for i in range(5):
        product = Product(
            sku=f"DELL-LAP-{i:03d}",
            category="Electronics",  # ❌ DUPLIKACJA - to samo dla każdego
            brand="Dell",  # ❌ DUPLIKACJA - to samo dla każdego
            specifications=dell_laptop_specs.copy(),  # ❌ DUPLIKACJA - kopia słownika!
            price=1500.0 + (i * 50),  # Różne ceny - OK
            stock_quantity=10 - i  # Różne stany - OK
        )
        products.append(product)

    # Wyświetl produkty
    for product in products:
        print(product.display_info())

    # ❌ ANALIZA PROBLEMU:
    print("\n" + "=" * 70)
    print("❌ PROBLEM Z PAMIĘCIĄ:")
    print("=" * 70)

    # Każdy produkt przechowuje:
    # - category: "Electronics" (string ~20 bytes)
    # - brand: "Dell" (string ~10 bytes)
    # - specifications: dict (~200 bytes z 5 kluczami)
    # RAZEM: ~230 bytes DUPLIKOWANYCH danych na produkt

    print(f"Liczba produktów: {len(products)}")
    print(f"Duplikowane dane na produkt: ~230 bytes")
    print(f"ZMARNOWANA PAMIĘĆ: ~{len(products) * 230} bytes")
    print()
    print("Dla 1000 produktów: ~230KB zmarnowanej pamięci!")
    print("Dla 10000 produktów: ~2.3MB zmarnowanej pamięci!")
    print()
    print("❌ Wszystkie produkty mają te same:")
    print(f"  - category: '{products[0].category}'")
    print(f"  - brand: '{products[0].brand}'")
    print(f"  - specifications: {products[0].specifications}")
    print()
    print("Ale każdy produkt przechowuje WŁASNĄ KOPIĘ! ❌")


"""
Jakie problemy rozwiązuje Flyweight?

1. ❌ Marnowanie pamięci przez duplikację
   - Powtarzające się dane (category, brand, specs) kopiowane w każdym obiekcie
   - Im więcej obiektów, tym większe marnotrawstwo
   - Skala problemu rośnie liniowo z liczbą obiektów

2. ❌ Brak mechanizmu współdzielenia
   - Nie ma sposobu na współdzielenie identycznych danych
   - Każdy obiekt jest całkowicie niezależny
   - Zmiana współdzielonych danych wymaga update'u wszystkich obiektów

3. ❌ Problemy wydajnościowe
   - Alokacja pamięci dla tysięcy kopii tych samych danych
   - Cache misses przez rozproszenie danych
   - Wolniejsze tworzenie obiektów (więcej danych do skopiowania)

4. ❌ Trudna optymalizacja
   - Nie ma centralnego miejsca zarządzania współdzielonymi danymi
   - Niemożliwe policzenie ile pamięci faktycznie potrzeba
   - Brak kontroli nad duplikacją

Jak Flyweight to rozwiązuje?
1. ✅ Oddzielenie intrinsic state (współdzielony) od extrinsic state (unikalny)
2. ✅ Flyweight przechowuje intrinsic state - współdzielony między obiektami
3. ✅ Context przechowuje tylko extrinsic state + referencję do flyweight
4. ✅ Factory zarządza pulą flyweights - zapobiega duplikatom
5. ✅ Drastyczna redukcja zużycia pamięci (1000 obiektów = 1 flyweight + 1000 lekkich kontekstów)
"""
