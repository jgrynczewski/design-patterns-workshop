"""
❌ PROBLEM: Bezpośrednie tworzenie produktów - brak spójności rodzin

Problemy:
1. Klient MUSI ZNAĆ konkretne klasy (Sword, Staff, HeavyArmor, etc.)
2. Brak gwarancji spójności - łatwo pomylić i stworzyć niespójny zestaw
3. Można przypadkowo skombinować Sword + LightRobe (warrior weapon + mage armor)
4. Klient operuje na konkretnych klasach, nie na abstrakcjach
"""

from abc import ABC, abstractmethod


# Product Interfaces

class Weapon(ABC):
    """Bazowy interfejs dla broni"""

    @abstractmethod
    def damage(self) -> int:
        """Zwraca obrażenia broni"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Zwraca nazwę broni"""
        pass


class Armor(ABC):
    """Bazowy interfejs dla pancerza"""

    @abstractmethod
    def defense(self) -> int:
        """Zwraca obronę pancerza"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Zwraca nazwę pancerza"""
        pass


# Concrete Products - Weapons

class Sword(Weapon):
    """Miecz - broń wojownika"""

    def damage(self) -> int:
        return 100

    def get_name(self) -> str:
        return "Heavy Sword"


class Staff(Weapon):
    """Laska - broń maga"""

    def damage(self) -> int:
        return 50

    def get_name(self) -> str:
        return "Magic Staff"


class Bow(Weapon):
    """Łuk - broń łucznika"""

    def damage(self) -> int:
        return 70

    def get_name(self) -> str:
        return "Long Bow"


# Concrete Products - Armor

class HeavyArmor(Armor):
    """Ciężka zbroja - pancerz wojownika"""

    def defense(self) -> int:
        return 60

    def get_name(self) -> str:
        return "Heavy Plate Armor"


class LightRobe(Armor):
    """Lekka szata - pancerz maga"""

    def defense(self) -> int:
        return 20

    def get_name(self) -> str:
        return "Light Robe"


class LeatherArmor(Armor):
    """Skórzana zbroja - pancerz łucznika"""

    def defense(self) -> int:
        return 35

    def get_name(self) -> str:
        return "Leather Armor"


# ❌ Przykład użycia - klient musi znać konkretne klasy
if __name__ == "__main__":
    print("=== WARRIOR EQUIPMENT ===")
    # ❌ Klient MUSI ZNAĆ że warrior używa Sword i HeavyArmor
    weapon = Sword()
    armor = HeavyArmor()
    print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
    print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")

    print("\n=== MAGE EQUIPMENT ===")
    # ❌ Klient MUSI ZNAĆ że mage używa Staff i LightRobe
    weapon = Staff()
    armor = LightRobe()
    print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
    print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")

    print("\n=== ARCHER EQUIPMENT ===")
    # ❌ Klient MUSI ZNAĆ że archer używa Bow i LeatherArmor
    weapon = Bow()
    armor = LeatherArmor()
    print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
    print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")

    print("\n=== ❌ PROBLEM - NIESPÓJNY ZESTAW ===")
    # ❌ Łatwo się pomylić i stworzyć niespójną kombinację!
    weapon = Sword()       # Heavy weapon (Warrior)
    armor = LightRobe()    # Light armor (Mage)
    print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
    print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")
    print("^ Warrior weapon + Mage armor? To nie ma sensu!")
    print("Nic nie wymusza spójności rodziny produktów!")


"""
Dlaczego to jest ZŁE?

1. ❌ Brak gwarancji spójności rodzin produktów
   - Można stworzyć Sword + LightRobe (warrior weapon + mage armor)
   - Można stworzyć Staff + HeavyArmor (mage weapon + warrior armor)
   - Nic nie wymusza że produkty pasują do siebie

2. ❌ Klient musi znać konkretne klasy
   - Musi wiedzieć że Warrior = Sword + HeavyArmor
   - Musi wiedzieć że Mage = Staff + LightRobe
   - Klient operuje na konkretach (Sword, Staff), nie abstrakcjach

3. ❌ Brak enkapsulacji logiki tworzenia
   - Klient sam musi znać wszystkie kombinacje
   - Wiedza o "rodzinach produktów" rozproszona po kodzie klienta

4. ❌ Trudne utrzymanie
   - Dodanie nowego produktu do rodziny = aktualizacja kodu klienta
   - Zmiana składu zestawu = aktualizacja wszędzie gdzie jest używany

5. ❌ Podatność na błędy
   - Łatwo o pomyłkę przy tworzeniu zestawu
   - Brak sprawdzenia w compile-time czy zestaw jest spójny

Jak Abstract Factory to rozwiązuje?
1. Każda rodzina produktów ma swoją fabrykę (WarriorEquipmentFactory, MageEquipmentFactory)
2. Fabryka gwarantuje spójność - zawsze zwraca pasujące produkty
3. Klient nie musi znać konkretnych klas - operuje na interfejsach (Weapon, Armor)
4. Klient używa fabryki - nie tworzy produktów bezpośrednio
5. Niemożliwe stworzenie niespójnego zestawu (Sword + LightRobe)
6. Logika "co pasuje do czego" enkapsulowana w fabrykach
"""
