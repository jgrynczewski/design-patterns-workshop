# %% About
# - Name: Mediator - Team Collaboration
# - Difficulty: medium
# - Lines: 22
# - Minutes: 15
# - Focus: Mediator pattern - centralized communication between objects

# %% Description
"""
Implementuj wzorzec Mediator do systemu komunikacji zespołu w workflow,
gdzie członkowie zespołu komunikują się przez centralny mediator.

Zadanie: Enkapsuluj komunikację zespołu w mediator object
"""

# %% Hints
# - TeamMediator interface definiuje metody komunikacyjne
# - WorkflowMediator zarządza wszystką komunikacją
# - TeamMember zna tylko mediator, nie innych members
# - Mediator może filtrować wiadomości na podstawie roli

# %% Doctests
"""
>>> # Test podstawowej komunikacji przez mediator
>>> mediator = WorkflowMediator()
>>> dev = Developer("John", mediator)
>>> pm = ProjectManager("Sarah", mediator)
>>> mediator.add_team_member(dev)
>>> mediator.add_team_member(pm)

>>> # Test wysyłania wiadomości
>>> dev.send_message("Feature completed", MessageType.STATUS_UPDATE)
>>> len(mediator.message_history)
1

>>> # Test otrzymywania wiadomości
>>> pm.send_message("Sprint planning tomorrow", MessageType.ANNOUNCEMENT)
>>> len(dev.received_messages)
1

>>> # Test filtrowania wiadomości
>>> dev.send_message("Need UI feedback", MessageType.QUESTION)
>>> # PM powinien otrzymać question, ale developer nie powinien otrzymywać własnej wiadomości
>>> len(pm.received_messages)
2
"""

# %% Imports
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime


# %% Message Types and Roles (już gotowe)

class MessageType(Enum):
    """Typy wiadomości w zespole"""
    TASK_ASSIGNMENT = "task_assignment"
    STATUS_UPDATE = "status_update"
    QUESTION = "question"
    ANNOUNCEMENT = "announcement"
    REVIEW_REQUEST = "review_request"


class TeamRole(Enum):
    """Role członków zespołu"""
    DEVELOPER = "developer"
    DESIGNER = "designer"
    PROJECT_MANAGER = "project_manager"
    TESTER = "tester"


# %% Message Class (już gotowe)

class Message:
    """Wiadomość w systemie komunikacji"""

    def __init__(self, sender: str, content: str, message_type: MessageType,
                 target_roles: List[TeamRole] = None):
        """Inicjalizuj wiadomość"""
        self.sender = sender
        self.content = content
        self.message_type = message_type
        self.target_roles = target_roles or []
        self.timestamp = datetime.now()
        self.message_id = f"MSG_{int(self.timestamp.timestamp())}"

    def __str__(self):
        return f"[{self.message_type.value}] {self.sender}: {self.content}"


# %% TODO: Implement TeamMediator Interface

class TeamMediator(ABC):
    """Interface dla mediator zespołu"""

    @abstractmethod
    def send_message(self, sender: 'TeamMember', content: str,
                     message_type: MessageType, target_roles: List[TeamRole] = None) -> None:
        """Wyślij wiadomość przez mediator"""
        pass

    @abstractmethod
    def add_team_member(self, member: 'TeamMember') -> None:
        """Dodaj członka zespołu"""
        pass

    @abstractmethod
    def remove_team_member(self, member: 'TeamMember') -> None:
        """Usuń członka zespołu"""
        pass

    @abstractmethod
    def notify_team_members(self, message: Message) -> None:
        """Powiadom odpowiednich członków zespołu"""
        pass


# %% TODO: Implement WorkflowMediator

class WorkflowMediator:
    """Konkretny mediator dla workflow zespołu"""

    def __init__(self):
        """Inicjalizuj workflow mediator"""
        # TODO:
        # self.team_members = []  # Lista członków zespołu
        # self.message_history = []  # Historia wszystkich wiadomości
        # self.message_filters = {}  # Filtry wiadomości dla różnych ról
        pass

    def send_message(self, sender: 'TeamMember', content: str,
                     message_type: MessageType, target_roles: List[TeamRole] = None) -> None:
        """Wyślij wiadomość przez mediator"""
        # TODO:
        # 1. Stwórz Message object
        # 2. Dodaj do message_history
        # 3. Wywołaj notify_team_members
        pass

    def add_team_member(self, member: 'TeamMember') -> None:
        """Dodaj członka zespołu"""
        # TODO: Dodaj member do team_members (jeśli nie ma już)
        pass

    def remove_team_member(self, member: 'TeamMember') -> None:
        """Usuń członka zespołu"""
        # TODO: Usuń member z team_members
        pass

    def notify_team_members(self, message: Message) -> None:
        """Powiadom odpowiednich członków zespołu"""
        # TODO:
        # 1. Dla każdego team member sprawdź czy powinien otrzymać wiadomość
        # 2. Sprawdź target_roles (jeśli określone)
        # 3. Sprawdź czy member != sender (nie wysyłaj do siebie)
        # 4. Wywołaj member.receive_message(message)
        pass

    def should_receive_message(self, member: 'TeamMember', message: Message) -> bool:
        """Sprawdź czy member powinien otrzymać wiadomość"""
        # TODO:
        # 1. Sprawdź czy member != sender
        # 2. Sprawdź target_roles (jeśli puste - wszyscy otrzymują)
        # 3. Sprawdź filtry specyficzne dla roli
        # 4. Zwróć True/False
        pass

    def get_message_statistics(self) -> Dict:
        """Zwróć statystyki wiadomości"""
        # TODO: Zwróć dict z:
        # - "total_messages": liczba wiadomości
        # - "messages_by_type": liczba wiadomości per typ
        # - "messages_by_sender": liczba wiadomości per sender
        # - "active_team_members": liczba aktywnych członków
        pass


# %% TODO: Implement TeamMember Abstract Class

class TeamMember(ABC):
    """Abstract base class dla członków zespołu"""

    def __init__(self, name: str, mediator: TeamMediator, role: TeamRole):
        """Inicjalizuj członka zespołu"""
        # TODO:
        # self.name = name
        # self.mediator = mediator
        # self.role = role
        # self.received_messages = []
        # self.sent_messages_count = 0
        pass

    def send_message(self, content: str, message_type: MessageType,
                     target_roles: List[TeamRole] = None) -> None:
        """Wyślij wiadomość przez mediator"""
        # TODO:
        # 1. Zwiększ sent_messages_count
        # 2. Wywołaj mediator.send_message
        pass

    def receive_message(self, message: Message) -> None:
        """Otrzymaj wiadomość od mediator"""
        # TODO:
        # 1. Dodaj message do received_messages
        # 2. Wywołaj process_message
        pass

    @abstractmethod
    def process_message(self, message: Message) -> None:
        """Przetworz otrzymaną wiadomość (role-specific logic)"""
        pass

    def get_message_stats(self) -> Dict:
        """Zwróć statystyki wiadomości członka"""
        # TODO: Zwróć dict z:
        # - "received_count": liczba otrzymanych wiadomości
        # - "sent_count": liczba wysłanych wiadomości
        # - "role": rola członka
        # - "name": imię członka
        pass


# %% TODO: Implement Concrete Team Members

class Developer:
    """Członek zespołu - Developer"""

    def __init__(self, name: str, mediator: TeamMediator):
        """Inicjalizuj developer"""
        # TODO: super().__init__(name, mediator, TeamRole.DEVELOPER)
        pass

    def process_message(self, message: Message) -> None:
        """Przetworz wiadomość jako developer"""
        # TODO:
        # - TASK_ASSIGNMENT: zaakceptuj zadanie
        # - REVIEW_REQUEST: sprawdź czy to request do code review
        # - QUESTION: odpowiedz jeśli dotyczy technicznych zagadnień
        # - ANNOUNCEMENT: zanotuj informację
        pass

    def complete_task(self, task_description: str) -> None:
        """Zgłoś ukończenie zadania"""
        # TODO: Wyślij STATUS_UPDATE z informacją o ukończeniu
        pass

    def request_code_review(self, code_description: str) -> None:
        """Poproś o code review"""
        # TODO: Wyślij REVIEW_REQUEST do innych developers
        pass


class Designer:
    """Członek zespołu - Designer"""

    def __init__(self, name: str, mediator: TeamMediator):
        """Inicjalizuj designer"""
        # TODO: super().__init__(name, mediator, TeamRole.DESIGNER)
        pass

    def process_message(self, message: Message) -> None:
        """Przetworz wiadomość jako designer"""
        # TODO:
        # - TASK_ASSIGNMENT: zaakceptuj zadania projektowe
        # - QUESTION: odpowiedz na pytania o UI/UX
        # - STATUS_UPDATE: zanotuj postępy w development
        pass

    def share_mockups(self, design_description: str) -> None:
        """Udostępnij mockupy zespołowi"""
        # TODO: Wyślij ANNOUNCEMENT o nowych mockupach
        pass


class ProjectManager:
    """Członek zespołu - Project Manager"""

    def __init__(self, name: str, mediator: TeamMediator):
        """Inicjalizuj project manager"""
        # TODO: super().__init__(name, mediator, TeamRole.PROJECT_MANAGER)
        pass

    def process_message(self, message: Message) -> None:
        """Przetworz wiadomość jako PM"""
        # TODO:
        # - STATUS_UPDATE: śledź postępy projektu
        # - QUESTION: odpowiedz na pytania o wymagania
        # - REVIEW_REQUEST: zanotuj potrzeby review
        pass

    def assign_task(self, task_description: str, target_role: TeamRole) -> None:
        """Przypisz zadanie do określonej roli"""
        # TODO: Wyślij TASK_ASSIGNMENT do target_role
        pass

    def make_announcement(self, announcement: str) -> None:
        """Ogłoś informację całemu zespołowi"""
        # TODO: Wyślij ANNOUNCEMENT do wszystkich
        pass


class Tester:
    """Członek zespołu - Tester"""

    def __init__(self, name: str, mediator: TeamMediator):
        """Inicjalizuj tester"""
        # TODO: super().__init__(name, mediator, TeamRole.TESTER)
        pass

    def process_message(self, message: Message) -> None:
        """Przetworz wiadomość jako tester"""
        # TODO:
        # - STATUS_UPDATE: sprawdź czy feature gotowe do testów
        # - TASK_ASSIGNMENT: zaakceptuj zadania testowe
        # - QUESTION: odpowiedz na pytania o jakość/testy
        pass

    def report_bug(self, bug_description: str) -> None:
        """Zgłoś błąd do developers"""
        # TODO: Wyślij QUESTION z opisem błędu do DEVELOPER
        pass

    def approve_feature(self, feature_description: str) -> None:
        """Zatwierdź feature po testach"""
        # TODO: Wyślij STATUS_UPDATE o zatwierdzeniu feature
        pass


# %% Example Usage (Optional)

def demonstrate_team_collaboration():
    """Demonstracja współpracy zespołu przez mediator"""
    # TODO (Opcjonalne):
    # 1. Stwórz mediator i członków zespołu
    # 2. Symuluj typowy workflow (assignment -> development -> testing -> approval)
    # 3. Pokaż różne typy komunikacji
    # 4. Przetestuj filtrowanie wiadomości
    # 5. Zwróć statystyki komunikacji
    pass
