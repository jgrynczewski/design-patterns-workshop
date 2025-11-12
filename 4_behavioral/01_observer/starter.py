# %% About
# - Name: Observer - Workflow Notifications
# - Difficulty: easy
# - Lines: 18
# - Minutes: 15
# - Focus: Observer pattern - one-to-many dependency

# %% Description
"""
Implementuj wzorzec Observer do systemu powiadomień o zmianach
statusu zadań w workflow.

Zadanie: Stwórz system gdzie wiele kanałów reaguje na zmiany statusu
"""

# %% Hints
# - WorkflowTask (subject) przechowuje listę observers
# - Przy set_status() powiadom wszystkich observers
# - Każdy observer ma swoją logikę notify()
# - Użyj enum dla statusów workflow

# %% Doctests
"""
>>> # Test podstawowego workflow
>>> task = WorkflowTask("Fix login bug", TaskStatus.ASSIGNED)
>>> task.task_id
'Fix login bug'
>>> task.status
<TaskStatus.ASSIGNED: 'assigned'>

>>> # Test dodawania observers
>>> email_notifier = EmailNotifier("dev@company.com")
>>> slack_notifier = SlackNotifier("#dev-team")
>>> task.add_observer(email_notifier)
>>> task.add_observer(slack_notifier)
>>> len(task.observers)
2

>>> # Test powiadomień przy zmianie statusu
>>> task.set_status(TaskStatus.IN_PROGRESS)
>>> task.status
<TaskStatus.IN_PROGRESS: 'in_progress'>
>>> len(email_notifier.notifications) > 0
True
>>> len(slack_notifier.messages) > 0
True
"""

# %% Imports
from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from datetime import datetime


# %% Task Status Enum (już gotowe)

class TaskStatus(Enum):
    """Statusy zadań w workflow"""
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    COMPLETED = "completed"


# %% TODO: Implement Observer Interface

class Observer(ABC):
    """Interface dla wszystkich observers"""

    @abstractmethod
    def notify(self, task: 'WorkflowTask', old_status: TaskStatus, new_status: TaskStatus) -> None:
        """Otrzymaj powiadomienie o zmianie statusu zadania"""
        pass


# %% TODO: Implement Concrete Observers

class EmailNotifier:
    """Observer wysyłający powiadomienia email"""

    def __init__(self, email_address: str):
        """Inicjalizuj notifier z adresem email"""
        # TODO:
        # self.email_address = ...
        # self.notifications = []  # Lista wysłanych powiadomień (do testów)
        pass

    def notify(self, task: 'WorkflowTask', old_status: TaskStatus, new_status: TaskStatus) -> None:
        """Wyślij powiadomienie email"""
        # TODO:
        # 1. Stwórz wiadomość email
        # 2. Dodaj do self.notifications (symulacja wysłania)
        # Format: f"Task '{task.task_id}' changed from {old_status.value} to {new_status.value}"
        pass


class SlackNotifier:
    """Observer wysyłający powiadomienia do Slack"""

    def __init__(self, channel: str):
        """Inicjalizuj notifier z kanałem Slack"""
        # TODO:
        # self.channel = ...
        # self.messages = []  # Lista wysłanych wiadomości (do testów)
        pass

    def notify(self, task: 'WorkflowTask', old_status: TaskStatus, new_status: TaskStatus) -> None:
        """Wyślij wiadomość do Slack"""
        # TODO:
        # 1. Stwórz wiadomość Slack
        # 2. Dodaj do self.messages
        # Format: f"📋 Task Update: '{task.task_id}' is now {new_status.value}"
        pass


class SMSNotifier:
    """Observer wysyłający SMS do managerów"""

    def __init__(self, phone_number: str):
        """Inicjalizuj notifier z numerem telefonu"""
        # TODO:
        # self.phone_number = ...
        # self.sms_sent = []  # Lista wysłanych SMS (do testów)
        pass

    def notify(self, task: 'WorkflowTask', old_status: TaskStatus, new_status: TaskStatus) -> None:
        """Wyślij SMS"""
        # TODO:
        # 1. Stwórz krótką wiadomość SMS
        # 2. Dodaj do self.sms_sent
        # Format: f"Task {task.task_id}: {old_status.value} → {new_status.value}"
        pass


class DashboardNotifier:
    """Observer aktualizujący dashboard"""

    def __init__(self):
        """Inicjalizuj dashboard notifier"""
        # TODO:
        # self.dashboard_updates = []  # Lista aktualizacji (do testów)
        pass

    def notify(self, task: 'WorkflowTask', old_status: TaskStatus, new_status: TaskStatus) -> None:
        """Aktualizuj dashboard"""
        # TODO:
        # 1. Stwórz update dashboard
        # 2. Dodaj do self.dashboard_updates
        # Format: {"task_id": task.task_id, "status": new_status.value, "timestamp": datetime.now()}
        pass


# %% TODO: Implement WorkflowTask (Subject)

class WorkflowTask:
    """Zadanie workflow które może mieć observers"""

    def __init__(self, task_id: str, initial_status: TaskStatus):
        """Inicjalizuj zadanie z początkowym statusem"""
        # TODO:
        # self.task_id = ...
        # self.status = ...
        # self.observers = []  # Lista observers
        pass

    def add_observer(self, observer: Observer) -> None:
        """Dodaj observer do listy"""
        # TODO: Dodaj observer do self.observers
        pass

    def remove_observer(self, observer: Observer) -> None:
        """Usuń observer z listy"""
        # TODO: Usuń observer z self.observers (jeśli istnieje)
        pass

    def notify_observers(self, old_status: TaskStatus, new_status: TaskStatus) -> None:
        """Powiadom wszystkich observers o zmianie"""
        # TODO: Dla każdego observer w self.observers wywołaj notify()
        pass

    def set_status(self, new_status: TaskStatus) -> None:
        """Zmień status zadania i powiadom observers"""
        # TODO:
        # 1. Zapisz stary status
        # 2. Ustaw nowy status
        # 3. Powiadom wszystkich observers
        pass

    def get_observer_count(self) -> int:
        """Zwróć liczbę observers (do testów)"""
        # TODO: Zwróć len(self.observers)
        pass


# %% Example Usage (Optional)

def create_sample_workflow():
    """Stwórz przykładowy workflow z powiadomieniami"""
    # TODO (Opcjonalne):
    # 1. Stwórz zadanie
    # 2. Dodaj różnych observers
    # 3. Symuluj zmiany statusu
    # 4. Zwróć zadanie
    pass
