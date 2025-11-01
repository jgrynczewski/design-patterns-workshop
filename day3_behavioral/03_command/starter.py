# %% About
# - Name: Command - Undo/Redo Operations
# - Difficulty: medium
# - Lines: 20
# - Minutes: 15
# - Focus: Command pattern - encapsulating requests as objects

# %% Description
"""
Implementuj wzorzec Command do systemu undo/redo operacji na dokumentach
w workflow system.

Zadanie: Enkapsuluj operacje jako obiekty z możliwością cofania
"""

# %% Hints
# - Command interface definiuje execute() i undo()
# - Każda komenda pamięta stan przed wykonaniem
# - DocumentManager przechowuje historię komend w stosie
# - Undo cofa ostatnią komendę, redo ją ponownie wykonuje

# %% Doctests
"""
>>> # Test tworzenia dokumentu
>>> manager = DocumentManager()
>>> doc = Document("1", "Plan projektu", "Wstępny plan")
>>> manager.add_document(doc)
>>> len(manager.documents)
1

>>> # Test komendy tworzenia
>>> create_cmd = CreateDocumentCommand(manager, "2", "Nowy dokument", "Treść")
>>> manager.execute_command(create_cmd)
>>> len(manager.documents)
2

>>> # Test undo tworzenia
>>> manager.undo()
>>> len(manager.documents)
1

>>> # Test edycji z undo
>>> edit_cmd = EditDocumentCommand(manager, "1", "Zaktualizowana treść")
>>> manager.execute_command(edit_cmd)
>>> manager.find_document("1").content
'Zaktualizowana treść'
>>> manager.undo()
>>> manager.find_document("1").content
'Wstępny plan'
"""

# %% Imports
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime


# %% Document Class (już gotowe)

class Document:
    """Dokument w workflow system"""

    def __init__(self, doc_id: str, title: str, content: str = ""):
        """Inicjalizuj dokument"""
        self.doc_id = doc_id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.modified_at = datetime.now()

    def update_content(self, new_content: str) -> str:
        """Zaktualizuj treść i zwróć poprzednią"""
        old_content = self.content
        self.content = new_content
        self.modified_at = datetime.now()
        return old_content


# %% TODO: Implement Command Interface

class Command(ABC):
    """Interface dla wszystkich komend"""

    @abstractmethod
    def execute(self) -> None:
        """Wykonaj komendę"""
        pass

    @abstractmethod
    def undo(self) -> None:
        """Cofnij komendę"""
        pass


# %% TODO: Implement Concrete Commands

class CreateDocumentCommand:
    """Komenda tworzenia nowego dokumentu"""

    def __init__(self, manager: 'DocumentManager', doc_id: str, title: str, content: str = ""):
        """Inicjalizuj komendę tworzenia"""
        # TODO:
        # self.manager = ...
        # self.doc_id = ...
        # self.title = ...
        # self.content = ...
        # self.created_document = None  # Referencja do utworzonego dokumentu
        pass

    def execute(self) -> None:
        """Wykonaj tworzenie dokumentu"""
        # TODO:
        # 1. Stwórz nowy dokument
        # 2. Dodaj do managera
        # 3. Zapisz referencję do dokumentu
        pass

    def undo(self) -> None:
        """Cofnij tworzenie dokumentu"""
        # TODO: Usuń dokument z managera
        pass


class EditDocumentCommand:
    """Komenda edycji dokumentu"""

    def __init__(self, manager: 'DocumentManager', doc_id: str, new_content: str):
        """Inicjalizuj komendę edycji"""
        # TODO:
        # self.manager = ...
        # self.doc_id = ...
        # self.new_content = ...
        # self.old_content = None  # Zapamięta poprzednią treść
        pass

    def execute(self) -> None:
        """Wykonaj edycję dokumentu"""
        # TODO:
        # 1. Znajdź dokument
        # 2. Zapisz starą treść
        # 3. Ustaw nową treść
        pass

    def undo(self) -> None:
        """Cofnij edycję dokumentu"""
        # TODO: Przywróć starą treść
        pass


class DeleteDocumentCommand:
    """Komenda usuwania dokumentu"""

    def __init__(self, manager: 'DocumentManager', doc_id: str):
        """Inicjalizuj komendę usuwania"""
        # TODO:
        # self.manager = ...
        # self.doc_id = ...
        # self.deleted_document = None  # Zapamięta usunięty dokument
        pass

    def execute(self) -> None:
        """Wykonaj usuwanie dokumentu"""
        # TODO:
        # 1. Znajdź dokument
        # 2. Zapisz go do self.deleted_document
        # 3. Usuń z managera
        pass

    def undo(self) -> None:
        """Cofnij usuwanie dokumentu"""
        # TODO: Przywróć usunięty dokument
        pass


# %% TODO: Implement Macro Command

class MacroCommand:
    """Komenda grupująca wiele operacji"""

    def __init__(self, commands: List[Command]):
        """Inicjalizuj macro komendę"""
        # TODO: self.commands = commands
        pass

    def execute(self) -> None:
        """Wykonaj wszystkie komendy w kolejności"""
        # TODO: Wykonaj każdą komendę z listy
        pass

    def undo(self) -> None:
        """Cofnij wszystkie komendy w odwrotnej kolejności"""
        # TODO: Cofnij komendy w odwrotnej kolejności
        pass


# %% TODO: Implement DocumentManager (Command Invoker)

class DocumentManager:
    """Manager dokumentów z obsługą undo/redo"""

    def __init__(self):
        """Inicjalizuj manager"""
        # TODO:
        # self.documents = []  # Lista dokumentów
        # self.command_history = []  # Historia komend
        # self.current_command_index = -1  # Wskaźnik aktualnej komendy
        pass

    def add_document(self, document: Document) -> None:
        """Dodaj dokument do kolekcji"""
        # TODO: Dodaj dokument do self.documents
        pass

    def remove_document(self, doc_id: str) -> Optional[Document]:
        """Usuń dokument z kolekcji"""
        # TODO:
        # 1. Znajdź dokument po ID
        # 2. Usuń go z listy
        # 3. Zwróć usunięty dokument lub None
        pass

    def find_document(self, doc_id: str) -> Optional[Document]:
        """Znajdź dokument po ID"""
        # TODO: Znajdź i zwróć dokument lub None
        pass

    def execute_command(self, command: Command) -> None:
        """Wykonaj komendę i dodaj do historii"""
        # TODO:
        # 1. Wykonaj komendę
        # 2. Usuń wszystkie komendy po current_command_index (dla nowej ścieżki)
        # 3. Dodaj komendę do historii
        # 4. Zaktualizuj current_command_index
        pass

    def undo(self) -> bool:
        """Cofnij ostatnią komendę"""
        # TODO:
        # 1. Sprawdź czy można cofnąć
        # 2. Cofnij komendę na current_command_index
        # 3. Zmniejsz current_command_index
        # 4. Zwróć True jeśli cofnięto, False w przeciwnym razie
        pass

    def redo(self) -> bool:
        """Ponów cofniętą komendę"""
        # TODO:
        # 1. Sprawdź czy można ponowić
        # 2. Zwiększ current_command_index
        # 3. Wykonaj komendę na current_command_index
        # 4. Zwróć True jeśli ponowiono, False w przeciwnym razie
        pass

    def can_undo(self) -> bool:
        """Sprawdź czy można cofnąć"""
        # TODO: Zwróć czy current_command_index >= 0
        pass

    def can_redo(self) -> bool:
        """Sprawdź czy można ponowić"""
        # TODO: Zwróć czy current_command_index < len(command_history) - 1
        pass

    def get_command_history_info(self) -> Dict[str, Any]:
        """Zwróć informacje o historii komend"""
        # TODO: Zwróć dict z:
        # - "total_commands": liczba komend w historii
        # - "current_index": aktualny indeks
        # - "can_undo": czy można cofnąć
        # - "can_redo": czy można ponowić
        pass


# %% Example Usage (Optional)

def demonstrate_command_pattern():
    """Demonstracja wzorca Command"""
    # TODO (Opcjonalne):
    # 1. Stwórz DocumentManager
    # 2. Wykonaj kilka operacji (create, edit, delete)
    # 3. Przetestuj undo/redo
    # 4. Przetestuj macro command
    # 5. Zwróć wyniki
    pass
