"""
Testy dla Command Pattern - Undo/Redo Operations
"""

import pytest
from datetime import datetime
from starter import (
    Document, Command,
    CreateDocumentCommand, EditDocumentCommand, DeleteDocumentCommand,
    MacroCommand, DocumentManager, demonstrate_command_pattern
)


class TestDocument:
    """Testy klasy Document"""

    def test_document_creation(self):
        """Test tworzenia dokumentu"""
        doc = Document("doc1", "Test Document", "Initial content")

        assert doc.doc_id == "doc1"
        assert doc.title == "Test Document"
        assert doc.content == "Initial content"
        assert isinstance(doc.created_at, datetime)
        assert isinstance(doc.modified_at, datetime)

    def test_document_update_content(self):
        """Test aktualizacji treści dokumentu"""
        doc = Document("doc1", "Test", "Old content")

        old_content = doc.update_content("New content")

        assert old_content == "Old content"
        assert doc.content == "New content"
        assert doc.modified_at > doc.created_at


class TestCreateDocumentCommand:
    """Testy komendy tworzenia dokumentu"""

    def test_create_command_implements_interface(self):
        """Test że CreateDocumentCommand implementuje Command"""
        manager = DocumentManager()
        command = CreateDocumentCommand(manager, "doc1", "Test", "Content")
        assert isinstance(command, Command)

    def test_create_command_execute(self):
        """Test wykonania komendy tworzenia"""
        manager = DocumentManager()
        command = CreateDocumentCommand(manager, "doc1", "Test Doc", "Test content")

        # Przed wykonaniem
        assert len(manager.documents) == 0

        # Wykonaj komendę
        command.execute()

        # Po wykonaniu
        assert len(manager.documents) == 1
        doc = manager.find_document("doc1")
        assert doc is not None
        assert doc.title == "Test Doc"
        assert doc.content == "Test content"

    def test_create_command_undo(self):
        """Test cofnięcia komendy tworzenia"""
        manager = DocumentManager()
        command = CreateDocumentCommand(manager, "doc1", "Test", "Content")

        # Wykonaj i cofnij
        command.execute()
        assert len(manager.documents) == 1

        command.undo()
        assert len(manager.documents) == 0
        assert manager.find_document("doc1") is None


class TestEditDocumentCommand:
    """Testy komendy edycji dokumentu"""

    def test_edit_command_implements_interface(self):
        """Test że EditDocumentCommand implementuje Command"""
        manager = DocumentManager()
        command = EditDocumentCommand(manager, "doc1", "New content")
        assert isinstance(command, Command)

    def test_edit_command_execute(self):
        """Test wykonania komendy edycji"""
        manager = DocumentManager()
        doc = Document("doc1", "Test", "Original content")
        manager.add_document(doc)

        command = EditDocumentCommand(manager, "doc1", "Updated content")
        command.execute()

        assert doc.content == "Updated content"

    def test_edit_command_undo(self):
        """Test cofnięcia komendy edycji"""
        manager = DocumentManager()
        doc = Document("doc1", "Test", "Original content")
        manager.add_document(doc)

        command = EditDocumentCommand(manager, "doc1", "Updated content")

        # Wykonaj i sprawdź
        command.execute()
        assert doc.content == "Updated content"

        # Cofnij i sprawdź
        command.undo()
        assert doc.content == "Original content"

    def test_edit_nonexistent_document(self):
        """Test edycji nieistniejącego dokumentu"""
        manager = DocumentManager()
        command = EditDocumentCommand(manager, "nonexistent", "Content")

        # Powinno rzucić błąd lub nic nie robić
        # W zależności od implementacji
        try:
            command.execute()
        except (ValueError, AttributeError):
            pass  # Oczekiwane zachowanie


class TestDeleteDocumentCommand:
    """Testy komendy usuwania dokumentu"""

    def test_delete_command_implements_interface(self):
        """Test że DeleteDocumentCommand implementuje Command"""
        manager = DocumentManager()
        command = DeleteDocumentCommand(manager, "doc1")
        assert isinstance(command, Command)

    def test_delete_command_execute(self):
        """Test wykonania komendy usuwania"""
        manager = DocumentManager()
        doc = Document("doc1", "Test", "Content")
        manager.add_document(doc)

        command = DeleteDocumentCommand(manager, "doc1")

        # Przed usunięciem
        assert len(manager.documents) == 1

        # Wykonaj usunięcie
        command.execute()
        assert len(manager.documents) == 0
        assert manager.find_document("doc1") is None

    def test_delete_command_undo(self):
        """Test cofnięcia komendy usuwania"""
        manager = DocumentManager()
        doc = Document("doc1", "Test", "Content")
        manager.add_document(doc)

        command = DeleteDocumentCommand(manager, "doc1")

        # Usuń i przywróć
        command.execute()
        assert len(manager.documents) == 0

        command.undo()
        assert len(manager.documents) == 1

        restored_doc = manager.find_document("doc1")
        assert restored_doc is not None
        assert restored_doc.title == "Test"
        assert restored_doc.content == "Content"


class TestMacroCommand:
    """Testy komendy macro"""

    def test_macro_command_implements_interface(self):
        """Test że MacroCommand implementuje Command"""
        commands = []
        macro = MacroCommand(commands)
        assert isinstance(macro, Command)

    def test_macro_command_execute(self):
        """Test wykonania macro komendy"""
        manager = DocumentManager()

        # Stwórz kilka komend
        create_cmd = CreateDocumentCommand(manager, "doc1", "Test1", "Content1")
        edit_cmd = EditDocumentCommand(manager, "doc1", "Updated content")

        macro = MacroCommand([create_cmd, edit_cmd])

        # Wykonaj macro
        macro.execute()

        # Sprawdź wyniki
        assert len(manager.documents) == 1
        doc = manager.find_document("doc1")
        assert doc.content == "Updated content"

    def test_macro_command_undo(self):
        """Test cofnięcia macro komendy"""
        manager = DocumentManager()

        create_cmd = CreateDocumentCommand(manager, "doc1", "Test", "Content")
        edit_cmd = EditDocumentCommand(manager, "doc1", "Updated")

        macro = MacroCommand([create_cmd, edit_cmd])

        # Wykonaj i cofnij
        macro.execute()
        assert len(manager.documents) == 1

        macro.undo()
        assert len(manager.documents) == 0

    def test_empty_macro_command(self):
        """Test pustej macro komendy"""
        macro = MacroCommand([])

        # Nie powinno rzucać błędów
        macro.execute()
        macro.undo()


class TestDocumentManager:
    """Testy DocumentManager"""

    def test_manager_creation(self):
        """Test tworzenia managera"""
        manager = DocumentManager()

        assert len(manager.documents) == 0
        assert len(manager.command_history) == 0
        assert manager.current_command_index == -1

    def test_add_document(self):
        """Test dodawania dokumentu"""
        manager = DocumentManager()
        doc = Document("doc1", "Test", "Content")

        manager.add_document(doc)
        assert len(manager.documents) == 1
        assert manager.find_document("doc1") is doc

    def test_remove_document(self):
        """Test usuwania dokumentu"""
        manager = DocumentManager()
        doc = Document("doc1", "Test", "Content")
        manager.add_document(doc)

        removed = manager.remove_document("doc1")
        assert removed is doc
        assert len(manager.documents) == 0

    def test_find_document(self):
        """Test znajdowania dokumentu"""
        manager = DocumentManager()
        doc1 = Document("doc1", "Test1", "Content1")
        doc2 = Document("doc2", "Test2", "Content2")

        manager.add_document(doc1)
        manager.add_document(doc2)

        found = manager.find_document("doc1")
        assert found is doc1

        not_found = manager.find_document("doc3")
        assert not_found is None

    def test_execute_command(self):
        """Test wykonywania komendy przez managera"""
        manager = DocumentManager()
        command = CreateDocumentCommand(manager, "doc1", "Test", "Content")

        manager.execute_command(command)

        # Sprawdź że komenda została wykonana
        assert len(manager.documents) == 1

        # Sprawdź historię komend
        assert len(manager.command_history) == 1
        assert manager.current_command_index == 0

    def test_undo_functionality(self):
        """Test funkcjonalności undo"""
        manager = DocumentManager()

        # Wykonaj komendy
        create_cmd = CreateDocumentCommand(manager, "doc1", "Test", "Content")
        edit_cmd = EditDocumentCommand(manager, "doc1", "Updated")

        manager.execute_command(create_cmd)
        manager.execute_command(edit_cmd)

        # Sprawdź stan przed undo
        assert len(manager.documents) == 1
        assert manager.find_document("doc1").content == "Updated"

        # Cofnij ostatnią komendę (edit)
        result = manager.undo()
        assert result is True
        assert manager.find_document("doc1").content == "Content"

        # Cofnij pierwszą komendę (create)
        result = manager.undo()
        assert result is True
        assert len(manager.documents) == 0

    def test_redo_functionality(self):
        """Test funkcjonalności redo"""
        manager = DocumentManager()
        command = CreateDocumentCommand(manager, "doc1", "Test", "Content")

        # Wykonaj i cofnij
        manager.execute_command(command)
        manager.undo()
        assert len(manager.documents) == 0

        # Ponów
        result = manager.redo()
        assert result is True
        assert len(manager.documents) == 1

    def test_undo_redo_limits(self):
        """Test granic undo/redo"""
        manager = DocumentManager()

        # Nie można cofnąć bez komend
        assert manager.can_undo() is False
        assert manager.undo() is False

        # Nie można ponowić bez cofniętych komend
        assert manager.can_redo() is False
        assert manager.redo() is False

    def test_command_history_branching(self):
        """Test rozgałęzienia historii komend"""
        manager = DocumentManager()

        # Wykonaj komendy
        cmd1 = CreateDocumentCommand(manager, "doc1", "Test1", "Content1")
        cmd2 = CreateDocumentCommand(manager, "doc2", "Test2", "Content2")

        manager.execute_command(cmd1)
        manager.execute_command(cmd2)
        assert len(manager.command_history) == 2

        # Cofnij jedną
        manager.undo()
        assert manager.current_command_index == 0

        # Wykonaj nową komendę (powinno usunąć cmd2 z historii)
        cmd3 = CreateDocumentCommand(manager, "doc3", "Test3", "Content3")
        manager.execute_command(cmd3)

        # Historia powinna zawierać cmd1 i cmd3
        assert len(manager.command_history) == 2
        assert manager.current_command_index == 1

    def test_get_command_history_info(self):
        """Test informacji o historii komend"""
        manager = DocumentManager()

        # Początkowy stan
        info = manager.get_command_history_info()
        assert info["total_commands"] == 0
        assert info["current_index"] == -1
        assert info["can_undo"] is False
        assert info["can_redo"] is False

        # Po dodaniu komendy
        command = CreateDocumentCommand(manager, "doc1", "Test", "Content")
        manager.execute_command(command)

        info = manager.get_command_history_info()
        assert info["total_commands"] == 1
        assert info["current_index"] == 0
        assert info["can_undo"] is True
        assert info["can_redo"] is False


class TestCommandPattern:
    """Testy wzorca Command w kompleksowych scenariuszach"""

    def test_complex_workflow(self):
        """Test złożonego workflow z wieloma operacjami"""
        manager = DocumentManager()

        # Stwórz kilka dokumentów
        create1 = CreateDocumentCommand(manager, "doc1", "Plan", "Initial plan")
        create2 = CreateDocumentCommand(manager, "doc2", "Notes", "Meeting notes")

        manager.execute_command(create1)
        manager.execute_command(create2)

        # Edytuj dokumenty
        edit1 = EditDocumentCommand(manager, "doc1", "Updated plan")
        edit2 = EditDocumentCommand(manager, "doc2", "Updated notes")

        manager.execute_command(edit1)
        manager.execute_command(edit2)

        # Usuń jeden dokument
        delete_cmd = DeleteDocumentCommand(manager, "doc2")
        manager.execute_command(delete_cmd)

        # Sprawdź stan
        assert len(manager.documents) == 1
        assert manager.find_document("doc1").content == "Updated plan"
        assert manager.find_document("doc2") is None

        # Cofnij wszystkie operacje
        for _ in range(5):
            manager.undo()

        # Powinniśmy wrócić do stanu początkowego
        assert len(manager.documents) == 0

    def test_macro_with_manager(self):
        """Test macro komendy z managerem"""
        manager = DocumentManager()

        # Stwórz macro komendę
        create_cmd = CreateDocumentCommand(manager, "doc1", "Test", "Content")
        edit_cmd = EditDocumentCommand(manager, "doc1", "Updated content")

        macro = MacroCommand([create_cmd, edit_cmd])

        # Wykonaj przez managera
        manager.execute_command(macro)

        # Sprawdź wynik
        assert len(manager.documents) == 1
        assert manager.find_document("doc1").content == "Updated content"

        # Cofnij macro
        manager.undo()
        assert len(manager.documents) == 0

    def test_undo_redo_cycle(self):
        """Test cyklu undo/redo"""
        manager = DocumentManager()
        command = CreateDocumentCommand(manager, "doc1", "Test", "Content")

        # Wykonaj -> cofnij -> ponów kilka razy
        for _ in range(3):
            manager.execute_command(command)
            assert len(manager.documents) == 1

            manager.undo()
            assert len(manager.documents) == 0

            manager.redo()
            assert len(manager.documents) == 1

            manager.undo()  # Przygotuj do następnej iteracji

    def test_command_independence(self):
        """Test niezależności komend"""
        manager1 = DocumentManager()
        manager2 = DocumentManager()

        # Te same komendy na różnych managerach
        cmd1 = CreateDocumentCommand(manager1, "doc1", "Test1", "Content1")
        cmd2 = CreateDocumentCommand(manager2, "doc1", "Test2", "Content2")

        cmd1.execute()
        cmd2.execute()

        # Każdy manager powinien mieć swój dokument
        assert len(manager1.documents) == 1
        assert len(manager2.documents) == 1
        assert manager1.find_document("doc1").content == "Content1"
        assert manager2.find_document("doc1").content == "Content2"


class TestDemonstrateCommandPattern:
    """Testy demonstracji wzorca Command (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_command_pattern(self):
        """Test demonstracji wzorca Command"""
        results = demonstrate_command_pattern()

        assert isinstance(results, dict)
        assert "operations_performed" in results
        assert "undo_operations" in results
        assert "final_state" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
