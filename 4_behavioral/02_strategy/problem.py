"""
❌ PROBLEM: Algorytmy przetwarzania wbudowane w klasę z if/elif

Rozwiązanie bez wzorca Strategy:
- Wszystkie algorytmy przetwarzania w jednej metodzie z if/elif
- Dodanie nowego algorytmu wymaga modyfikacji metody execute_task()
- Niemożliwa zmiana algorytmu w runtime
"""

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


class TaskManager:
    """
    ❌ PROBLEM: Wszystkie algorytmy w jednej klasie z if/elif

    Konsekwencje:
    1. Dodanie nowego priorytetu wymaga modyfikacji execute_task()
    2. Niemożliwa zmiana algorytmu w runtime
    3. Naruszenie Open/Closed Principle
    4. Trudne testowanie każdego algorytmu osobno
    """

    def execute_task(self, task: WorkflowTask) -> Dict[str, Any]:
        """
        ❌ PROBLEM: Wielki if/elif dla każdego priorytetu
        """
        start_time = time.time()

        # ❌ PROBLEM: Hardcoded if/elif dla każdego typu
        if task.priority == TaskPriority.URGENT:
            # Logika dla urgent
            validation_passed = (
                task.priority == TaskPriority.URGENT
                and task.description
            )
            # Natychmiastowe przetwarzanie
            task.mark_completed()
            result = {
                "status": "completed",
                "processing_time": time.time() - start_time,
                "strategy_used": "urgent",
                "validation_passed": validation_passed
            }

        elif task.priority == TaskPriority.HIGH or task.priority == TaskPriority.MEDIUM:
            # Logika dla standard
            validation_passed = len(task.title) >= 3
            time.sleep(1)  # Symulacja przetwarzania
            task.mark_completed()
            result = {
                "status": "completed",
                "processing_time": time.time() - start_time,
                "strategy_used": "standard",
                "validation_passed": validation_passed
            }

        elif task.priority == TaskPriority.LOW:
            # Logika dla background
            validation_passed = task.priority != TaskPriority.URGENT
            time.sleep(0.1)  # Symulacja wolnego przetwarzania
            task.mark_completed()
            result = {
                "status": "completed",
                "processing_time": time.time() - start_time,
                "strategy_used": "background",
                "validation_passed": validation_passed
            }

        else:
            # ❌ PROBLEM: Co z nowym priorytetem CRITICAL?
            raise ValueError(f"Unknown priority: {task.priority}")

        return result


# ❌ Przykład użycia
if __name__ == "__main__":
    manager = TaskManager()

    # Działa, ale brak elastyczności
    urgent_task = WorkflowTask("Security breach", TaskPriority.URGENT, "Critical fix")
    result = manager.execute_task(urgent_task)
    print(f"Urgent: {result['strategy_used']}")

    standard_task = WorkflowTask("Fix bug", TaskPriority.HIGH, "Bug in login")
    result = manager.execute_task(standard_task)
    print(f"Standard: {result['strategy_used']}")

    # ❌ Chcę przetworzyć HIGH task jako urgent (natychmiast)?
    # Nie mogę - algorytm jest hardcoded w if/elif
    #
    # ❌ Chcę dodać CRITICAL priority?
    # Muszę EDYTOWAĆ metodę execute_task() (dodać elif)
    #
    # ❌ Chcę testować algorytm urgent w izolacji?
    # Muszę testować całą klasę TaskManager
    #
    # Naruszenie Open/Closed Principle!


"""
Jakie problemy rozwiązuje Strategy?

1. ❌ Naruszenie Open/Closed Principle
   - Dodanie nowego algorytmu wymaga EDYCJI execute_task()
   - Nie można rozszerzyć bez modyfikacji

2. ❌ Brak elastyczności w runtime
   - Algorytm przetwarzania wybrany raz na podstawie priority
   - Nie można zmienić algorytmu dla tego samego taska
   - Niemożliwa zmiana strategii dynamicznie

3. ❌ Trudne testowanie
   - Testowanie każdego algorytmu wymaga testowania całej klasy
   - Nie można testować algorytmów w izolacji
   - Mocki wymagają patchowania całej metody

4. ❌ Naruszenie Single Responsibility Principle
   - TaskManager odpowiada za zarządzanie zadaniami
   - TaskManager zawiera 3 różne algorytmy przetwarzania
   - Zmiana w algorytmie urgent może zepsuć standard

5. ❌ Duplikacja kodu
   - Każdy if/elif ma podobną strukturę (start_time, validation, result dict)
   - Wspólna logika powielona w każdej gałęzi

Jak Strategy to rozwiązuje?
1. Każdy algorytm w osobnej klasie (UrgentTaskProcessor, StandardTaskProcessor, BackgroundTaskProcessor)
2. TaskManager deleguje do strategy.process_task(task)
3. Zmiana strategii w runtime: manager.set_strategy(new_strategy)
4. Nowa strategia = nowa klasa, zero zmian w TaskManager
"""
