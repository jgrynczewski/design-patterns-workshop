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


# %% Helper Classes - GOTOWE

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


# %% Strategy Interface - GOTOWE
# WZORZEC: Strategy (interfejs strategii)

class TaskProcessor(ABC):
    """Interface dla strategii przetwarzania zadań"""

    @abstractmethod
    def process_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """Przetworz zadanie i zwróć wynik"""
        pass


# %% Concrete Strategies - DO IMPLEMENTACJI
# WZORZEC: Concrete Strategy (konkretna strategia)

# TODO: Zaimplementuj klasę UrgentTaskProcessor
# Dziedziczy po TaskProcessor
# Metoda process_task(task: WorkflowTask) -> Dict[str, Any]:
#   - Zapisz start time (time.time())
#   - Walidacja: sprawdź czy task.priority == URGENT i description nie jest puste
#   - Natychmiastowe przetwarzanie (bez delay, bez time.sleep)
#   - Oznacz zadanie jako completed (task.mark_completed())
#   - Zwróć dict z kluczami: "status" (str), "processing_time" (float), "strategy_used" (str = "urgent"), "validation_passed" (bool)

class UrgentTaskProcessor:
    pass


# TODO: Zaimplementuj klasę StandardTaskProcessor
# Dziedziczy po TaskProcessor
# Metoda process_task(task: WorkflowTask) -> Dict[str, Any]:
#   - Zapisz start time (time.time())
#   - Walidacja: sprawdź czy title ma przynajmniej 3 znaki
#   - Symuluj przetwarzanie: time.sleep(1)
#   - Oznacz zadanie jako completed (task.mark_completed())
#   - Zwróć dict z kluczami: "status" (str), "processing_time" (float), "strategy_used" (str = "standard"), "validation_passed" (bool)

class StandardTaskProcessor:
    pass


# TODO: Zaimplementuj klasę BackgroundTaskProcessor
# Dziedziczy po TaskProcessor
# Metoda process_task(task: WorkflowTask) -> Dict[str, Any]:
#   - Zapisz start time (time.time())
#   - Walidacja: sprawdź czy priority != URGENT (zadania pilne nie mogą być w tle)
#   - Symuluj wolne przetwarzanie: time.sleep(0.1)
#   - Oznacz zadanie jako completed (task.mark_completed())
#   - Zwróć dict z kluczami: "status" (str), "processing_time" (float), "strategy_used" (str = "background"), "validation_passed" (bool)

class BackgroundTaskProcessor:
    pass


# %% Context - DO IMPLEMENTACJI
# WZORZEC: Context (kontekst używający strategii)

# TODO: Zaimplementuj klasę TaskManager
# Konstruktor przyjmuje strategy: TaskProcessor = None (opcjonalna strategia)
#   - Przechowuje strategię jako self.strategy
#
# Metoda set_strategy(strategy: TaskProcessor) -> None:
#   - Ustawia nową strategię przetwarzania (self.strategy = strategy)
#
# Metoda execute_task(task: WorkflowTask) -> Dict[str, Any]:
#   - Sprawdza czy strategia jest ustawiona (jeśli nie - raise ValueError("No strategy set"))
#   - Deleguje do self.strategy.process_task(task)
#   - Zwraca wynik z process_task()

class TaskManager:
    pass
