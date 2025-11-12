"""
Testy dla Mediator Pattern - Team Collaboration
"""

import pytest
from datetime import datetime
from starter import (
    MessageType, TeamRole, Message, TeamMediator,
    WorkflowMediator, TeamMember,
    Developer, Designer, ProjectManager, Tester,
    demonstrate_team_collaboration
)


class TestMessageType:
    """Testy enum MessageType"""

    def test_message_type_values(self):
        """Test wartości enum MessageType"""
        assert MessageType.TASK_ASSIGNMENT.value == "task_assignment"
        assert MessageType.STATUS_UPDATE.value == "status_update"
        assert MessageType.QUESTION.value == "question"
        assert MessageType.ANNOUNCEMENT.value == "announcement"
        assert MessageType.REVIEW_REQUEST.value == "review_request"


class TestTeamRole:
    """Testy enum TeamRole"""

    def test_team_role_values(self):
        """Test wartości enum TeamRole"""
        assert TeamRole.DEVELOPER.value == "developer"
        assert TeamRole.DESIGNER.value == "designer"
        assert TeamRole.PROJECT_MANAGER.value == "project_manager"
        assert TeamRole.TESTER.value == "tester"


class TestMessage:
    """Testy klasy Message"""

    def test_message_creation(self):
        """Test tworzenia wiadomości"""
        message = Message("John", "Hello team", MessageType.ANNOUNCEMENT)

        assert message.sender == "John"
        assert message.content == "Hello team"
        assert message.message_type == MessageType.ANNOUNCEMENT
        assert message.target_roles == []
        assert isinstance(message.timestamp, datetime)
        assert message.message_id.startswith("MSG_")

    def test_message_with_target_roles(self):
        """Test wiadomości z określonymi rolami docelowymi"""
        target_roles = [TeamRole.DEVELOPER, TeamRole.TESTER]
        message = Message("Sarah", "Code review needed", MessageType.REVIEW_REQUEST, target_roles)

        assert message.target_roles == target_roles

    def test_message_str_representation(self):
        """Test reprezentacji string wiadomości"""
        message = Message("Alice", "Design ready", MessageType.STATUS_UPDATE)
        str_repr = str(message)

        assert "status_update" in str_repr
        assert "Alice" in str_repr
        assert "Design ready" in str_repr

    def test_unique_message_ids(self):
        """Test unikalności ID wiadomości"""
        message1 = Message("User1", "Test 1", MessageType.ANNOUNCEMENT)
        message2 = Message("User2", "Test 2", MessageType.QUESTION)

        assert message1.message_id != message2.message_id


class TestTeamMediator:
    """Testy abstract base class TeamMediator"""

    def test_team_mediator_is_abstract(self):
        """Test że TeamMediator jest abstract"""
        with pytest.raises(TypeError):
            TeamMediator()

    def test_workflow_mediator_inheritance(self):
        """Test że WorkflowMediator dziedziczy po TeamMediator"""
        mediator = WorkflowMediator()
        assert isinstance(mediator, TeamMediator)


class TestWorkflowMediator:
    """Testy WorkflowMediator"""

    def test_workflow_mediator_creation(self):
        """Test tworzenia workflow mediator"""
        mediator = WorkflowMediator()

        assert len(mediator.team_members) == 0
        assert len(mediator.message_history) == 0
        assert isinstance(mediator.message_filters, dict)

    def test_add_team_member(self):
        """Test dodawania członka zespołu"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        mediator.add_team_member(developer)

        assert len(mediator.team_members) == 1
        assert developer in mediator.team_members

    def test_add_duplicate_team_member(self):
        """Test dodawania duplikatu członka zespołu"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        mediator.add_team_member(developer)
        mediator.add_team_member(developer)  # Duplikat

        assert len(mediator.team_members) == 1

    def test_remove_team_member(self):
        """Test usuwania członka zespołu"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        mediator.add_team_member(developer)
        mediator.remove_team_member(developer)

        assert len(mediator.team_members) == 0

    def test_send_message_creates_message_history(self):
        """Test że wysłanie wiadomości tworzy historię"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        mediator.send_message(developer, "Test message", MessageType.ANNOUNCEMENT)

        assert len(mediator.message_history) == 1
        assert mediator.message_history[0].sender == "John"
        assert mediator.message_history[0].content == "Test message"

    def test_notify_team_members(self):
        """Test powiadamiania członków zespołu"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)
        pm = ProjectManager("Sarah", mediator)

        mediator.add_team_member(developer)
        mediator.add_team_member(pm)

        message = Message("John", "Task completed", MessageType.STATUS_UPDATE)
        mediator.notify_team_members(message)

        # PM powinien otrzymać wiadomość, ale nie developer (sender)
        assert len(pm.received_messages) == 1
        assert len(developer.received_messages) == 0

    def test_should_receive_message_sender_exclusion(self):
        """Test że sender nie otrzymuje własnej wiadomości"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        message = Message("John", "Test", MessageType.ANNOUNCEMENT)

        should_receive = mediator.should_receive_message(developer, message)
        assert should_receive is False

    def test_should_receive_message_target_roles(self):
        """Test filtrowania na podstawie target_roles"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)
        designer = Designer("Alice", mediator)

        # Wiadomość tylko dla developers
        message = Message("Sarah", "Code review", MessageType.REVIEW_REQUEST, [TeamRole.DEVELOPER])

        dev_should_receive = mediator.should_receive_message(developer, message)
        designer_should_receive = mediator.should_receive_message(designer, message)

        assert dev_should_receive is True
        assert designer_should_receive is False

    def test_get_message_statistics(self):
        """Test statystyk wiadomości"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)
        pm = ProjectManager("Sarah", mediator)

        mediator.add_team_member(developer)
        mediator.add_team_member(pm)

        # Wyślij różne typy wiadomości
        mediator.send_message(developer, "Task done", MessageType.STATUS_UPDATE)
        mediator.send_message(pm, "Sprint planning", MessageType.ANNOUNCEMENT)
        mediator.send_message(developer, "Need help", MessageType.QUESTION)

        stats = mediator.get_message_statistics()

        assert stats["total_messages"] == 3
        assert stats["messages_by_type"][MessageType.STATUS_UPDATE.value] == 1
        assert stats["messages_by_type"][MessageType.ANNOUNCEMENT.value] == 1
        assert stats["messages_by_type"][MessageType.QUESTION.value] == 1
        assert stats["active_team_members"] == 2


class TestTeamMember:
    """Testy abstract base class TeamMember"""

    def test_team_member_is_abstract(self):
        """Test że TeamMember jest abstract"""
        mediator = WorkflowMediator()

        with pytest.raises(TypeError):
            TeamMember("Test", mediator, TeamRole.DEVELOPER)

    def test_concrete_members_inheritance(self):
        """Test że concrete members dziedziczą po TeamMember"""
        mediator = WorkflowMediator()

        developer = Developer("John", mediator)
        designer = Designer("Alice", mediator)
        pm = ProjectManager("Sarah", mediator)
        tester = Tester("Bob", mediator)

        assert isinstance(developer, TeamMember)
        assert isinstance(designer, TeamMember)
        assert isinstance(pm, TeamMember)
        assert isinstance(tester, TeamMember)


class TestDeveloper:
    """Testy Developer"""

    def test_developer_creation(self):
        """Test tworzenia developer"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        assert developer.name == "John"
        assert developer.role == TeamRole.DEVELOPER
        assert developer.mediator is mediator
        assert len(developer.received_messages) == 0
        assert developer.sent_messages_count == 0

    def test_developer_send_message(self):
        """Test wysyłania wiadomości przez developer"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        developer.send_message("Hello", MessageType.ANNOUNCEMENT)

        assert developer.sent_messages_count == 1
        assert len(mediator.message_history) == 1

    def test_developer_receive_message(self):
        """Test otrzymywania wiadomości przez developer"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        message = Message("Sarah", "New task", MessageType.TASK_ASSIGNMENT)
        developer.receive_message(message)

        assert len(developer.received_messages) == 1

    def test_developer_complete_task(self):
        """Test zgłaszania ukończenia zadania przez developer"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        developer.complete_task("Login feature implemented")

        assert developer.sent_messages_count == 1
        assert len(mediator.message_history) == 1
        assert mediator.message_history[0].message_type == MessageType.STATUS_UPDATE

    def test_developer_request_code_review(self):
        """Test prośby o code review"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        developer.request_code_review("Payment module needs review")

        assert developer.sent_messages_count == 1
        assert mediator.message_history[0].message_type == MessageType.REVIEW_REQUEST

    def test_developer_get_message_stats(self):
        """Test statystyk wiadomości developer"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)

        # Wyślij i otrzymaj wiadomości
        developer.send_message("Test", MessageType.ANNOUNCEMENT)
        message = Message("Sarah", "Reply", MessageType.QUESTION)
        developer.receive_message(message)

        stats = developer.get_message_stats()

        assert stats["sent_count"] == 1
        assert stats["received_count"] == 1
        assert stats["role"] == TeamRole.DEVELOPER.value
        assert stats["name"] == "John"


class TestDesigner:
    """Testy Designer"""

    def test_designer_creation(self):
        """Test tworzenia designer"""
        mediator = WorkflowMediator()
        designer = Designer("Alice", mediator)

        assert designer.name == "Alice"
        assert designer.role == TeamRole.DESIGNER

    def test_designer_share_mockups(self):
        """Test udostępniania mockupów przez designer"""
        mediator = WorkflowMediator()
        designer = Designer("Alice", mediator)

        designer.share_mockups("New login page mockups available")

        assert designer.sent_messages_count == 1
        assert mediator.message_history[0].message_type == MessageType.ANNOUNCEMENT


class TestProjectManager:
    """Testy Project Manager"""

    def test_project_manager_creation(self):
        """Test tworzenia project manager"""
        mediator = WorkflowMediator()
        pm = ProjectManager("Sarah", mediator)

        assert pm.name == "Sarah"
        assert pm.role == TeamRole.PROJECT_MANAGER

    def test_pm_assign_task(self):
        """Test przypisywania zadania przez PM"""
        mediator = WorkflowMediator()
        pm = ProjectManager("Sarah", mediator)

        pm.assign_task("Implement user authentication", TeamRole.DEVELOPER)

        assert pm.sent_messages_count == 1
        assert mediator.message_history[0].message_type == MessageType.TASK_ASSIGNMENT
        assert TeamRole.DEVELOPER in mediator.message_history[0].target_roles

    def test_pm_make_announcement(self):
        """Test ogłoszenia przez PM"""
        mediator = WorkflowMediator()
        pm = ProjectManager("Sarah", mediator)

        pm.make_announcement("Sprint review tomorrow at 2 PM")

        assert pm.sent_messages_count == 1
        assert mediator.message_history[0].message_type == MessageType.ANNOUNCEMENT


class TestTester:
    """Testy Tester"""

    def test_tester_creation(self):
        """Test tworzenia tester"""
        mediator = WorkflowMediator()
        tester = Tester("Bob", mediator)

        assert tester.name == "Bob"
        assert tester.role == TeamRole.TESTER

    def test_tester_report_bug(self):
        """Test zgłaszania błędu przez tester"""
        mediator = WorkflowMediator()
        tester = Tester("Bob", mediator)

        tester.report_bug("Login button not working on mobile")

        assert tester.sent_messages_count == 1
        assert mediator.message_history[0].message_type == MessageType.QUESTION
        assert TeamRole.DEVELOPER in mediator.message_history[0].target_roles

    def test_tester_approve_feature(self):
        """Test zatwierdzania feature przez tester"""
        mediator = WorkflowMediator()
        tester = Tester("Bob", mediator)

        tester.approve_feature("User registration feature tested and approved")

        assert tester.sent_messages_count == 1
        assert mediator.message_history[0].message_type == MessageType.STATUS_UPDATE


class TestMediatorPattern:
    """Testy wzorca Mediator w kompleksowych scenariuszach"""

    def test_full_team_communication(self):
        """Test komunikacji pełnego zespołu"""
        mediator = WorkflowMediator()

        developer = Developer("John", mediator)
        designer = Designer("Alice", mediator)
        pm = ProjectManager("Sarah", mediator)
        tester = Tester("Bob", mediator)

        # Dodaj wszystkich do mediator
        mediator.add_team_member(developer)
        mediator.add_team_member(designer)
        mediator.add_team_member(pm)
        mediator.add_team_member(tester)

        # PM przypisuje zadanie
        pm.assign_task("Create user profile page", TeamRole.DEVELOPER)

        # Developer otrzymuje zadanie
        assert len(developer.received_messages) == 1
        assert developer.received_messages[0].message_type == MessageType.TASK_ASSIGNMENT

        # Designer nie otrzymuje zadania dla developer
        assert len(designer.received_messages) == 0

    def test_workflow_scenario(self):
        """Test typowego scenariusza workflow"""
        mediator = WorkflowMediator()

        developer = Developer("John", mediator)
        designer = Designer("Alice", mediator)
        pm = ProjectManager("Sarah", mediator)
        tester = Tester("Bob", mediator)

        for member in [developer, designer, pm, tester]:
            mediator.add_team_member(member)

        # 1. PM ogłasza sprint
        pm.make_announcement("Sprint 5 starts today")

        # 2. Designer udostępnia mockupy
        designer.share_mockups("Profile page designs ready")

        # 3. PM przypisuje zadanie developer
        pm.assign_task("Implement profile page", TeamRole.DEVELOPER)

        # 4. Developer kończy zadanie
        developer.complete_task("Profile page implemented")

        # 5. Tester zgłasza błąd
        tester.report_bug("Profile image upload not working")

        # 6. Developer prosi o review po poprawce
        developer.request_code_review("Fixed image upload, please review")

        # Sprawdź komunikację
        assert len(mediator.message_history) == 6

        # Każdy powinien otrzymać announcement
        for member in [developer, designer, tester]:  # Nie PM (sender)
            announcements = [msg for msg in member.received_messages
                             if msg.message_type == MessageType.ANNOUNCEMENT]
            assert len(announcements) >= 1

    def test_message_filtering_by_role(self):
        """Test filtrowania wiadomości na podstawie roli"""
        mediator = WorkflowMediator()

        developer1 = Developer("John", mediator)
        developer2 = Developer("Jane", mediator)
        designer = Designer("Alice", mediator)
        pm = ProjectManager("Sarah", mediator)

        for member in [developer1, developer2, designer, pm]:
            mediator.add_team_member(member)

        # Wiadomość tylko dla developers
        pm.assign_task("Fix critical bug", TeamRole.DEVELOPER)

        # Tylko developers powinni otrzymać
        assert len(developer1.received_messages) == 1
        assert len(developer2.received_messages) == 1
        assert len(designer.received_messages) == 0

    def test_mediator_independence(self):
        """Test niezależności różnych mediators"""
        mediator1 = WorkflowMediator()
        mediator2 = WorkflowMediator()

        dev1 = Developer("John", mediator1)
        dev2 = Developer("Jane", mediator2)

        mediator1.add_team_member(dev1)
        mediator2.add_team_member(dev2)

        dev1.send_message("Hello from team 1", MessageType.ANNOUNCEMENT)
        dev2.send_message("Hello from team 2", MessageType.ANNOUNCEMENT)

        # Każdy mediator powinien mieć własną historię
        assert len(mediator1.message_history) == 1
        assert len(mediator2.message_history) == 1
        assert mediator1.message_history[0].content != mediator2.message_history[0].content

    def test_complex_communication_patterns(self):
        """Test złożonych wzorców komunikacji"""
        mediator = WorkflowMediator()

        developers = [Developer(f"Dev{i}", mediator) for i in range(3)]
        testers = [Tester(f"Tester{i}", mediator) for i in range(2)]
        pm = ProjectManager("PM", mediator)

        all_members = developers + testers + [pm]
        for member in all_members:
            mediator.add_team_member(member)

        # PM przypisuje zadania różnym grupom
        pm.assign_task("Implement feature A", TeamRole.DEVELOPER)
        pm.assign_task("Test feature B", TeamRole.TESTER)

        # Sprawdź że odpowiednie grupy otrzymały zadania
        for dev in developers:
            dev_tasks = [msg for msg in dev.received_messages
                         if msg.message_type == MessageType.TASK_ASSIGNMENT and
                         "feature A" in msg.content]
            assert len(dev_tasks) == 1

        for tester in testers:
            tester_tasks = [msg for msg in tester.received_messages
                            if msg.message_type == MessageType.TASK_ASSIGNMENT and
                            "feature B" in msg.content]
            assert len(tester_tasks) == 1

    def test_message_processing_customization(self):
        """Test customizacji przetwarzania wiadomości"""
        mediator = WorkflowMediator()
        developer = Developer("John", mediator)
        pm = ProjectManager("Sarah", mediator)

        mediator.add_team_member(developer)
        mediator.add_team_member(pm)

        # Wyślij różne typy wiadomości
        task_message = Message("Sarah", "New task", MessageType.TASK_ASSIGNMENT)
        question_message = Message("Sarah", "Technical question", MessageType.QUESTION)

        developer.receive_message(task_message)
        developer.receive_message(question_message)

        # Developer powinien przetworzyć różne typy wiadomości
        assert len(developer.received_messages) == 2


class TestDemonstrateTeamCollaboration:
    """Testy demonstracji team collaboration (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_team_collaboration(self):
        """Test demonstracji współpracy zespołu"""
        results = demonstrate_team_collaboration()

        assert isinstance(results, dict)
        assert "workflow_steps" in results
        assert "communication_stats" in results
        assert "team_members" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
