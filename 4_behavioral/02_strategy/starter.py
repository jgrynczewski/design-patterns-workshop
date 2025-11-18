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


# Helper Classes - GOTOWE

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


# Strategy Interface - GOTOWE
# WZORZEC: Strategy (interfejs strategii)

class TaskProcessor(ABC):
    """Interface dla strategii przetwarzania zadań"""

    @abstractmethod
    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie i zwróć wynik"""
        pass


# Concrete Strategies - ROZWIĄZANIE
# WZORZEC: Concrete Strategy (konkretna strategia)

class UrgentTaskProcessor(TaskProcessor):
    """Strategia dla zadań pilnych - natychmiastowe przetwarzanie"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        start_time = time.time()

        # Walidacja: sprawdź czy zadanie jest pilne i ma opis
        validation_passed = bool(
            task.priority == TaskPriority.URGENT
            and task.description
        )

        # Natychmiastowe przetwarzanie (bez delay)
        task.mark_completed()

        return {
            "status": "completed",
            "processing_time": time.time() - start_time,
            "strategy_used": "urgent",
            "validation_passed": validation_passed
        }


class StandardTaskProcessor(TaskProcessor):
    """Strategia dla zadań standardowych - normalne przetwarzanie"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        start_time = time.time()

        # Walidacja: sprawdź czy tytuł ma przynajmniej 3 znaki
        validation_passed = len(task.title) >= 3

        # Symulacja normalnego przetwarzania
        time.sleep(1)
        task.mark_completed()

        return {
            "status": "completed",
            "processing_time": time.time() - start_time,
            "strategy_used": "standard",
            "validation_passed": validation_passed
        }


class BackgroundTaskProcessor(TaskProcessor):
    """Strategia dla zadań w tle - wolne przetwarzanie"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        start_time = time.time()

        # Walidacja: zadania pilne nie mogą być w tle
        validation_passed = task.priority != TaskPriority.URGENT

        # Symulacja wolnego przetwarzania w tle
        time.sleep(0.1)
        task.mark_completed()

        return {
            "status": "completed",
            "processing_time": time.time() - start_time,
            "strategy_used": "background",
            "validation_passed": validation_passed
        }


# Context - ROZWIĄZANIE
# WZORZEC: Context (kontekst używający strategii)

class TaskManager:
    """
    Manager zadań - deleguje przetwarzanie do strategii

    Context we wzorcu Strategy - nie wie jak przetwarzać zadania,
    deleguje to do aktualnie ustawionej strategii.
    """

    def __init__(self, strategy: TaskProcessor = None):
        """
        Inicjalizacja managera z opcjonalną strategią

        Args:
            strategy: Początkowa strategia przetwarzania
        """
        self.strategy = strategy

    def set_strategy(self, strategy: TaskProcessor) -> None:
        """
        Zmienia strategię przetwarzania w runtime

        Args:
            strategy: Nowa strategia przetwarzania
        """
        self.strategy = strategy

    def execute_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """
        Wykonuje zadanie używając aktualnej strategii

        Args:
            task: Zadanie do wykonania

        Returns:
            Wynik przetwarzania z strategii

        Raises:
            ValueError: Gdy strategia nie jest ustawiona
        """
        if self.strategy is None:
            raise ValueError("No strategy set")

        # Delegacja do strategii
        return self.strategy.process_task(task)


# Przykład użycia
if __name__ == "__main__":
    # Tworzenie managera z początkową strategią
    manager = TaskManager(UrgentTaskProcessor())

    # Urgent processing
    urgent_task = WorkflowTask("Security breach", TaskPriority.URGENT, "Critical fix needed")
    result = manager.execute_task(urgent_task)
    print(f"Urgent: {result['strategy_used']}, time: {result['processing_time']:.3f}s")

    # Zmiana strategii w runtime
    manager.set_strategy(StandardTaskProcessor())
    standard_task = WorkflowTask("Fix bug", TaskPriority.HIGH, "Bug in user interface")
    result = manager.execute_task(standard_task)
    print(f"Standard: {result['strategy_used']}, time: {result['processing_time']:.3f}s")

    # Kolejna zmiana strategii
    manager.set_strategy(BackgroundTaskProcessor())
    low_task = WorkflowTask("Update docs", TaskPriority.LOW, "Documentation update")
    result = manager.execute_task(low_task)
    print(f"Background: {result['strategy_used']}, time: {result['processing_time']:.3f}s")
