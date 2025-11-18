"""
❌ PROBLEM: Eksplozja kombinacji klas dla różnych promocji

Rozwiązanie bez wzorca Decorator:
- Każda kombinacja promocji wymaga osobnej klasy
- n promocji = 2^n możliwych klas (eksplozja kombinatoryczna)
- Duplikacja logiki obliczania cen
- Niemożliwe dodawanie promocji dynamicznie w runtime
"""


class BaseProduct:
    """Podstawowy produkt bez promocji"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.name


class ProductWith10PercentOff:
    """❌ Osobna klasa dla 10% rabatu"""

    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price

    def get_price(self) -> float:
        return self.base_price * 0.9  # Hardcoded 10% off

    def get_description(self) -> str:
        return f"{self.name} (10% off)"


class ProductWith50DollarsOff:
    """❌ Osobna klasa dla $50 rabatu"""

    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price

    def get_price(self) -> float:
        return max(0, self.base_price - 50)  # Hardcoded $50 off

    def get_description(self) -> str:
        return f"{self.name} ($50 off)"


class ProductWith10PercentAnd50DollarsOff:
    """❌ Osobna klasa dla kombinacji 10% + $50 rabatu"""

    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price

    def get_price(self) -> float:
        # ❌ Duplikacja logiki z poprzednich klas
        price_after_percentage = self.base_price * 0.9
        return max(0, price_after_percentage - 50)

    def get_description(self) -> str:
        return f"{self.name} (10% off) ($50 off)"


class ProductWith10PercentAndFreeShipping:
    """❌ Kolejna kombinacja = kolejna klasa"""

    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price

    def get_price(self) -> float:
        return self.base_price * 0.9

    def get_description(self) -> str:
        return f"{self.name} (10% off) + Free Shipping"


# ❌ I tak dalej... dla każdej kombinacji potrzebujemy nowej klasy!
# - ProductWith50DollarsOffAndFreeShipping
# - ProductWith10PercentAnd50DollarsOffAndFreeShipping
# - ProductWith20PercentOff
# - ProductWith20PercentAnd50DollarsOff
# - ...
#
# 3 promocje = 2^3 = 8 możliwych kombinacji = 8 klas! ❌
# 5 promocji = 2^5 = 32 klasy! ❌
# 10 promocji = 2^10 = 1024 klasy! ❌


# ❌ Przykład użycia
if __name__ == "__main__":
    # Produkt bez promocji
    basic = BaseProduct("Gaming Laptop", 1000.0)
    print(f"{basic.get_description()}: ${basic.get_price()}")

    # Produkt z 10% rabatem - osobna klasa
    with_10_percent = ProductWith10PercentOff("Gaming Laptop", 1000.0)
    print(f"{with_10_percent.get_description()}: ${with_10_percent.get_price()}")

    # Produkt z $50 rabatem - osobna klasa
    with_50_dollars = ProductWith50DollarsOff("Gaming Laptop", 1000.0)
    print(f"{with_50_dollars.get_description()}: ${with_50_dollars.get_price()}")

    # Produkt z obiema promocjami - kolejna osobna klasa
    with_both = ProductWith10PercentAnd50DollarsOff("Gaming Laptop", 1000.0)
    print(f"{with_both.get_description()}: ${with_both.get_price()}")

    # ❌ Chcemy dodać promocję 15% off?
    #     Musimy stworzyć 8 nowych klas dla wszystkich kombinacji z 15%!
    #
    # ❌ Chcemy zmienić kolejność stosowania promocji (najpierw $50, potem 10%)?
    #     Musimy edytować lub tworzyć nowe klasy!
    #
    # ❌ Chcemy dynamicznie wybrać promocje w runtime?
    #     Niemożliwe - klasy są tworzone w compile time!


"""
Jakie problemy rozwiązuje Decorator?

1. ❌ Eksplozja kombinatoryczna klas
   - Każda kombinacja promocji wymaga osobnej klasy
   - n promocji = 2^n klas
   - Niemożliwe utrzymanie przy wielu promocjach

2. ❌ Duplikacja logiki
   - Obliczanie 10% rabatu powielone w wielu klasach
   - Zmiana sposobu liczenia rabatu wymaga edycji wielu klas
   - Naruszenie DRY (Don't Repeat Yourself)

3. ❌ Brak elastyczności
   - Nie można dynamicznie wybierać promocji w runtime
   - Kolejność promocji hardcoded w klasach
   - Dodanie nowej promocji wymaga tworzenia wielu nowych klas

4. ❌ Naruszenie Open/Closed Principle
   - Dodanie nowej promocji wymaga modyfikacji istniejących klas
   - Niemożliwe rozszerzenie bez modyfikacji

Jak Decorator to rozwiązuje?
1. Każda promocja to osobny dekorator (jedna klasa)
2. Dekoratory można opakowywać dynamicznie w runtime
3. Kompozycja: decorator wrappuje product
4. Dziedziczenie: decorator implementuje ten sam interfejs co product
5. Delegacja: decorator wywołuje product.get_price() i modyfikuje wynik
6. n promocji = n klas (nie 2^n!)
"""
