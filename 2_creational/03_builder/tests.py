"""
Testy dla Builder Pattern - RPG Character Creator
"""

import pytest
from starter import Character, CharacterBuilder


class TestCharacterBuilder:
    """Testy podstawowego Builder"""

    def test_builder_fluent_interface(self):
        """Test method chaining (fluent interface)"""
        builder = CharacterBuilder()

        # Test czy każda metoda zwraca builder (dla chaining)
        result = builder.set_name("Test")
        assert isinstance(result, CharacterBuilder)
        assert result is builder  # Powinien zwrócić siebie

        result = builder.set_class("warrior")
        assert isinstance(result, CharacterBuilder)
        assert result is builder

    def test_character_creation_with_required_fields(self):
        """Test tworzenia postaci z wymaganymi polami"""
        character = (CharacterBuilder()
                     .set_name("Aragorn")
                     .set_class("ranger")
                     .build())

        assert character.name == "Aragorn"
        assert character.character_class == "ranger"
        assert character.level == 1  # domyślny poziom

    def test_character_creation_with_all_fields(self):
        """Test tworzenia postaci ze wszystkimi polami"""
        character = (CharacterBuilder()
                     .set_name("Legolas")
                     .set_class("archer")
                     .set_level(25)
                     .set_stat("dexterity", 90)
                     .set_stat("perception", 85)
                     .add_skill("archery")
                     .add_skill("stealth")
                     .add_equipment("elven bow")
                     .add_equipment("quiver")
                     .build())

        assert character.name == "Legolas"
        assert character.character_class == "archer"
        assert character.level == 25
        assert character.stats["dexterity"] == 90
        assert character.stats["perception"] == 85
        assert "archery" in character.skills
        assert "stealth" in character.skills
        assert "elven bow" in character.equipment
        assert "quiver" in character.equipment

    def test_build_without_name_raises_error(self):
        """Test że brak name powoduje błąd"""
        builder = CharacterBuilder().set_class("warrior")

        with pytest.raises(ValueError, match="name"):
            builder.build()

    def test_build_without_class_raises_error(self):
        """Test że brak class powoduje błąd"""
        builder = CharacterBuilder().set_name("TestName")

        with pytest.raises(ValueError, match="class"):
            builder.build()

    def test_builder_reset(self):
        """Test resetowania builder"""
        builder = (CharacterBuilder()
                   .set_name("ToReset")
                   .set_class("warrior")
                   .set_level(10))

        builder.reset()

        # Po reset próba build bez ustawienia wymaganych pól powinna failować
        with pytest.raises(ValueError):
            builder.build()

    def test_builder_reuse_after_reset(self):
        """Test reużycia builder po reset"""
        builder = CharacterBuilder()

        # Pierwszy character
        char1 = (builder
                 .set_name("First")
                 .set_class("warrior")
                 .build())

        # Reset i drugi character
        char2 = (builder
                 .reset()
                 .set_name("Second")
                 .set_class("mage")
                 .build())

        assert char1.name == "First"
        assert char1.character_class == "warrior"
        assert char2.name == "Second"
        assert char2.character_class == "mage"

        # Powinny być różnymi obiektami
        assert char1 is not char2


class TestCharacterClass:
    """Testy klasy Character"""

    def test_character_str_representation(self):
        """Test reprezentacji string postaci"""
        character = Character()
        character.name = "TestName"
        character.character_class = "TestClass"
        character.level = 42

        str_repr = str(character)
        assert "TestName" in str_repr
        assert "TestClass" in str_repr
        assert "42" in str_repr

    def test_character_get_info(self):
        """Test metody get_info"""
        character = Character()
        character.name = "Test"
        character.character_class = "warrior"
        character.level = 5
        character.stats = {"strength": 80}
        character.skills = ["slash"]
        character.equipment = ["sword"]

        info = character.get_info()

        assert info["name"] == "Test"
        assert info["class"] == "warrior"
        assert info["level"] == 5
        assert info["stats"]["strength"] == 80
        assert "slash" in info["skills"]
        assert "sword" in info["equipment"]

        # Test że to są kopie (nie referencje)
        info["stats"]["strength"] = 999
        assert character.stats["strength"] == 80  # Nie powinno się zmienić


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

