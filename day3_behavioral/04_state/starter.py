# %% About
# - Name: State - Workflow States
# - Difficulty: medium
# - Lines: 22
# - Minutes: 15
# - Focus: State pattern - object behavior changes with internal state

# %% Description
"""
Implementuj wzorzec State do zarządzania stanami dokumentów w workflow,
gdzie dokument zmienia zachowanie w zależności od stanu.

Zadanie: Enkapsuluj stany jako obiekty z właściwymi przejściami
"""

# %% Hints
# - DocumentState interface definiuje akcje dostępne w stanie
# - Każdy concrete state implementuje dozwolone operacje
# - DocumentContext deleguje akcje do aktualnego stanu
# - Stan może zmieniać context na następny stan

# %% Doctests
"""
>>> # Test podstawowego workflow dokumentu
>>> doc = DocumentContext("Project Plan")
>>> doc.get_current_state_name()
'draft'
>>> doc.content
''

>>> # Test edycji w stanie draft
>>> doc.edit("Initial project outline")
>>> doc.content
'Initial project outline'

>>> # Test przejścia do review
>>> doc.submit_for_review()
>>> doc.get_current_state_name()
'review'

>>> # Test że nie można edytować w review
>>> try:
...     doc.edit("New content")
... except OperationNotAllowedError as e:
...     print("Cannot edit in review state")
Cannot edit in review state

>>> # Test zatwierdzenia
>>> doc.approve()
>>> doc.get_current_state_name()
'approved'
"""

# %% Imports
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


# %% Custom Exception (już gotowe)

class OperationNotAllowedError(Exception):
    """Wyjątek dla niedozwolonych operacji w danym stanie"""
    pass


# %% Document State Types (już gotowe)

class DocumentStateType(Enum):
    """Typy stanów dokumentu"""
    DRAFT = "draft"
    REVIEW = "review"
    APPROVED = "approved"
    PUBLISHED = "published"


# %% TODO: Implement DocumentState Interface

class DocumentState(ABC):
    """Interface dla stanów dokumentu"""

    @abstractmethod
    def edit(self, context: 'DocumentContext', new_content: str) -> None:
        """Edytuj treść dokumentu"""
        pass

    @abstractmethod
    def submit_for_review(self, context: 'DocumentContext') -> None:
        """Wyślij dokument do przeglądu"""
        pass

    @abstractmethod
    def approve(self, context: 'DocumentContext') -> None:
        """Zatwierdź dokument"""
        pass

    @abstractmethod
    def reject(self, context: 'DocumentContext', reason: str = "") -> None:
        """Odrzuć dokument"""
        pass

    @abstractmethod
    def publish(self, context: 'DocumentContext') -> None:
        """Opublikuj dokument"""
        pass

    @abstractmethod
    def get_state_name(self) -> str:
        """Zwróć nazwę stanu"""
        pass


# %% TODO: Implement Concrete States

class DraftState:
    """Stan projektu - można edytować i wysłać do przeglądu"""

    def edit(self, context: 'DocumentContext', new_content: str) -> None:
        """Edytuj treść (dozwolone w draft)"""
        # TODO: Ustaw context.content = new_content
        pass

    def submit_for_review(self, context: 'DocumentContext') -> None:
        """Wyślij do przeglądu"""
        # TODO:
        # 1. Sprawdź czy content nie jest pusty
        # 2. Zmień stan na ReviewState()
        pass

    def approve(self, context: 'DocumentContext') -> None:
        """Nie można zatwierdzić w draft"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def reject(self, context: 'DocumentContext', reason: str = "") -> None:
        """Nie można odrzucić w draft"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def publish(self, context: 'DocumentContext') -> None:
        """Nie można opublikować w draft"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def get_state_name(self) -> str:
        """Zwróć nazwę stanu"""
        # TODO: Zwróć "draft"
        pass


class ReviewState:
    """Stan przeglądu - można zatwierdzić lub odrzucić"""

    def edit(self, context: 'DocumentContext', new_content: str) -> None:
        """Nie można edytować w review"""
        # TODO: Rzuć OperationNotAllowedError("Cannot edit document in review state")
        pass

    def submit_for_review(self, context: 'DocumentContext') -> None:
        """Już w review"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def approve(self, context: 'DocumentContext') -> None:
        """Zatwierdź dokument"""
        # TODO: Zmień stan na ApprovedState()
        pass

    def reject(self, context: 'DocumentContext', reason: str = "") -> None:
        """Odrzuć dokument"""
        # TODO:
        # 1. Ustaw context.rejection_reason = reason
        # 2. Zmień stan na DraftState() (wraca do edycji)
        pass

    def publish(self, context: 'DocumentContext') -> None:
        """Nie można opublikować bez zatwierdzenia"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def get_state_name(self) -> str:
        """Zwróć nazwę stanu"""
        # TODO: Zwróć "review"
        pass


class ApprovedState:
    """Stan zatwierdzony - można opublikować"""

    def edit(self, context: 'DocumentContext', new_content: str) -> None:
        """Nie można edytować zatwierdzonego"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def submit_for_review(self, context: 'DocumentContext') -> None:
        """Już zatwierdzony"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def approve(self, context: 'DocumentContext') -> None:
        """Już zatwierdzony"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def reject(self, context: 'DocumentContext', reason: str = "") -> None:
        """Nie można odrzucić zatwierdzonego"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def publish(self, context: 'DocumentContext') -> None:
        """Opublikuj dokument"""
        # TODO: Zmień stan na PublishedState()
        pass

    def get_state_name(self) -> str:
        """Zwróć nazwę stanu"""
        # TODO: Zwróć "approved"
        pass


class PublishedState:
    """Stan opublikowany - tylko do odczytu"""

    def edit(self, context: 'DocumentContext', new_content: str) -> None:
        """Nie można edytować opublikowanego"""
        # TODO: Rzuć OperationNotAllowedError("Cannot edit published document")
        pass

    def submit_for_review(self, context: 'DocumentContext') -> None:
        """Już opublikowany"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def approve(self, context: 'DocumentContext') -> None:
        """Już opublikowany"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def reject(self, context: 'DocumentContext', reason: str = "") -> None:
        """Nie można odrzucić opublikowanego"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def publish(self, context: 'DocumentContext') -> None:
        """Już opublikowany"""
        # TODO: Rzuć OperationNotAllowedError
        pass

    def get_state_name(self) -> str:
        """Zwróć nazwę stanu"""
        # TODO: Zwróć "published"
        pass


# %% TODO: Implement DocumentContext

class DocumentContext:
    """Context zarządzający stanem dokumentu"""

    def __init__(self, title: str):
        """Inicjalizuj dokument w stanie draft"""
        # TODO:
        # self.title = title
        # self.content = ""
        # self.rejection_reason = ""
        # self._state = DraftState()  # Początkowy stan
        pass

    def set_state(self, state: DocumentState) -> None:
        """Ustaw nowy stan"""
        # TODO: self._state = state
        pass

    def edit(self, new_content: str) -> None:
        """Deleguj edycję do aktualnego stanu"""
        # TODO: self._state.edit(self, new_content)
        pass

    def submit_for_review(self) -> None:
        """Deleguj wysłanie do przeglądu"""
        # TODO: self._state.submit_for_review(self)
        pass

    def approve(self) -> None:
        """Deleguj zatwierdzenie"""
        # TODO: self._state.approve(self)
        pass

    def reject(self, reason: str = "") -> None:
        """Deleguj odrzucenie"""
        # TODO: self._state.reject(self, reason)
        pass

    def publish(self) -> None:
        """Deleguj publikację"""
        # TODO: self._state.publish(self)
        pass

    def get_current_state_name(self) -> str:
        """Zwróć nazwę aktualnego stanu"""
        # TODO: return self._state.get_state_name()
        pass

    def can_edit(self) -> bool:
        """Sprawdź czy można edytować w aktualnym stanie"""
        # TODO:
        # try:
        #     # Spróbuj wywołać edit z pustym stringiem (test)
        #     return True/False w zależności od stanu
        # except OperationNotAllowedError:
        #     return False
        pass

    def get_available_actions(self) -> list:
        """Zwróć listę dostępnych akcji w aktualnym stanie"""
        # TODO: Zwróć listę stringów z dostępnymi akcjami
        # np. ["edit", "submit_for_review"] dla draft
        pass

    def get_document_info(self) -> dict:
        """Zwróć informacje o dokumencie"""
        # TODO: Zwróć dict z:
        # - "title": tytuł dokumentu
        # - "current_state": nazwa aktualnego stanu
        # - "content_length": długość treści
        # - "can_edit": czy można edytować
        # - "rejection_reason": powód odrzucenia (jeśli był)
        pass


# %% Example Usage (Optional)

def demonstrate_document_workflow():
    """Demonstracja workflow dokumentu"""
    # TODO (Opcjonalne):
    # 1. Stwórz dokument
    # 2. Przejdź przez cały workflow (draft -> review -> approved -> published)
    # 3. Przetestuj niedozwolone operacje
    # 4. Zwróć wyniki
    pass
