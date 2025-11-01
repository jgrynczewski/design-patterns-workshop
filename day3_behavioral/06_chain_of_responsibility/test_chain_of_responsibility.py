"""
Testy dla Chain of Responsibility Pattern - Approval Chain
"""

import pytest
from datetime import datetime
from starter import (
    Priority, ExpenseRequest, ApprovalResult, ApprovalHandler,
    TeamLeadApprover, ManagerApprover, DirectorApprover, CEOApprover,
    ApprovalChainBuilder, demonstrate_approval_chain
)


class TestPriority:
    """Testy enum Priority"""

    def test_priority_values(self):
        """Test wartości enum Priority"""
        assert Priority.LOW.value == "low"
        assert Priority.MEDIUM.value == "medium"
        assert Priority.HIGH.value == "high"
        assert Priority.URGENT.value == "urgent"


class TestExpenseRequest:
    """Testy klasy ExpenseRequest"""

    def test_expense_request_creation(self):
        """Test tworzenia expense request"""
        request = ExpenseRequest(1500.0, "New laptop", Priority.MEDIUM)

        assert request.amount == 1500.0
        assert request.description == "New laptop"
        assert request.priority == Priority.MEDIUM
        assert isinstance(request.created_at, datetime)
        assert request.request_id.startswith("EXP_")

    def test_expense_request_str(self):
        """Test reprezentacji string expense request"""
        request = ExpenseRequest(500.0, "Office supplies", Priority.LOW)
        str_repr = str(request)

        assert "500.0 PLN" in str_repr
        assert "Office supplies" in str_repr
        assert request.request_id in str_repr

    def test_unique_request_ids(self):
        """Test unikalności ID requests"""
        request1 = ExpenseRequest(100.0, "Test 1", Priority.LOW)
        request2 = ExpenseRequest(200.0, "Test 2", Priority.HIGH)

        assert request1.request_id != request2.request_id


class TestApprovalResult:
    """Testy klasy ApprovalResult"""

    def test_approval_result_creation(self):
        """Test tworzenia approval result"""
        result = ApprovalResult(True, "Manager", "Within budget")

        assert result.approved is True
        assert result.approved_by == "Manager"
        assert result.reason == "Within budget"
        assert isinstance(result.processed_at, datetime)
        assert isinstance(result.approval_chain, list)

    def test_approval_result_rejection(self):
        """Test rejection result"""
        result = ApprovalResult(False, "", "Exceeds budget limit")

        assert result.approved is False
        assert result.approved_by == ""
        assert result.reason == "Exceeds budget limit"


class TestApprovalHandler:
    """Testy abstract base class ApprovalHandler"""

    def test_approval_handler_is_abstract(self):
        """Test że ApprovalHandler jest abstract"""
        with pytest.raises(TypeError):
            ApprovalHandler("Test", 1000.0)

    def test_concrete_handlers_inheritance(self):
        """Test że concrete handlers dziedziczą po ApprovalHandler"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        director = DirectorApprover()
        ceo = CEOApprover()

        assert isinstance(team_lead, ApprovalHandler)
        assert isinstance(manager, ApprovalHandler)
        assert isinstance(director, ApprovalHandler)
        assert isinstance(ceo, ApprovalHandler)


class TestTeamLeadApprover:
    """Testy Team Lead Approver"""

    def test_team_lead_creation(self):
        """Test tworzenia team lead approver"""
        team_lead = TeamLeadApprover()

        assert team_lead.name == "Team Lead"
        assert team_lead.approval_limit == 1000.0
        assert len(team_lead.processed_requests) == 0

    def test_team_lead_can_handle_small_amounts(self):
        """Test że team lead może obsłużyć małe kwoty"""
        team_lead = TeamLeadApprover()
        small_request = ExpenseRequest(500.0, "Office supplies", Priority.LOW)

        assert team_lead.can_handle(small_request) is True

    def test_team_lead_cannot_handle_large_amounts(self):
        """Test że team lead nie może obsłużyć dużych kwot"""
        team_lead = TeamLeadApprover()
        large_request = ExpenseRequest(2000.0, "Expensive equipment", Priority.HIGH)

        assert team_lead.can_handle(large_request) is False

    def test_team_lead_process_request(self):
        """Test przetwarzania request przez team lead"""
        team_lead = TeamLeadApprover()
        request = ExpenseRequest(800.0, "Team lunch", Priority.LOW)

        result = team_lead.process_request(request)

        assert result.approved is True
        assert result.approved_by == "Team Lead"

    def test_team_lead_priority_restrictions(self):
        """Test ograniczeń priorytetów dla team lead"""
        team_lead = TeamLeadApprover()

        # LOW i MEDIUM powinny być OK
        low_request = ExpenseRequest(500.0, "Supplies", Priority.LOW)
        medium_request = ExpenseRequest(500.0, "Software", Priority.MEDIUM)

        low_result = team_lead.process_request(low_request)
        medium_result = team_lead.process_request(medium_request)

        assert low_result.approved is True
        assert medium_result.approved is True

    def test_team_lead_handle_request_within_limit(self):
        """Test obsługi request w ramach limitu"""
        team_lead = TeamLeadApprover()
        request = ExpenseRequest(900.0, "Office equipment", Priority.MEDIUM)

        result = team_lead.handle_request(request)

        assert result.approved is True
        assert result.approved_by == "Team Lead"
        assert len(team_lead.processed_requests) == 1


class TestManagerApprover:
    """Testy Manager Approver"""

    def test_manager_creation(self):
        """Test tworzenia manager approver"""
        manager = ManagerApprover()

        assert manager.name == "Manager"
        assert manager.approval_limit == 5000.0

    def test_manager_can_handle_medium_amounts(self):
        """Test że manager może obsłużyć średnie kwoty"""
        manager = ManagerApprover()
        request = ExpenseRequest(3000.0, "New computer", Priority.MEDIUM)

        assert manager.can_handle(request) is True

    def test_manager_cannot_handle_very_large_amounts(self):
        """Test że manager nie może obsłużyć bardzo dużych kwot"""
        manager = ManagerApprover()
        request = ExpenseRequest(10000.0, "Server rack", Priority.HIGH)

        assert manager.can_handle(request) is False

    def test_manager_process_request(self):
        """Test przetwarzania request przez manager"""
        manager = ManagerApprover()
        request = ExpenseRequest(4000.0, "Marketing campaign", Priority.HIGH)

        result = manager.process_request(request)

        assert result.approved is True
        assert result.approved_by == "Manager"


class TestDirectorApprover:
    """Testy Director Approver"""

    def test_director_creation(self):
        """Test tworzenia director approver"""
        director = DirectorApprover()

        assert director.name == "Director"
        assert director.approval_limit == 25000.0

    def test_director_can_handle_large_amounts(self):
        """Test że director może obsłużyć duże kwoty"""
        director = DirectorApprover()
        request = ExpenseRequest(20000.0, "Equipment upgrade", Priority.HIGH)

        assert director.can_handle(request) is True

    def test_director_priority_requirements(self):
        """Test wymagań priorytetów dla director"""
        director = DirectorApprover()

        # Duża kwota z HIGH priority - OK
        high_priority_request = ExpenseRequest(15000.0, "Critical upgrade", Priority.HIGH)
        result_high = director.process_request(high_priority_request)
        assert result_high.approved is True

        # Duża kwota z LOW priority - może być odrzucona
        low_priority_request = ExpenseRequest(15000.0, "Nice to have", Priority.LOW)
        result_low = director.process_request(low_priority_request)
        # Director może odrzucić duże kwoty z niskim priorytetem


class TestCEOApprover:
    """Testy CEO Approver"""

    def test_ceo_creation(self):
        """Test tworzenia CEO approver"""
        ceo = CEOApprover()

        assert ceo.name == "CEO"
        assert ceo.approval_limit == float('inf')

    def test_ceo_can_handle_anything(self):
        """Test że CEO może obsłużyć każdą kwotę"""
        ceo = CEOApprover()

        requests = [
            ExpenseRequest(1000.0, "Small expense", Priority.LOW),
            ExpenseRequest(100000.0, "Major investment", Priority.URGENT),
            ExpenseRequest(1000000.0, "Company acquisition", Priority.HIGH)
        ]

        for request in requests:
            assert ceo.can_handle(request) is True

    def test_ceo_urgent_priority_approval(self):
        """Test że CEO zatwierdza wszystko z priorytetem URGENT"""
        ceo = CEOApprover()
        urgent_request = ExpenseRequest(500000.0, "Emergency equipment", Priority.URGENT)

        result = ceo.process_request(urgent_request)

        assert result.approved is True
        assert result.approved_by == "CEO"

    def test_ceo_large_amount_discretion(self):
        """Test dyskrecji CEO przy bardzo dużych kwotach"""
        ceo = CEOApprover()
        huge_request = ExpenseRequest(75000.0, "Luxury office", Priority.LOW)

        result = ceo.process_request(huge_request)
        # CEO może odrzucić bardzo duże kwoty z niskim priorytetem


class TestChainOfResponsibility:
    """Testy wzorca Chain of Responsibility"""

    def test_chain_setup(self):
        """Test ustawiania łańcucha handlers"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        director = DirectorApprover()

        # Test fluent interface
        returned_manager = team_lead.set_next(manager)
        returned_director = manager.set_next(director)

        assert returned_manager is manager
        assert returned_director is director

    def test_small_expense_approved_by_team_lead(self):
        """Test że małe wydatki są zatwierdzane przez team lead"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        team_lead.set_next(manager)

        small_expense = ExpenseRequest(500.0, "Office supplies", Priority.LOW)
        result = team_lead.handle_request(small_expense)

        assert result.approved is True
        assert result.approved_by == "Team Lead"

    def test_medium_expense_escalated_to_manager(self):
        """Test że średnie wydatki są eskalowane do manager"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        team_lead.set_next(manager)

        medium_expense = ExpenseRequest(3000.0, "New laptop", Priority.MEDIUM)
        result = team_lead.handle_request(medium_expense)

        assert result.approved is True
        assert result.approved_by == "Manager"

    def test_large_expense_escalated_to_director(self):
        """Test że duże wydatki są eskalowane do director"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        director = DirectorApprover()

        team_lead.set_next(manager).set_next(director)

        large_expense = ExpenseRequest(15000.0, "Server upgrade", Priority.HIGH)
        result = team_lead.handle_request(large_expense)

        assert result.approved is True
        assert result.approved_by == "Director"

    def test_huge_expense_escalated_to_ceo(self):
        """Test że ogromne wydatki są eskalowane do CEO"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        director = DirectorApprover()
        ceo = CEOApprover()

        team_lead.set_next(manager).set_next(director).set_next(ceo)

        huge_expense = ExpenseRequest(50000.0, "Major equipment", Priority.URGENT)
        result = team_lead.handle_request(huge_expense)

        assert result.approved is True
        assert result.approved_by == "CEO"

    def test_expense_rejected_when_no_handler_can_approve(self):
        """Test odrzucenia gdy żaden handler nie może zatwierdzić"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        team_lead.set_next(manager)  # Brak director i CEO

        huge_expense = ExpenseRequest(100000.0, "Company jet", Priority.LOW)
        result = team_lead.handle_request(huge_expense)

        assert result.approved is False

    def test_processing_statistics(self):
        """Test statystyk przetwarzania"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        team_lead.set_next(manager)

        # Przetworz kilka requests
        requests = [
            ExpenseRequest(500.0, "Supplies", Priority.LOW),
            ExpenseRequest(2000.0, "Equipment", Priority.MEDIUM),
            ExpenseRequest(800.0, "Software", Priority.LOW)
        ]

        for request in requests:
            team_lead.handle_request(request)

        # Sprawdź statystyki team lead
        stats = team_lead.get_processing_stats()
        assert stats["total_processed"] == 3
        assert stats["handler_name"] == "Team Lead"
        assert stats["approval_limit"] == 1000.0

        # Sprawdź statystyki manager
        manager_stats = manager.get_processing_stats()
        assert manager_stats["total_processed"] == 1  # Tylko jeden przekazany


class TestApprovalChainBuilder:
    """Testy Builder dla łańcucha zatwierdzania"""

    def test_chain_builder_creation(self):
        """Test tworzenia chain builder"""
        builder = ApprovalChainBuilder()
        assert len(builder.handlers) == 0

    def test_chain_builder_fluent_interface(self):
        """Test fluent interface builder"""
        builder = ApprovalChainBuilder()

        result = builder.add_team_lead().add_manager().add_director().add_ceo()

        assert result is builder
        assert len(builder.handlers) == 4

    def test_chain_builder_build_complete_chain(self):
        """Test budowania kompletnego łańcucha"""
        builder = ApprovalChainBuilder()

        chain_head = builder.add_team_lead().add_manager().add_director().add_ceo().build()

        assert isinstance(chain_head, TeamLeadApprover)

    def test_chain_builder_partial_chain(self):
        """Test budowania częściowego łańcucha"""
        builder = ApprovalChainBuilder()

        chain_head = builder.add_team_lead().add_manager().build()

        assert isinstance(chain_head, TeamLeadApprover)

    def test_chain_builder_empty_chain(self):
        """Test budowania pustego łańcucha"""
        builder = ApprovalChainBuilder()

        chain_head = builder.build()

        assert chain_head is None

    def test_built_chain_functionality(self):
        """Test funkcjonalności zbudowanego łańcucha"""
        builder = ApprovalChainBuilder()
        chain_head = builder.add_team_lead().add_manager().add_director().build()

        # Test różnych kwot
        small_expense = ExpenseRequest(500.0, "Small", Priority.LOW)
        medium_expense = ExpenseRequest(3000.0, "Medium", Priority.MEDIUM)
        large_expense = ExpenseRequest(15000.0, "Large", Priority.HIGH)

        small_result = chain_head.handle_request(small_expense)
        medium_result = chain_head.handle_request(medium_expense)
        large_result = chain_head.handle_request(large_expense)

        assert small_result.approved_by == "Team Lead"
        assert medium_result.approved_by == "Manager"
        assert large_result.approved_by == "Director"


class TestComplexScenarios:
    """Testy złożonych scenariuszy"""

    def test_priority_based_routing(self):
        """Test routingu opartego na priorytecie"""
        builder = ApprovalChainBuilder()
        chain_head = builder.add_team_lead().add_manager().add_director().add_ceo().build()

        # URGENT requests mogą być obsługiwane na wyższych poziomach
        urgent_expense = ExpenseRequest(50000.0, "Emergency repair", Priority.URGENT)
        result = chain_head.handle_request(urgent_expense)

        assert result.approved is True
        assert result.approved_by == "CEO"

    def test_multiple_chains_independence(self):
        """Test niezależności wielu łańcuchów"""
        # Pierwszy łańcuch
        builder1 = ApprovalChainBuilder()
        chain1 = builder1.add_team_lead().add_manager().build()

        # Drugi łańcuch
        builder2 = ApprovalChainBuilder()
        chain2 = builder2.add_team_lead().add_director().add_ceo().build()

        expense = ExpenseRequest(15000.0, "Equipment", Priority.HIGH)

        result1 = chain1.handle_request(expense)
        result2 = chain2.handle_request(expense)

        # Pierwszy łańcuch nie może zatwierdzić (brak director/CEO)
        assert result1.approved is False

        # Drugi łańcuch może zatwierdzić
        assert result2.approved is True
        assert result2.approved_by == "Director"

    def test_handler_processing_history(self):
        """Test historii przetwarzania handlers"""
        team_lead = TeamLeadApprover()
        manager = ManagerApprover()
        team_lead.set_next(manager)

        requests = [
            ExpenseRequest(300.0, "Supplies 1", Priority.LOW),
            ExpenseRequest(2000.0, "Equipment 1", Priority.MEDIUM),
            ExpenseRequest(700.0, "Supplies 2", Priority.LOW),
        ]

        for request in requests:
            team_lead.handle_request(request)

        # Team lead przetworzy wszystkie (ale zatwierdzi tylko 2)
        assert len(team_lead.processed_requests) == 3

        # Manager przetworzy tylko 1 (eskalowany)
        assert len(manager.processed_requests) == 1


class TestDemonstrateApprovalChain:
    """Testy demonstracji approval chain (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_approval_chain(self):
        """Test demonstracji łańcucha zatwierdzania"""
        results = demonstrate_approval_chain()

        assert isinstance(results, dict)
        assert "requests_processed" in results
        assert "approval_statistics" in results
        assert "chain_performance" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
