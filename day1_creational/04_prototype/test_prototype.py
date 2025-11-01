"""
Testy dla Prototype Pattern - Object Cloning
"""

import pytest
from starter import Enemy, Item, Spell, PrototypeManager


class TestEnemyPrototype:
    """Testy klonowania przeciwników"""

    def test_enemy_clone_basic(self):
        """Test podstawowego klonowania przeciwnika"""
        orc = Enemy("Orc", 100, 15, ["club", "leather_armor"])
        orc_clone = orc.clone()

        # Sprawdź że są różnymi obiektami
        assert orc is not orc_clone

        # Sprawdź że mają te same wartości
        assert orc_clone.name == "Orc"
        assert orc_clone.hp == 100
        assert orc_clone.damage == 15
        assert orc_clone.equipment == ["club", "leather_armor"]

    def test_enemy_clone_deep_copy_equipment(self):
        """Test deep copy dla equipment"""
        orc = Enemy("Orc", 100, 15, ["club", "leather_armor"])
        orc_clone = orc.clone()

        # Modyfikuj equipment w klonie
        orc_clone.equipment.append("shield")
        orc_clone.equipment[0] = "iron_club"

        # Oryginał nie powinien być zmieniony
        assert orc.equipment == ["club", "leather_armor"]
        assert orc_clone.equipment == ["iron_club", "leather_armor", "shield"]

        # Listy powinny być różnymi obiektami
        assert orc.equipment is not orc_clone.equipment

    def test_enemy_clone_shallow_copy_primitives(self):
        """Test że primitive values są skopiowane poprawnie"""
        orc = Enemy("Orc", 100, 15, ["club"])
        orc_clone = orc.clone()

        # Zmień wartości w klonie
        orc_clone.name = "Elite Orc"
        orc_clone.hp = 200
        orc_clone.damage = 25

        # Oryginał nie powinien być zmieniony
        assert orc.name == "Orc"
        assert orc.hp == 100
        assert orc.damage == 15

    def test_enemy_str_representation(self):
        """Test reprezentacji string"""
        orc = Enemy("Orc Warrior", 120, 20, ["sword"])
        assert "Orc Warrior" in str(orc)
        assert "120" in str(orc)
        assert "20" in str(orc)


class TestItemPrototype:
    """Testy klonowania przedmiotów"""

    def test_item_clone_basic(self):
        """Test podstawowego klonowania przedmiotu"""
        sword = Item("Iron Sword", "weapon", {"damage": 25, "durability": 100})
        sword_clone = sword.clone()

        # Różne obiekty
        assert sword is not sword_clone

        # Te same wartości
        assert sword_clone.name == "Iron Sword"
        assert sword_clone.item_type == "weapon"
        assert sword_clone.properties == {"damage": 25, "durability": 100}

    def test_item_clone_deep_copy_properties(self):
        """Test deep copy dla properties"""
        sword = Item("Magic Sword", "weapon", {
            "damage": 50,
            "enchantments": ["fire", "sharpness"],
            "stats": {"strength": 5, "agility": 2}
        })
        sword_clone = sword.clone()

        # Modyfikuj properties w klonie
        sword_clone.properties["damage"] = 75
        sword_clone.properties["enchantments"].append("lightning")
        sword_clone.properties["stats"]["strength"] = 10

        # Oryginał nie powinien być zmieniony
        assert sword.properties["damage"] == 50
        assert sword.properties["enchantments"] == ["fire", "sharpness"]
        assert sword.properties["stats"]["strength"] == 5

        # Dict powinien być różnym obiektem
        assert sword.properties is not sword_clone.properties
        assert sword.properties["enchantments"] is not sword_clone.properties["enchantments"]
        assert sword.properties["stats"] is not sword_clone.properties["stats"]

    def test_item_str_representation(self):
        """Test reprezentacji string"""
        potion = Item("Health Potion", "consumable", {"heal": 50})
        assert "Health Potion" in str(potion)
        assert "consumable" in str(potion)


class TestSpellPrototype:
    """Testy klonowania czarów"""

    def test_spell_clone_basic(self):
        """Test podstawowego klonowania czaru"""
        fireball = Spell("Fireball", 15, ["fire_damage", "area_effect"])
        fireball_clone = fireball.clone()

        # Różne obiekty
        assert fireball is not fireball_clone

        # Te same wartości
        assert fireball_clone.name == "Fireball"
        assert fireball_clone.mana_cost == 15
        assert fireball_clone.effects == ["fire_damage", "area_effect"]

    def test_spell_clone_deep_copy_effects(self):
        """Test deep copy dla effects"""
        spell = Spell("Complex Spell", 25, ["damage", "slow", "poison"])
        spell_clone = spell.clone()

        # Modyfikuj effects w klonie
        spell_clone.effects.append("stun")
        spell_clone.effects[0] = "massive_damage"

        # Oryginał nie powinien być zmieniony
        assert spell.effects == ["damage", "slow", "poison"]
        assert spell_clone.effects == ["massive_damage", "slow", "poison", "stun"]

        # Listy powinny być różnymi obiektami
        assert spell.effects is not spell_clone.effects

    def test_spell_str_representation(self):
        """Test reprezentacji string"""
        heal = Spell("Greater Heal", 20, ["heal"])
        assert "Greater Heal" in str(heal)
        assert "20" in str(heal)


class TestPrototypeManager:
    """Testy managera prototypów"""

    def test_register_and_create(self):
        """Test rejestracji i tworzenia prototypów"""
        manager = PrototypeManager()
        orc = Enemy("Base Orc", 80, 12, ["club"])

        # Zarejestruj
        manager.register("orc_template", orc)

        # Stwórz nową instancję
        new_orc = manager.create("orc_template")

        # Sprawdź że to różne obiekty z tymi samymi wartościami
        assert orc is not new_orc
        assert new_orc.name == "Base Orc"
        assert new_orc.hp == 80
        assert new_orc.damage == 12
        assert new_orc.equipment == ["club"]

    def test_create_nonexistent_prototype(self):
        """Test tworzenia nieistniejącego prototypu"""
        manager = PrototypeManager()

        with pytest.raises(KeyError):
            manager.create("nonexistent")

    def test_create_multiple(self):
        """Test tworzenia wielu instancji"""
        manager = PrototypeManager()
        sword = Item("Base Sword", "weapon", {"damage": 20})

        manager.register("sword_template", sword)

        # Stwórz 5 kopii
        swords = manager.create_multiple("sword_template", 5)

        assert len(swords) == 5

        # Wszystkie powinny być różnymi obiektami
        for i in range(len(swords)):
            for j in range(i + 1, len(swords)):
                assert swords[i] is not swords[j]

        # Wszystkie powinny mieć te same wartości
        for sword_copy in swords:
            assert sword_copy.name == "Base Sword"
            assert sword_copy.item_type == "weapon"
            assert sword_copy.properties["damage"] == 20

    def test_create_multiple_zero_count(self):
        """Test tworzenia zero instancji"""
        manager = PrototypeManager()
        orc = Enemy("Orc", 100, 15, ["club"])
        manager.register("orc", orc)

        result = manager.create_multiple("orc", 0)
        assert result == []

    def test_list_prototypes(self):
        """Test listowania zarejestrowanych prototypów"""
        manager = PrototypeManager()

        # Początkowo pusty
        assert manager.list_prototypes() == []

        # Dodaj prototypy
        orc = Enemy("Orc", 100, 15, ["club"])
        sword = Item("Sword", "weapon", {"damage": 25})
        fireball = Spell("Fireball", 15, ["fire"])

        manager.register("orc", orc)
        manager.register("sword", sword)
        manager.register("fireball", fireball)

        # Sprawdź listę
        prototypes = manager.list_prototypes()
        assert len(prototypes) == 3
        assert "orc" in prototypes
        assert "sword" in prototypes
        assert "fireball" in prototypes

    def test_register_multiple_types(self):
        """Test rejestracji różnych typów prototypów"""
        manager = PrototypeManager()

        # Różne typy
        enemy = Enemy("Dragon", 500, 75, ["claws", "fire_breath"])
        item = Item("Dragon Scale", "material", {"rarity": "legendary"})
        spell = Spell("Dragon Roar", 30, ["fear", "stun"])

        manager.register("dragon", enemy)
        manager.register("scale", item)
        manager.register("roar", spell)

        # Sprawdź że można tworzyć wszystkie typy
        new_dragon = manager.create("dragon")
        new_scale = manager.create("scale")
        new_roar = manager.create("roar")

        assert isinstance(new_dragon, Enemy)
        assert isinstance(new_scale, Item)
        assert isinstance(new_roar, Spell)


class TestPrototypePerformance:
    """Testy wydajności wzorca Prototype"""

    def test_clone_vs_constructor_concept(self):
        """Test konceptualny - klonowanie vs konstruktor"""
        # Stwórz skomplikowany obiekt
        complex_enemy = Enemy(
            "Elite Boss",
            1000,
            100,
            ["legendary_sword", "dragon_armor", "magic_ring", "health_potion"] * 10
        )

        # Klonowanie powinno działać
        clone1 = complex_enemy.clone()
        clone2 = complex_enemy.clone()

        # Sprawdź że klony są niezależne
        assert clone1 is not clone2
        assert clone1.equipment is not clone2.equipment

        # Modyfikacja jednego nie wpływa na drugi
        clone1.equipment.append("extra_item")
        assert len(clone1.equipment) != len(clone2.equipment)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
