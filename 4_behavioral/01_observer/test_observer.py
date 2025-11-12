"""
Testy dla Observer Pattern - Workflow Notifications
"""

import pytest
from datetime import datetime
from starter import (
    Observer, WorkflowTask, TaskStatus,
    EmailNotifier, SlackNotifier, SMSNotifier, DashboardNotifier,
    create_sample_workflow
)


class TestTaskStatus:
    """Testy enum StatusTask"""

    def test_task_status_values(self):
        """Test wartości enum TaskStatus"""
        assert TaskStatus.ASSIGNED.value == "assigned"
        assert TaskStatus.IN_PROGRESS.value == "in_progress"
        assert TaskStatus.REVIEW.value == "review"
        assert TaskStatus.COMPLETED.value == "completed"


class TestWorkflowTask:
    """Testy klasy WorkflowTask (Subject)"""

    def test_task_creation(self):
        """Test tworzenia zadania"""
        task = WorkflowTask("Fix bug #123", TaskStatus.ASSIGNED)

        assert task.task_id == "Fix bug #123"
        assert task.status == TaskStatus.ASSIGNED
        assert task.get_observer_count() == 0

    def test_add_observer(self):
        """Test dodawania observers"""
        task = WorkflowTask("Test task", TaskStatus.ASSIGNED)
        email_notifier = EmailNotifier("test@example.com")
        slack_notifier = SlackNotifier("#dev")

        task.add_observer(email_notifier)
        assert task.get_observer_count() == 1

        task.add_observer(slack_notifier)
        assert task.get_observer_count() == 2

    def test_remove_observer(self):
        """Test usuwania observers"""
        task = WorkflowTask("Test task", TaskStatus.ASSIGNED)
        email_notifier = EmailNotifier("test@example.com")
        slack_notifier = SlackNotifier("#dev")

        task.add_observer(email_notifier)
        task.add_observer(slack_notifier)
        assert task.get_observer_count() == 2

        task.remove_observer(email_notifier)
        assert task.get_observer_count() == 1

        task.remove_observer(slack_notifier)
        assert task.get_observer_count() == 0

    def test_remove_nonexistent_observer(self):
        """Test usuwania nieistniejącego observer"""
        task = WorkflowTask("Test task", TaskStatus.ASSIGNED)
        email_notifier = EmailNotifier("test@example.com")

        # Nie powinno rzucać błędu
        task.remove_observer(email_notifier)
        assert task.get_observer_count() == 0

    def test_set_status_without_observers(self):
        """Test zmiany statusu bez observers"""
        task = WorkflowTask("Test task", TaskStatus.ASSIGNED)

        task.set_status(TaskStatus.IN_PROGRESS)
        assert task.status == TaskStatus.IN_PROGRESS

    def test_set_status_with_observers(self):
        """Test zmiany statusu z observers"""
        task = WorkflowTask("Test task", TaskStatus.ASSIGNED)
        email_notifier = EmailNotifier("test@example.com")

        task.add_observer(email_notifier)
        task.set_status(TaskStatus.IN_PROGRESS)

        assert task.status == TaskStatus.IN_PROGRESS
        assert len(email_notifier.notifications) == 1


class TestEmailNotifier:
    """Testy EmailNotifier"""

    def test_email_notifier_creation(self):
        """Test tworzenia EmailNotifier"""
        notifier = EmailNotifier("user@example.com")

        assert notifier.email_address == "user@example.com"
        assert len(notifier.notifications) == 0

    def test_email_notifier_implements_observer(self):
        """Test że EmailNotifier implementuje Observer"""
        notifier = EmailNotifier("user@example.com")
        assert isinstance(notifier, Observer)

    def test_email_notification(self):
        """Test wysyłania powiadomienia email"""
        task = WorkflowTask("Email test task", TaskStatus.ASSIGNED)
        notifier = EmailNotifier("dev@company.com")

        notifier.notify(task, TaskStatus.ASSIGNED, TaskStatus.IN_PROGRESS)

        assert len(notifier.notifications) == 1
        notification = notifier.notifications[0]
        assert "Email test task" in notification
        assert "assigned" in notification
        assert "in_progress" in notification

    def test_multiple_email_notifications(self):
        """Test wielu powiadomień email"""
        task = WorkflowTask("Multi test", TaskStatus.ASSIGNED)
        notifier = EmailNotifier("test@example.com")

        notifier.notify(task, TaskStatus.ASSIGNED, TaskStatus.IN_PROGRESS)
        notifier.notify(task, TaskStatus.IN_PROGRESS, TaskStatus.REVIEW)

        assert len(notifier.notifications) == 2


class TestSlackNotifier:
    """Testy SlackNotifier"""

    def test_slack_notifier_creation(self):
        """Test tworzenia SlackNotifier"""
        notifier = SlackNotifier("#development")

        assert notifier.channel == "#development"
        assert len(notifier.messages) == 0

    def test_slack_notifier_implements_observer(self):
        """Test że SlackNotifier implementuje Observer"""
        notifier = SlackNotifier("#dev")
        assert isinstance(notifier, Observer)

    def test_slack_notification(self):
        """Test wysyłania wiadomości do Slack"""
        task = WorkflowTask("Slack test task", TaskStatus.ASSIGNED)
        notifier = SlackNotifier("#dev-team")

        notifier.notify(task, TaskStatus.ASSIGNED, TaskStatus.IN_PROGRESS)

        assert len(notifier.messages) == 1
        message = notifier.messages[0]
        assert "Slack test task" in message
        assert "in_progress" in message
        assert "📋" in message  # Emoji


class TestSMSNotifier:
    """Testy SMSNotifier"""

    def test_sms_notifier_creation(self):
        """Test tworzenia SMSNotifier"""
        notifier = SMSNotifier("+48123456789")

        assert notifier.phone_number == "+48123456789"
        assert len(notifier.sms_sent) == 0

    def test_sms_notifier_implements_observer(self):
        """Test że SMSNotifier implementuje Observer"""
        notifier = SMSNotifier("+48123456789")
        assert isinstance(notifier, Observer)

    def test_sms_notification(self):
        """Test wysyłania SMS"""
        task = WorkflowTask("SMS test", TaskStatus.REVIEW)
        notifier = SMSNotifier("+48987654321")

        notifier.notify(task, TaskStatus.REVIEW, TaskStatus.COMPLETED)

        assert len(notifier.sms_sent) == 1
        sms = notifier.sms_sent[0]
        assert "SMS test" in sms
        assert "review" in sms
        assert "completed" in sms


class TestDashboardNotifier:
    """Testy DashboardNotifier"""

    def test_dashboard_notifier_creation(self):
        """Test tworzenia DashboardNotifier"""
        notifier = DashboardNotifier()

        assert len(notifier.dashboard_updates) == 0

    def test_dashboard_notifier_implements_observer(self):
        """Test że DashboardNotifier implementuje Observer"""
        notifier = DashboardNotifier()
        assert isinstance(notifier, Observer)

    def test_dashboard_notification(self):
        """Test aktualizacji dashboard"""
        task = WorkflowTask("Dashboard test", TaskStatus.ASSIGNED)
        notifier = DashboardNotifier()

        notifier.notify(task, TaskStatus.ASSIGNED, TaskStatus.IN_PROGRESS)

        assert len(notifier.dashboard_updates) == 1
        update = notifier.dashboard_updates[0]
        assert update["task_id"] == "Dashboard test"
        assert update["status"] == "in_progress"
        assert "timestamp" in update
        assert isinstance(update["timestamp"], datetime)


class TestObserverPattern:
    """Testy wzorca Observer w kompleksowych scenariuszach"""

    def test_multiple_observers_single_task(self):
        """Test wielu observers na jednym zadaniu"""
        task = WorkflowTask("Complex task", TaskStatus.ASSIGNED)

        email_notifier = EmailNotifier("manager@company.com")
        slack_notifier = SlackNotifier("#project-alpha")
        sms_notifier = SMSNotifier("+48123456789")
        dashboard_notifier = DashboardNotifier()

        task.add_observer(email_notifier)
        task.add_observer(slack_notifier)
        task.add_observer(sms_notifier)
        task.add_observer(dashboard_notifier)

        # Zmiana statusu powinna powiadomić wszystkich
        task.set_status(TaskStatus.IN_PROGRESS)

        assert len(email_notifier.notifications) == 1
        assert len(slack_notifier.messages) == 1
        assert len(sms_notifier.sms_sent) == 1
        assert len(dashboard_notifier.dashboard_updates) == 1

    def test_workflow_lifecycle(self):
        """Test pełnego cyklu życia workflow"""
        task = WorkflowTask("Lifecycle task", TaskStatus.ASSIGNED)
        email_notifier = EmailNotifier("dev@company.com")
        slack_notifier = SlackNotifier("#updates")

        task.add_observer(email_notifier)
        task.add_observer(slack_notifier)

        # Symuluj pełny cykl workflow
        task.set_status(TaskStatus.IN_PROGRESS)
        task.set_status(TaskStatus.REVIEW)
        task.set_status(TaskStatus.COMPLETED)

        # Każdy observer powinien otrzymać 3 powiadomienia
        assert len(email_notifier.notifications) == 3
        assert len(slack_notifier.messages) == 3

    def test_observer_independence(self):
        """Test niezależności observers"""
        task = WorkflowTask("Independence test", TaskStatus.ASSIGNED)

        email1 = EmailNotifier("user1@example.com")
        email2 = EmailNotifier("user2@example.com")

        task.add_observer(email1)
        task.add_observer(email2)

        task.set_status(TaskStatus.IN_PROGRESS)

        # Oba observers powinny otrzymać powiadomienia
        assert len(email1.notifications) == 1
        assert len(email2.notifications) == 1

        # Usuń jednego observer
        task.remove_observer(email1)
        task.set_status(TaskStatus.REVIEW)

        # Tylko email2 powinien otrzymać drugie powiadomienie
        assert len(email1.notifications) == 1  # Bez zmian
        assert len(email2.notifications) == 2  # Nowe powiadomienie

    def test_dynamic_observer_management(self):
        """Test dynamicznego zarządzania observers"""
        task = WorkflowTask("Dynamic test", TaskStatus.ASSIGNED)

        observers = [
            EmailNotifier(f"user{i}@example.com") for i in range(5)
        ]

        # Dodaj wszystkich observers
        for observer in observers:
            task.add_observer(observer)

        assert task.get_observer_count() == 5

        # Zmiana statusu
        task.set_status(TaskStatus.IN_PROGRESS)

        # Wszyscy powinni otrzymać powiadomienie
        for observer in observers:
            assert len(observer.notifications) == 1

        # Usuń połowę observers
        for observer in observers[:3]:
            task.remove_observer(observer)

        assert task.get_observer_count() == 2

        # Kolejna zmiana statusu
        task.set_status(TaskStatus.REVIEW)

        # Tylko pozostali observers powinni otrzymać powiadomienie
        for observer in observers[:3]:
            assert len(observer.notifications) == 1  # Bez zmian
        for observer in observers[3:]:
            assert len(observer.notifications) == 2  # Nowe powiadomienie


class TestSampleWorkflow:
    """Testy przykładowego workflow (jeśli zaimplementowany)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_sample_workflow_creation(self):
        """Test tworzenia przykładowego workflow"""
        workflow = create_sample_workflow()

        assert isinstance(workflow, WorkflowTask)
        assert workflow.get_observer_count() > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
