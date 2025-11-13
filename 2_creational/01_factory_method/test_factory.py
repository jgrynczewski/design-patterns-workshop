"""
Testy dla Factory Method Pattern - RPG Weapons
"""

import pytest
from starter import Warrior, Mage, Archer, Character, Weapon, Sword, Staff, Bow


class TestFactoryMethod:
    """Testy wzorca Factory Method"""

    def test_warrior_creates_sword(self):
        """Test czy Warrior tworzy Sword przez factory method"""
        warrior = Warrior("Conan")
        weapon = warrior.create_weapon()

        assert isinstance(weapon, Weapon)
        assert isinstance(weapon, Sword)
        assert weapon.get_name() == "Sword"
        assert weapon.get_damage() == 50

    def test_mage_creates_staff(self):
        """Test czy Mage tworzy Staff przez factory method"""
        mage = Mage("Gandalf")
        weapon = mage.create_weapon()

        assert isinstance(weapon, Weapon)
        assert isinstance(weapon, Staff)
        assert weapon.get_name() == "Staff"
        assert weapon.get_damage() == 30

    def test_archer_creates_bow(self):
        """Test czy Archer tworzy Bow przez factory method"""
        archer = Archer("Legolas")
        weapon = archer.create_weapon()

        assert isinstance(weapon, Weapon)
        assert isinstance(weapon, Bow)
        assert weapon.get_name() == "Bow"
        assert weapon.get_damage() == 40

    def test_warrior_attack(self):
        """Test metody attack() dla Warrior"""
        warrior = Warrior("Conan")
        result = warrior.attack()

        assert isinstance(result, str)
        assert "Conan" in result
        assert "Sword" in result
        assert "50" in result

    def test_mage_attack(self):
        """Test metody attack() dla Mage"""
        mage = Mage("Gandalf")
        result = mage.attack()

        assert isinstance(result, str)
        assert "Gandalf" in result
        assert "Staff" in result
        assert "30" in result

    def test_archer_attack(self):
        """Test metody attack() dla Archer"""
        archer = Archer("Legolas")
        result = archer.attack()

        assert isinstance(result, str)
        assert "Legolas" in result
        assert "Bow" in result
        assert "40" in result

    def test_character_is_abstract(self):
        """Test czy Character jest klasą abstrakcyjną"""
        with pytest.raises(TypeError):
            # Nie można stworzyć instancji klasy abstrakcyjnej
            Character("Someone")

    def test_weapon_is_abstract(self):
        """Test czy Weapon jest klasą abstrakcyjną"""
        with pytest.raises(TypeError):
            # Nie można stworzyć instancji klasy abstrakcyjnej
            Weapon()

    def test_multiple_characters_create_different_weapons(self):
        """Test czy różne postaci tworzą różne bronie"""
        warrior = Warrior("Warrior1")
        mage = Mage("Mage1")
        archer = Archer("Archer1")

        warrior_weapon = warrior.create_weapon()
        mage_weapon = mage.create_weapon()
        archer_weapon = archer.create_weapon()

        # Każda postać tworzy inną broń
        assert type(warrior_weapon) != type(mage_weapon)
        assert type(mage_weapon) != type(archer_weapon)
        assert type(warrior_weapon) != type(archer_weapon)

    def test_sword_implements_weapon_interface(self):
        """Test czy Sword implementuje interfejs Weapon"""
        sword = Sword()
        assert isinstance(sword, Weapon)
        assert hasattr(sword, 'get_name')
        assert hasattr(sword, 'get_damage')
        assert callable(sword.get_name)
        assert callable(sword.get_damage)

    def test_staff_implements_weapon_interface(self):
        """Test czy Staff implementuje interfejs Weapon"""
        staff = Staff()
        assert isinstance(staff, Weapon)
        assert hasattr(staff, 'get_name')
        assert hasattr(staff, 'get_damage')

    def test_bow_implements_weapon_interface(self):
        """Test czy Bow implementuje interfejs Weapon"""
        bow = Bow()
        assert isinstance(bow, Weapon)
        assert hasattr(bow, 'get_name')
        assert hasattr(bow, 'get_damage')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
