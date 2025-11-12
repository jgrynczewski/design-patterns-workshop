"""
Strategy Pattern - Task Processing Strategies - SOLUTION

>>> # Test concrete strategies
>>> task = WorkflowTask("Fix bug", TaskPriority.URGENT, "Critical fix")
>>> processor = UrgentTaskProcessor()
>>> result = processor.process_task(task)
>>> result["strategy_used"]
'urgent'

>>> # Test TaskManager with strategy
>>> manager = TaskManager()
>>> manager.set_strategy(StandardTaskProcessor())
>>> task = WorkflowTask("Update", TaskPriority.MEDIUM, "Update docs")
>>> result = manager.execute_task(task)
>>> result["status"]
'completed'
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


class TaskProcessor(ABC):
    """STRATEGY INTERFACE - definiuje wspólny interfejs dla algorytmów"""

    @abstractmethod
    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie i zwróć wynik"""
        pass


class UrgentTaskProcessor(TaskProcessor):
    """CONCRETE STRATEGY - strategia dla zadań pilnych"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie pilne natychmiast"""
        start_time = time.time()

        validation_passed = self._validate_urgent_task(task)

        # Natychmiastowe przetwarzanie (bez delay)
        task.mark_completed()

        processing_time = time.time() - start_time

        return {
            "status": "completed",
            "processing_time": processing_time,
            "strategy_used": "urgent",
            "validation_passed": validation_passed
        }

    def _validate_urgent_task(self, task: WorkflowTask) -> bool:
        """Walidacja zadania pilnego"""
        return task.priority == TaskPriority.URGENT and task.description != ""


class StandardTaskProcessor(TaskProcessor):
    """CONCRETE STRATEGY - strategia dla zadań standardowych"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie standardowe"""
        start_time = time.time()

        validation_passed = self._validate_standard_task(task)

        # Normalne przetwarzanie z delay
        time.sleep(1)
        task.mark_completed()

        processing_time = time.time() - start_time

        return {
            "status": "completed",
            "processing_time": processing_time,
            "strategy_used": "standard",
            "validation_passed": validation_passed
        }

    def _validate_standard_task(self, task: WorkflowTask) -> bool:
        """Walidacja zadania standardowego"""
        return len(task.title) >= 3


class BackgroundTaskProcessor(TaskProcessor):
    """CONCRETE STRATEGY - strategia dla zadań w tle"""

    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie w tle"""
        start_time = time.time()

        validation_passed = self._validate_background_task(task)

        # Wolne przetwarzanie w tle (skrócone dla testów)
        time.sleep(0.1)  # W produkcji byłoby 3s
        task.mark_completed()

        processing_time = time.time() - start_time

        return {
            "status": "completed",
            "processing_time": processing_time,
            "strategy_used": "background",
            "validation_passed": validation_passed
        }

    def _validate_background_task(self, task: WorkflowTask) -> bool:
        """Walidacja zadania do przetwarzania w tle"""
        return task.priority != TaskPriority.URGENT


class TaskManager:
    """CONTEXT - używa strategii do przetwarzania zadań"""

    def __init__(self, strategy: TaskProcessor = None):
        """Inicjalizuj manager z opcjonalną strategią"""
        self.strategy = strategy
        self.processed_tasks = []

    def set_strategy(self, strategy: TaskProcessor) -> None:
        """Ustaw nową strategię przetwarzania"""
        self.strategy = strategy

    def execute_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Wykonaj zadanie używając aktualnej strategii"""
        if self.strategy is None:
            raise ValueError("Strategy not set. Use set_strategy() first.")

        result = self.strategy.process_task(task)
        self.processed_tasks.append(task)

        return result

    def auto_select_strategy(self, task: WorkflowTask) -> None:
        """Automatycznie wybierz strategię na podstawie priorytetu"""
        if task.priority == TaskPriority.URGENT:
            self.strategy = UrgentTaskProcessor()
        elif task.priority in [TaskPriority.HIGH, TaskPriority.MEDIUM]:
            self.strategy = StandardTaskProcessor()
        else:  # TaskPriority.LOW
            self.strategy = BackgroundTaskProcessor()

    def execute_with_auto_strategy(self, task: WorkflowTask) -> Dict[str, Any]:
        """Wykonaj zadanie z automatycznym wyborem strategii"""
        self.auto_select_strategy(task)
        return self.execute_task(task)

    def get_processing_stats(self) -> Dict[str, Any]:
        """Zwróć statystyki przetwarzania"""
        return {
            "total_processed": len(self.processed_tasks),
            "current_strategy": self.strategy
        }


def demonstrate_strategies():
    """Demonstracja różnych strategii przetwarzania"""
    print("=== Strategy Pattern: Task Processing ===\n")

    manager = TaskManager()

    # Zadanie pilne
    urgent_task = WorkflowTask("Security breach", TaskPriority.URGENT, "Critical security issue")
    manager.set_strategy(UrgentTaskProcessor())
    result = manager.execute_task(urgent_task)
    print(f"Urgent task: {result['strategy_used']}, time: {result['processing_time']:.3f}s")

    # Zadanie standardowe
    standard_task = WorkflowTask("Fix bug", TaskPriority.HIGH, "Bug in UI")
    manager.set_strategy(StandardTaskProcessor())
    result = manager.execute_task(standard_task)
    print(f"Standard task: {result['strategy_used']}, time: {result['processing_time']:.3f}s")

    # Zadanie w tle
    background_task = WorkflowTask("Update docs", TaskPriority.LOW, "Documentation update")
    manager.set_strategy(BackgroundTaskProcessor())
    result = manager.execute_task(background_task)
    print(f"Background task: {result['strategy_used']}, time: {result['processing_time']:.3f}s")

    print("\nStrategy: Różne algorytmy dla różnych priorytetów")


if __name__ == "__main__":
    demonstrate_strategies()
