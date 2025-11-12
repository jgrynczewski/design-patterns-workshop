"""
Strategy Pattern - Task Processing Strategies

>>> # Test tworzenia zadania
>>> task = WorkflowTask("Fix database bug", TaskPriority.HIGH, "Bug in user login")
>>> task.title
'Fix database bug'
>>> task.priority
<TaskPriority.HIGH: 'high'>

>>> # Test strategii urgent
>>> urgent_processor = UrgentTaskProcessor()
>>> manager = TaskManager(urgent_processor)
>>> urgent_task = WorkflowTask("Security breach", TaskPriority.URGENT, "Critical fix needed")
>>> result = manager.execute_task(urgent_task)
>>> result["status"]
'completed'
>>> result["processing_time"] < 1.0
True

>>> # Test zmiany strategii w runtime
>>> background_processor = BackgroundTaskProcessor()
>>> manager.set_strategy(background_processor)
>>> low_task = WorkflowTask("Update docs", TaskPriority.LOW, "Documentation update")
>>> result = manager.execute_task(low_task)
>>> result["strategy_used"]
'background'
"""

from abc import ABC, abstractmethod
from enum import Enum
import time
from typing import Dict, Any
from datetime import datetime


class TaskPriority(Enum):
    """Priorytety zadań w workflow"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class WorkflowTask:
    """Zadanie w workflow system"""

    def __init__(self, title: str, priority: TaskPriority, description: str):
        self.title = title
        self.priority = priority
        self.description = description
        self.created_at = datetime.now()
        self.completed_at = None

    def mark_completed(self):
        """Oznacz zadanie jako ukończone"""
        self.completed_at = datetime.now()


# TODO: Zaimplementuj TaskProcessor Strategy Interface
class TaskProcessor(ABC):
    """Interface dla strategii przetwarzania zadań"""

    @abstractmethod
    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie i zwróć wynik"""
        pass


# TODO: Zaimplementuj Concrete Strategies
class UrgentTaskProcessor(TaskProcessor):
    """Strategia dla zadań pilnych - natychmiastowe przetwarzanie"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie pilne natychmiast"""
        # TODO:
        # 1. Zapisz start time
        # 2. Validation: sprawdź czy task.priority == URGENT
        # 3. Natychmiastowe przetwarzanie (bez delay)
        # 4. Oznacz zadanie jako completed
        # 5. Zwróć result dict z: status, processing_time, strategy_used="urgent", validation_passed
        pass

    def _validate_urgent_task(self, task: WorkflowTask) -> bool:
        """Walidacja zadania pilnego"""
        # TODO: Sprawdź czy priority == URGENT i description nie jest puste
        pass


class StandardTaskProcessor(TaskProcessor):
    """Strategia dla zadań standardowych - normalne przetwarzanie"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie standardowe"""
        # TODO:
        # 1. Zapisz start time
        # 2. Validation: sprawdź czy task prawidłowe
        # 3. Symuluj przetwarzanie: time.sleep(1)
        # 4. Oznacz zadanie jako completed
        # 5. Zwróć result dict z: status, processing_time, strategy_used="standard", validation_passed
        pass

    def _validate_standard_task(self, task: WorkflowTask) -> bool:
        """Walidacja zadania standardowego"""
        # TODO: Sprawdź czy title ma przynajmniej 3 znaki
        pass


class BackgroundTaskProcessor(TaskProcessor):
    """Strategia dla zadań w tle - wolne przetwarzanie"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie w tle"""
        # TODO:
        # 1. Zapisz start time
        # 2. Validation: sprawdź czy można przetworzyć w tle
        # 3. Symuluj wolne przetwarzanie: time.sleep(0.1)  # Skrócone dla testów zamiast 3s
        # 4. Oznacz zadanie jako completed
        # 5. Zwróć result dict z: status, processing_time, strategy_used="background", validation_passed
        pass

    def _validate_background_task(self, task: WorkflowTask) -> bool:
        """Walidacja zadania do przetwarzania w tle"""
        # TODO: Sprawdź czy priority != URGENT (zadania pilne nie mogą być w tle)
        pass


# TODO: Zaimplementuj TaskManager (Context)
class TaskManager:
    """Manager zadań używający różnych strategii przetwarzania"""

    def __init__(self, strategy: TaskProcessor = None):
        """Inicjalizuj manager z opcjonalną strategią"""
        # TODO:
        # self.strategy = strategy (może być None)
        # self.processed_tasks = []  # Historia przetworzonych zadań
        pass

    def set_strategy(self, strategy: TaskProcessor) -> None:
        """Ustaw nową strategię przetwarzania"""
        # TODO: Ustaw self.strategy
        pass

    def execute_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Wykonaj zadanie używając aktualnej strategii"""
        # TODO:
        # 1. Sprawdź czy strategia jest ustawiona (jeśli nie - raise ValueError)
        # 2. Wywołaj strategy.process_task(task)
        # 3. Dodaj task do self.processed_tasks
        # 4. Zwróć wynik
        pass

    def auto_select_strategy(self, task: WorkflowTask) -> None:
        """Automatycznie wybierz strategię na podstawie priorytetu"""
        # TODO:
        # - URGENT -> UrgentTaskProcessor
        # - HIGH/MEDIUM -> StandardTaskProcessor
        # - LOW -> BackgroundTaskProcessor
        pass

    def execute_with_auto_strategy(self, task: WorkflowTask) -> Dict[str, Any]:
        """Wykonaj zadanie z automatycznym wyborem strategii"""
        # TODO:
        # 1. Wywołaj auto_select_strategy(task)
        # 2. Wywołaj execute_task(task)
        # 3. Zwróć wynik
        pass

    def get_processing_stats(self) -> Dict[str, Any]:
        """Zwróć statystyki przetwarzania"""
        # TODO: Zwróć dict z:
        # - "total_processed": liczba przetworzonych zadań
        # - "current_strategy": nazwa aktualnej strategii (lub None)
        pass


def demonstrate_strategies():
    """Demonstracja różnych strategii przetwarzania"""
    # TODO (Opcjonalne):
    # 1. Stwórz zadania o różnych priorytetach
    # 2. Przetestuj każdą strategię
    # 3. Pokaż różnice w czasach przetwarzania
    # 4. Zwróć wyniki
    pass


# Strategy Pattern:
# Definiuje rodzinę algorytmów, enkapsuluje je i robi wymiennymi
# Klient może wybierać algorytm w runtime
# Każda strategia ma ten sam interfejs, inną implementację
