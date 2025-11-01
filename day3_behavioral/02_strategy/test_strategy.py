"""
Testy dla Strategy Pattern - Task Processing Strategies
"""

import pytest
import time
from starter import (
    TaskPriority, WorkflowTask, TaskProcessor,
    UrgentTaskProcessor, StandardTaskProcessor, BackgroundTaskProcessor,
    TaskManager, demonstrate_strategies
)


class TestTaskPriority:
    """Testy enum TaskPriority"""

    def test_task_priority_values(self):
        """Test wartości enum TaskPriority"""
        assert TaskPriority.LOW.value == "low"
        assert TaskPriority.MEDIUM.value == "medium"
        assert TaskPriority.HIGH.value == "high"
        assert TaskPriority.URGENT.value == "urgent"


class TestWorkflowTask:
    """Testy klasy WorkflowTask"""

    def test_task_creation(self):
        """Test tworzenia zadania"""
        task = WorkflowTask("Test task", TaskPriority.MEDIUM, "Test description")

        assert task.title == "Test task"
        assert task.priority == TaskPriority.MEDIUM
        assert task.description == "Test description"
        assert task.completed_at is None

    def test_task_mark_completed(self):
        """Test oznaczania zadania jako ukończone"""
        task = WorkflowTask("Complete me", TaskPriority.HIGH, "Test task")

        assert task.completed_at is None
        task.mark_completed()
        assert task.completed_at is not None


class TestUrgentTaskProcessor:
    """Testy strategii pilnych zadań"""

    def test_urgent_processor_implements_interface(self):
        """Test że UrgentTaskProcessor implementuje interface"""
        processor = UrgentTaskProcessor()
        assert isinstance(processor, TaskProcessor)

    def test_urgent_task_processing(self):
        """Test przetwarzania zadania pilnego"""
        processor = UrgentTaskProcessor()
        task = WorkflowTask("Security breach", TaskPriority.URGENT, "Critical security issue")

        start_time = time.time()
        result = processor.process_task(task)
        end_time = time.time()

        assert result["status"] == "completed"
        assert result["strategy_used"] == "urgent"
        assert result["validation_passed"] is True
        assert result["processing_time"] < 0.1  # Powinno być bardzo szybkie
        assert (end_time - start_time) < 0.1  # Bez delay
        assert task.completed_at is not None

    def test_urgent_validation(self):
        """Test walidacji zadań pilnych"""
        processor = UrgentTaskProcessor()

        # Prawidłowe zadanie pilne
        valid_task = WorkflowTask("Emergency", TaskPriority.URGENT, "Critical issue")
        result = processor.process_task(valid_task)
        assert result["validation_passed"] is True

        # Nieprawidłowe zadanie (nie pilne)
        invalid_task = WorkflowTask("Normal task", TaskPriority.MEDIUM, "Regular work")
        result = processor.process_task(invalid_task)
        assert result["validation_passed"] is False


class TestStandardTaskProcessor:
    """Testy strategii standardowych zadań"""

    def test_standard_processor_implements_interface(self):
        """Test że StandardTaskProcessor implementuje interface"""
        processor = StandardTaskProcessor()
        assert isinstance(processor, TaskProcessor)

    def test_standard_task_processing(self):
        """Test przetwarzania zadania standardowego"""
        processor = StandardTaskProcessor()
        task = WorkflowTask("Fix bug", TaskPriority.HIGH, "Bug in user interface")

        start_time = time.time()
        result = processor.process_task(task)
        end_time = time.time()

        assert result["status"] == "completed"
        assert result["strategy_used"] == "standard"
        assert result["validation_passed"] is True
        assert (end_time - start_time) >= 0.9  # Powinno mieć ~1s delay
        assert task.completed_at is not None

    def test_standard_validation(self):
        """Test walidacji zadań standardowych"""
        processor = StandardTaskProcessor()

        # Prawidłowe zadanie (tytuł >= 3 znaki)
        valid_task = WorkflowTask("Fix", TaskPriority.MEDIUM, "Fix something")
        result = processor.process_task(valid_task)
        assert result["validation_passed"] is True

        # Nieprawidłowe zadanie (tytuł < 3 znaki)
        invalid_task = WorkflowTask("AB", TaskPriority.MEDIUM, "Too short title")
        result = processor.process_task(invalid_task)
        assert result["validation_passed"] is False


class TestBackgroundTaskProcessor:
    """Testy strategii zadań w tle"""

    def test_background_processor_implements_interface(self):
        """Test że BackgroundTaskProcessor implementuje interface"""
        processor = BackgroundTaskProcessor()
        assert isinstance(processor, TaskProcessor)

    def test_background_task_processing(self):
        """Test przetwarzania zadania w tle"""
        processor = BackgroundTaskProcessor()
        task = WorkflowTask("Update documentation", TaskPriority.LOW, "Update user manual")

        start_time = time.time()
        result = processor.process_task(task)
        end_time = time.time()

        assert result["status"] == "completed"
        assert result["strategy_used"] == "background"
        assert result["validation_passed"] is True
        assert (end_time - start_time) >= 0.05  # Powinno mieć delay (skrócony w testach)
        assert task.completed_at is not None

    def test_background_validation(self):
        """Test walidacji zadań w tle"""
        processor = BackgroundTaskProcessor()

        # Prawidłowe zadanie (nie pilne)
        valid_task = WorkflowTask("Cleanup", TaskPriority.LOW, "Clean old files")
        result = processor.process_task(valid_task)
        assert result["validation_passed"] is True

        # Nieprawidłowe zadanie (pilne - nie może być w tle)
        invalid_task = WorkflowTask("Emergency", TaskPriority.URGENT, "Critical issue")
        result = processor.process_task(invalid_task)
        assert result["validation_passed"] is False


class TestTaskManager:
    """Testy TaskManager (Context)"""

    def test_task_manager_creation(self):
        """Test tworzenia TaskManager"""
        manager = TaskManager()

        assert manager.strategy is None
        assert len(manager.processed_tasks) == 0

    def test_task_manager_with_initial_strategy(self):
        """Test tworzenia TaskManager z początkową strategią"""
        strategy = UrgentTaskProcessor()
        manager = TaskManager(strategy)

        assert manager.strategy is strategy

    def test_set_strategy(self):
        """Test ustawiania strategii"""
        manager = TaskManager()
        strategy = StandardTaskProcessor()

        manager.set_strategy(strategy)
        assert manager.strategy is strategy

    def test_execute_task_with_strategy(self):
        """Test wykonywania zadania z ustawioną strategią"""
        manager = TaskManager()
        strategy = UrgentTaskProcessor()
        manager.set_strategy(strategy)

        task = WorkflowTask("Test execution", TaskPriority.URGENT, "Test task")
        result = manager.execute_task(task)

        assert result["status"] == "completed"
        assert result["strategy_used"] == "urgent"
        assert len(manager.processed_tasks) == 1
        assert manager.processed_tasks[0] is task

    def test_execute_task_without_strategy(self):
        """Test wykonywania zadania bez ustawionej strategii"""
        manager = TaskManager()
        task = WorkflowTask("No strategy", TaskPriority.MEDIUM, "Test")

        with pytest.raises(ValueError):
            manager.execute_task(task)

    def test_auto_select_strategy_urgent(self):
        """Test automatycznego wyboru strategii dla zadań pilnych"""
        manager = TaskManager()
        task = WorkflowTask("Emergency", TaskPriority.URGENT, "Critical issue")

        manager.auto_select_strategy(task)
        assert isinstance(manager.strategy, UrgentTaskProcessor)

    def test_auto_select_strategy_standard(self):
        """Test automatycznego wyboru strategii dla zadań standardowych"""
        manager = TaskManager()

        for priority in [TaskPriority.HIGH, TaskPriority.MEDIUM]:
            task = WorkflowTask("Standard task", priority, "Regular work")
            manager.auto_select_strategy(task)
            assert isinstance(manager.strategy, StandardTaskProcessor)

    def test_auto_select_strategy_background(self):
        """Test automatycznego wyboru strategii dla zadań w tle"""
        manager = TaskManager()
        task = WorkflowTask("Background task", TaskPriority.LOW, "Low priority work")

        manager.auto_select_strategy(task)
        assert isinstance(manager.strategy, BackgroundTaskProcessor)

    def test_execute_with_auto_strategy(self):
        """Test wykonywania z automatycznym wyborem strategii"""
        manager = TaskManager()

        # Test z zadaniem pilnym
        urgent_task = WorkflowTask("Emergency", TaskPriority.URGENT, "Critical")
        result = manager.execute_with_auto_strategy(urgent_task)
        assert result["strategy_used"] == "urgent"

        # Test z zadaniem w tle
        background_task = WorkflowTask("Cleanup", TaskPriority.LOW, "Background work")
        result = manager.execute_with_auto_strategy(background_task)
        assert result["strategy_used"] == "background"

    def test_processing_stats(self):
        """Test statystyk przetwarzania"""
        manager = TaskManager()
        strategy = StandardTaskProcessor()
        manager.set_strategy(strategy)

        # Początkowo brak przetworzonych zadań
        stats = manager.get_processing_stats()
        assert stats["total_processed"] == 0
        assert "standard" in str(type(stats["current_strategy"])).lower()

        # Po przetworzeniu zadań
        task1 = WorkflowTask("Task 1", TaskPriority.MEDIUM, "First task")
        task2 = WorkflowTask("Task 2", TaskPriority.MEDIUM, "Second task")

        manager.execute_task(task1)
        manager.execute_task(task2)

        stats = manager.get_processing_stats()
        assert stats["total_processed"] == 2


class TestStrategyPattern:
    """Testy wzorca Strategy w kompleksowych scenariuszach"""

    def test_strategy_interchangeability(self):
        """Test wymienności strategii"""
        manager = TaskManager()
        task = WorkflowTask("Flexible task", TaskPriority.MEDIUM, "Can be processed differently")

        # Test z różnymi strategiami
        strategies = [
            (UrgentTaskProcessor(), "urgent"),
            (StandardTaskProcessor(), "standard"),
            (BackgroundTaskProcessor(), "background")
        ]

        for strategy, expected_name in strategies:
            manager.set_strategy(strategy)
            result = manager.execute_task(task)
            assert result["strategy_used"] == expected_name

    def test_different_processing_times(self):
        """Test różnych czasów przetwarzania"""
        task = WorkflowTask("Timing test", TaskPriority.MEDIUM, "Test processing times")

        # Urgent - najszybszy
        urgent_processor = UrgentTaskProcessor()
        start = time.time()
        urgent_result = urgent_processor.process_task(task)
        urgent_time = time.time() - start

        # Standard - średni czas
        standard_processor = StandardTaskProcessor()
        start = time.time()
        standard_result = standard_processor.process_task(task)
        standard_time = time.time() - start

        # Background - najwolniejszy
        background_processor = BackgroundTaskProcessor()
        start = time.time()
        background_result = background_processor.process_task(task)
        background_time = time.time() - start

        # Sprawdź kolejność czasów
        assert urgent_time < standard_time
        assert urgent_time < background_time

    def test_validation_differences(self):
        """Test różnych walidacji w strategiach"""
        # Zadanie z krótkim tytułem
        short_title_task = WorkflowTask("AB", TaskPriority.MEDIUM, "Short title")

        urgent_processor = UrgentTaskProcessor()
        standard_processor = StandardTaskProcessor()

        # Urgent processor akceptuje (sprawdza tylko priorytet)
        urgent_result = urgent_processor.process_task(short_title_task)
        # Standard processor odrzuca (sprawdza długość tytułu)
        standard_result = standard_processor.process_task(short_title_task)

        # Różne wyniki walidacji
        assert urgent_result["validation_passed"] != standard_result["validation_passed"]

    def test_strategy_independence(self):
        """Test niezależności strategii"""
        task = WorkflowTask("Independence test", TaskPriority.HIGH, "Test strategy independence")

        # Każda strategia powinna dać inny wynik
        processors = [
            UrgentTaskProcessor(),
            StandardTaskProcessor(),
            BackgroundTaskProcessor()
        ]

        results = []
        for processor in processors:
            result = processor.process_task(task)
            results.append(result["strategy_used"])

        # Wszystkie strategie powinny być różne
        assert len(set(results)) == len(results)


class TestDemonstrateStrategies:
    """Testy demonstracji strategii (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_strategies(self):
        """Test demonstracji różnych strategii"""
        results = demonstrate_strategies()

        assert isinstance(results, list)
        assert len(results) > 0

        # Sprawdź że mamy wyniki z różnych strategii
        strategy_types = [r["strategy_used"] for r in results]
        assert len(set(strategy_types)) > 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
