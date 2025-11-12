# %% About
# - Name: Memento - Workflow Snapshots
# - Difficulty: medium
# - Lines: 24
# - Minutes: 15
# - Focus: Memento pattern - capturing and restoring object state

# %% Description
"""
Implementuj wzorzec Memento do systemu snapshots workflow,
gdzie możesz zapisywać i przywracać stany dokumentów i projektów.

Zadanie: Enkapsuluj snapshots stanu w memento objects
"""

# %% Hints
# - Memento przechowuje immutable snapshot stanu
# - Originator tworzy mementos i może przywrócić stan
# - Caretaker zarządza kolekcją mementos
# - Snapshot zawiera timestamp i metadata

# %% Doctests
"""
>>> # Test podstawowych snapshots dokumentu
>>> doc = DocumentOriginator("Project Plan")
>>> caretaker = WorkflowCaretaker()
>>> doc.edit("Initial content")
>>> caretaker.save_snapshot(doc, "Initial version")
>>> len(caretaker.snapshots)
1

>>> # Test edycji i rollback
>>> doc.edit("Updated content")
>>> doc.content
'Updated content'
>>> caretaker.restore_snapshot(doc, "Initial version")
>>> doc.content
'Initial content'

>>> # Test named snapshots
>>> doc.edit("Final version")
>>> caretaker.create_milestone(doc, "Release v1.0", ["release", "v1.0"])
>>> milestone = caretaker.get_milestone("Release v1.0")
>>> milestone is not None
True

>>> # Test project snapshots
>>> project = ProjectOriginator("WebApp")
>>> project.add_document("README", "Project description")
>>> project.set_status("In Progress")
>>> caretaker.save_project_snapshot(project, "Sprint 1 start")
>>> len(caretaker.project_snapshots)
1
"""

# %% Imports
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from datetime import datetime
from copy import deepcopy


# %% TODO: Implement Memento Classes

class DocumentMemento:
    """Memento przechowujące stan dokumentu"""

    def __init__(self, title: str, content: str, metadata: Dict[str, Any], version: int):
        """Inicjalizuj document memento"""
        # TODO:
        # self._title = title  # Użyj _ dla immutability
        # self._content = content
        # self._metadata = deepcopy(metadata)
        # self._version = version
        # self._timestamp = datetime.now()
        pass

    def get_title(self) -> str:
        """Zwróć tytuł (read-only access)"""
        # TODO: return self._title
        pass

    def get_content(self) -> str:
        """Zwróć treść (read-only access)"""
        # TODO: return self._content
        pass

    def get_metadata(self) -> Dict[str, Any]:
        """Zwróć kopię metadanych"""
        # TODO: return deepcopy(self._metadata)
        pass

    def get_version(self) -> int:
        """Zwróć wersję"""
        # TODO: return self._version
        pass

    def get_timestamp(self) -> datetime:
        """Zwróć timestamp utworzenia"""
        # TODO: return self._timestamp
        pass


class ProjectMemento:
    """Memento przechowujące stan projektu"""

    def __init__(self, name: str, documents: Dict[str, Dict], status: str,
                 settings: Dict[str, Any]):
        """Inicjalizuj project memento"""
        # TODO:
        # self._name = name
        # self._documents = deepcopy(documents)  # Deep copy dla bezpieczeństwa
        # self._status = status
        # self._settings = deepcopy(settings)
        # self._timestamp = datetime.now()
        pass

    def get_name(self) -> str:
        """Zwróć nazwę projektu"""
        # TODO: return self._name
        pass

    def get_documents(self) -> Dict[str, Dict]:
        """Zwróć kopię dokumentów"""
        # TODO: return deepcopy(self._documents)
        pass

    def get_status(self) -> str:
        """Zwróć status projektu"""
        # TODO: return self._status
        pass

    def get_settings(self) -> Dict[str, Any]:
        """Zwróć kopię ustawień"""
        # TODO: return deepcopy(self._settings)
        pass

    def get_timestamp(self) -> datetime:
        """Zwróć timestamp utworzenia"""
        # TODO: return self._timestamp
        pass


# %% TODO: Implement Originator Classes

class DocumentOriginator:
    """Originator dla dokumentów - zarządza stanem i tworzy mementos"""

    def __init__(self, title: str):
        """Inicjalizuj document originator"""
        # TODO:
        # self.title = title
        # self.content = ""
        # self.metadata = {}
        # self.version = 1
        # self.last_modified = datetime.now()
        pass

    def edit(self, new_content: str) -> None:
        """Edytuj treść dokumentu"""
        # TODO:
        # self.content = new_content
        # self.version += 1
        # self.last_modified = datetime.now()
        pass

    def update_metadata(self, key: str, value: Any) -> None:
        """Zaktualizuj metadane"""
        # TODO:
        # self.metadata[key] = value
        # self.last_modified = datetime.now()
        pass

    def create_memento(self) -> DocumentMemento:
        """Stwórz memento z aktualnym stanem"""
        # TODO: return DocumentMemento(self.title, self.content, self.metadata, self.version)
        pass

    def restore_from_memento(self, memento: DocumentMemento) -> None:
        """Przywróć stan z memento"""
        # TODO:
        # self.title = memento.get_title()
        # self.content = memento.get_content()
        # self.metadata = memento.get_metadata()
        # self.version = memento.get_version()
        # self.last_modified = datetime.now()  # Update restore time
        pass

    def get_state_summary(self) -> Dict[str, Any]:
        """Zwróć podsumowanie aktualnego stanu"""
        # TODO: Zwróć dict z title, content_length, version, last_modified
        pass


class ProjectOriginator:
    """Originator dla projektów - zarządza stanem projektu"""

    def __init__(self, name: str):
        """Inicjalizuj project originator"""
        # TODO:
        # self.name = name
        # self.documents = {}  # Dict[str, Dict] - nazwa -> dane dokumentu
        # self.status = "New"
        # self.settings = {"theme": "default", "auto_save": True}
        # self.created_at = datetime.now()
        # self.last_modified = datetime.now()
        pass

    def add_document(self, name: str, content: str) -> None:
        """Dodaj dokument do projektu"""
        # TODO:
        # self.documents[name] = {
        #     "content": content,
        #     "created_at": datetime.now(),
        #     "version": 1
        # }
        # self.last_modified = datetime.now()
        pass

    def update_document(self, name: str, content: str) -> None:
        """Zaktualizuj dokument w projekcie"""
        # TODO:
        # if name in self.documents:
        #     self.documents[name]["content"] = content
        #     self.documents[name]["version"] += 1
        #     self.last_modified = datetime.now()
        pass

    def remove_document(self, name: str) -> None:
        """Usuń dokument z projektu"""
        # TODO:
        # if name in self.documents:
        #     del self.documents[name]
        #     self.last_modified = datetime.now()
        pass

    def set_status(self, status: str) -> None:
        """Ustaw status projektu"""
        # TODO:
        # self.status = status
        # self.last_modified = datetime.now()
        pass

    def update_setting(self, key: str, value: Any) -> None:
        """Zaktualizuj ustawienie projektu"""
        # TODO:
        # self.settings[key] = value
        # self.last_modified = datetime.now()
        pass

    def create_memento(self) -> ProjectMemento:
        """Stwórz memento z aktualnym stanem projektu"""
        # TODO: return ProjectMemento(self.name, self.documents, self.status, self.settings)
        pass

    def restore_from_memento(self, memento: ProjectMemento) -> None:
        """Przywróć stan projektu z memento"""
        # TODO:
        # self.name = memento.get_name()
        # self.documents = memento.get_documents()
        # self.status = memento.get_status()
        # self.settings = memento.get_settings()
        # self.last_modified = datetime.now()
        pass

    def get_project_summary(self) -> Dict[str, Any]:
        """Zwróć podsumowanie projektu"""
        # TODO: Zwróć dict z name, document_count, status, last_modified
        pass


# %% TODO: Implement Snapshot Container

class SnapshotContainer:
    """Kontener dla pojedynczego snapshot z metadata"""

    def __init__(self, memento: Any, description: str, tags: List[str] = None):
        """Inicjalizuj snapshot container"""
        # TODO:
        # self.memento = memento
        # self.description = description
        # self.tags = tags or []
        # self.created_at = datetime.now()
        # self.snapshot_id = f"SNAP_{int(self.created_at.timestamp())}"
        pass

    def has_tag(self, tag: str) -> bool:
        """Sprawdź czy snapshot ma określony tag"""
        # TODO: return tag in self.tags
        pass

    def matches_description(self, keyword: str) -> bool:
        """Sprawdź czy opis zawiera keyword"""
        # TODO: return keyword.lower() in self.description.lower()
        pass


# %% TODO: Implement WorkflowCaretaker

class WorkflowCaretaker:
    """Caretaker zarządzający snapshots workflow"""

    def __init__(self):
        """Inicjalizuj workflow caretaker"""
        # TODO:
        # self.snapshots = []  # Lista SnapshotContainer dla dokumentów
        # self.project_snapshots = []  # Lista SnapshotContainer dla projektów
        # self.named_snapshots = {}  # Dict[str, SnapshotContainer] - milestones
        # self.auto_save_enabled = True
        pass

    def save_snapshot(self, originator: DocumentOriginator, description: str) -> str:
        """Zapisz snapshot dokumentu"""
        # TODO:
        # 1. Stwórz memento z originator.create_memento()
        # 2. Stwórz SnapshotContainer
        # 3. Dodaj do self.snapshots
        # 4. Zwróć snapshot_id
        pass

    def save_project_snapshot(self, originator: ProjectOriginator, description: str) -> str:
        """Zapisz snapshot projektu"""
        # TODO:
        # 1. Stwórz memento z originator.create_memento()
        # 2. Stwórz SnapshotContainer
        # 3. Dodaj do self.project_snapshots
        # 4. Zwróć snapshot_id
        pass

    def restore_snapshot(self, originator: DocumentOriginator, description: str) -> bool:
        """Przywróć snapshot dokumentu po opisie"""
        # TODO:
        # 1. Znajdź snapshot po description
        # 2. Jeśli znaleziony - wywołaj originator.restore_from_memento
        # 3. Zwróć True/False
        pass

    def restore_project_snapshot(self, originator: ProjectOriginator, description: str) -> bool:
        """Przywróć snapshot projektu po opisie"""
        # TODO:
        # 1. Znajdź project snapshot po description
        # 2. Jeśli znaleziony - wywołaj originator.restore_from_memento
        # 3. Zwróć True/False
        pass

    def create_milestone(self, originator: DocumentOriginator, name: str, tags: List[str] = None) -> str:
        """Stwórz named milestone snapshot"""
        # TODO:
        # 1. Stwórz memento
        # 2. Stwórz SnapshotContainer z tags
        # 3. Dodaj do self.named_snapshots[name]
        # 4. Zwróć snapshot_id
        pass

    def restore_milestone(self, originator: DocumentOriginator, name: str) -> bool:
        """Przywróć named milestone"""
        # TODO:
        # 1. Sprawdź czy name w self.named_snapshots
        # 2. Przywróć z memento
        # 3. Zwróć True/False
        pass

    def get_milestone(self, name: str) -> Optional[SnapshotContainer]:
        """Zwróć milestone snapshot"""
        # TODO: return self.named_snapshots.get(name)
        pass

    def list_snapshots_by_tag(self, tag: str) -> List[SnapshotContainer]:
        """Zwróć snapshots z określonym tagiem"""
        # TODO: Przeszukaj wszystkie snapshots i zwróć te z tagiem
        pass

    def cleanup_old_snapshots(self, max_age_days: int) -> int:
        """Usuń stare snapshots (nie milestones)"""
        # TODO:
        # 1. Sprawdź age każdego snapshot
        # 2. Usuń te starsze niż max_age_days
        # 3. Zwróć liczbę usuniętych
        pass

    def get_caretaker_statistics(self) -> Dict[str, Any]:
        """Zwróć statystyki caretaker"""
        # TODO: Zwróć dict z:
        # - "total_snapshots": liczba document snapshots
        # - "total_project_snapshots": liczba project snapshots
        # - "named_snapshots": liczba milestones
        # - "oldest_snapshot": timestamp najstarszego
        # - "newest_snapshot": timestamp najnowszego
        pass


# %% Example Usage (Optional)

def demonstrate_workflow_snapshots():
    """Demonstracja workflow snapshots"""
    # TODO (Opcjonalne):
    # 1. Stwórz caretaker i originators
    # 2. Symuluj typowy workflow z zapisywaniem snapshots
    # 3. Przetestuj różne scenariusze restore
    # 4. Pokaż milestones i tagging
    # 5. Zwróć statystyki
    pass
