"""
Testy dla State Pattern - Workflow States
"""

import pytest
from starter import (
    OperationNotAllowedError, DocumentStateType, DocumentState,
    DraftState, ReviewState, ApprovedState, PublishedState,
    DocumentContext, demonstrate_document_workflow
)


class TestOperationNotAllowedError:
    """Testy custom exception"""

    def test_operation_not_allowed_error(self):
        """Test rzucania wyjątku"""
        with pytest.raises(OperationNotAllowedError):
            raise OperationNotAllowedError("Test error")


class TestDocumentStateType:
    """Testy enum DocumentStateType"""

    def test_document_state_type_values(self):
        """Test wartości enum"""
        assert DocumentStateType.DRAFT.value == "draft"
        assert DocumentStateType.REVIEW.value == "review"
        assert DocumentStateType.APPROVED.value == "approved"
        assert DocumentStateType.PUBLISHED.value == "published"


class TestDraftState:
    """Testy stanu Draft"""

    def test_draft_state_implements_interface(self):
        """Test że DraftState implementuje DocumentState"""
        state = DraftState()
        assert isinstance(state, DocumentState)

    def test_draft_state_name(self):
        """Test nazwy stanu"""
        state = DraftState()
        assert state.get_state_name() == "draft"

    def test_draft_allows_editing(self):
        """Test że draft pozwala na edycję"""
        context = DocumentContext("Test Document")
        state = DraftState()

        # Nie powinno rzucać błędu
        state.edit(context, "New content")
        assert context.content == "New content"

    def test_draft_allows_submit_for_review(self):
        """Test wysłania do przeglądu z draft"""
        context = DocumentContext("Test Document")
        context.edit("Some content")  # Dodaj treść
        state = DraftState()

        state.submit_for_review(context)
        assert context.get_current_state_name() == "review"

    def test_draft_submit_empty_content(self):
        """Test wysłania pustego dokumentu do przeglądu"""
        context = DocumentContext("Test Document")
        state = DraftState()

        # Powinno rzucić błąd dla pustego contentu
        with pytest.raises(OperationNotAllowedError):
            state.submit_for_review(context)

    def test_draft_blocks_approve(self):
        """Test że draft blokuje zatwierdzenie"""
        context = DocumentContext("Test Document")
        state = DraftState()

        with pytest.raises(OperationNotAllowedError):
            state.approve(context)

    def test_draft_blocks_reject(self):
        """Test że draft blokuje odrzucenie"""
        context = DocumentContext("Test Document")
        state = DraftState()

        with pytest.raises(OperationNotAllowedError):
            state.reject(context)

    def test_draft_blocks_publish(self):
        """Test że draft blokuje publikację"""
        context = DocumentContext("Test Document")
        state = DraftState()

        with pytest.raises(OperationNotAllowedError):
            state.publish(context)


class TestReviewState:
    """Testy stanu Review"""

    def test_review_state_implements_interface(self):
        """Test że ReviewState implementuje DocumentState"""
        state = ReviewState()
        assert isinstance(state, DocumentState)

    def test_review_state_name(self):
        """Test nazwy stanu"""
        state = ReviewState()
        assert state.get_state_name() == "review"

    def test_review_blocks_editing(self):
        """Test że review blokuje edycję"""
        context = DocumentContext("Test Document")
        state = ReviewState()

        with pytest.raises(OperationNotAllowedError):
            state.edit(context, "New content")

    def test_review_blocks_submit_for_review(self):
        """Test że review blokuje ponowne wysłanie"""
        context = DocumentContext("Test Document")
        state = ReviewState()

        with pytest.raises(OperationNotAllowedError):
            state.submit_for_review(context)

    def test_review_allows_approve(self):
        """Test zatwierdzenia w review"""
        context = DocumentContext("Test Document")
        context.set_state(ReviewState())

        context.approve()
        assert context.get_current_state_name() == "approved"

    def test_review_allows_reject(self):
        """Test odrzucenia w review"""
        context = DocumentContext("Test Document")
        context.set_state(ReviewState())

        context.reject("Needs more work")
        assert context.get_current_state_name() == "draft"
        assert context.rejection_reason == "Needs more work"

    def test_review_blocks_publish(self):
        """Test że review blokuje publikację"""
        context = DocumentContext("Test Document")
        state = ReviewState()

        with pytest.raises(OperationNotAllowedError):
            state.publish(context)


class TestApprovedState:
    """Testy stanu Approved"""

    def test_approved_state_implements_interface(self):
        """Test że ApprovedState implementuje DocumentState"""
        state = ApprovedState()
        assert isinstance(state, DocumentState)

    def test_approved_state_name(self):
        """Test nazwy stanu"""
        state = ApprovedState()
        assert state.get_state_name() == "approved"

    def test_approved_blocks_editing(self):
        """Test że approved blokuje edycję"""
        context = DocumentContext("Test Document")
        state = ApprovedState()

        with pytest.raises(OperationNotAllowedError):
            state.edit(context, "New content")

    def test_approved_blocks_submit_for_review(self):
        """Test że approved blokuje wysłanie do przeglądu"""
        context = DocumentContext("Test Document")
        state = ApprovedState()

        with pytest.raises(OperationNotAllowedError):
            state.submit_for_review(context)

    def test_approved_blocks_approve(self):
        """Test że approved blokuje ponowne zatwierdzenie"""
        context = DocumentContext("Test Document")
        state = ApprovedState()

        with pytest.raises(OperationNotAllowedError):
            state.approve(context)

    def test_approved_blocks_reject(self):
        """Test że approved blokuje odrzucenie"""
        context = DocumentContext("Test Document")
        state = ApprovedState()

        with pytest.raises(OperationNotAllowedError):
            state.reject(context)

    def test_approved_allows_publish(self):
        """Test publikacji z approved"""
        context = DocumentContext("Test Document")
        context.set_state(ApprovedState())

        context.publish()
        assert context.get_current_state_name() == "published"


class TestPublishedState:
    """Testy stanu Published"""

    def test_published_state_implements_interface(self):
        """Test że PublishedState implementuje DocumentState"""
        state = PublishedState()
        assert isinstance(state, DocumentState)

    def test_published_state_name(self):
        """Test nazwy stanu"""
        state = PublishedState()
        assert state.get_state_name() == "published"

    def test_published_blocks_all_modifications(self):
        """Test że published blokuje wszystkie modyfikacje"""
        context = DocumentContext("Test Document")
        state = PublishedState()

        with pytest.raises(OperationNotAllowedError):
            state.edit(context, "New content")

        with pytest.raises(OperationNotAllowedError):
            state.submit_for_review(context)

        with pytest.raises(OperationNotAllowedError):
            state.approve(context)

        with pytest.raises(OperationNotAllowedError):
            state.reject(context)

        with pytest.raises(OperationNotAllowedError):
            state.publish(context)


class TestDocumentContext:
    """Testy DocumentContext"""

    def test_document_context_creation(self):
        """Test tworzenia kontekstu dokumentu"""
        context = DocumentContext("Test Document")

        assert context.title == "Test Document"
        assert context.content == ""
        assert context.rejection_reason == ""
        assert context.get_current_state_name() == "draft"

    def test_document_context_edit_delegation(self):
        """Test delegacji edycji do stanu"""
        context = DocumentContext("Test Document")

        # W draft - powinno działać
        context.edit("New content")
        assert context.content == "New content"

        # Przejdź do review
        context.submit_for_review()

        # W review - powinno rzucić błąd
        with pytest.raises(OperationNotAllowedError):
            context.edit("Another content")

    def test_document_context_state_transitions(self):
        """Test przejść między stanami"""
        context = DocumentContext("Test Document")
        context.edit("Initial content")

        # Draft -> Review
        context.submit_for_review()
        assert context.get_current_state_name() == "review"

        # Review -> Approved
        context.approve()
        assert context.get_current_state_name() == "approved"

        # Approved -> Published
        context.publish()
        assert context.get_current_state_name() == "published"

    def test_document_context_rejection_workflow(self):
        """Test workflow z odrzuceniem"""
        context = DocumentContext("Test Document")
        context.edit("Initial content")
        context.submit_for_review()

        # Odrzuć z powodu
        context.reject("Needs improvement")

        assert context.get_current_state_name() == "draft"
        assert context.rejection_reason == "Needs improvement"

        # Można znów edytować
        context.edit("Improved content")
        assert context.content == "Improved content"

    def test_can_edit_method(self):
        """Test metody can_edit"""
        context = DocumentContext("Test Document")

        # Draft - można edytować
        assert context.can_edit() is True

        # Review - nie można edytować
        context.edit("Content")
        context.submit_for_review()
        assert context.can_edit() is False

        # Approved - nie można edytować
        context.approve()
        assert context.can_edit() is False

        # Published - nie można edytować
        context.publish()
        assert context.can_edit() is False

    def test_get_available_actions(self):
        """Test dostępnych akcji w różnych stanach"""
        context = DocumentContext("Test Document")

        # Draft
        actions = context.get_available_actions()
        assert "edit" in actions
        assert "submit_for_review" in actions
        assert "approve" not in actions

        # Review
        context.edit("Content")
        context.submit_for_review()
        actions = context.get_available_actions()
        assert "edit" not in actions
        assert "approve" in actions
        assert "reject" in actions

    def test_get_document_info(self):
        """Test informacji o dokumencie"""
        context = DocumentContext("Test Document")
        context.edit("Some content")

        info = context.get_document_info()

        assert info["title"] == "Test Document"
        assert info["current_state"] == "draft"
        assert info["content_length"] == len("Some content")
        assert info["can_edit"] is True
        assert info["rejection_reason"] == ""


class TestStatePattern:
    """Testy wzorca State w kompleksowych scenariuszach"""

    def test_complete_workflow_success(self):
        """Test kompletnego workflow bez problemów"""
        context = DocumentContext("Project Documentation")

        # Draft phase
        context.edit("Initial documentation")
        context.edit("Updated documentation")
        assert context.get_current_state_name() == "draft"

        # Review phase
        context.submit_for_review()
        assert context.get_current_state_name() == "review"

        # Approval phase
        context.approve()
        assert context.get_current_state_name() == "approved"

        # Publication
        context.publish()
        assert context.get_current_state_name() == "published"

        # Verify final state
        assert context.can_edit() is False
        assert context.content == "Updated documentation"

    def test_workflow_with_rejection_and_resubmission(self):
        """Test workflow z odrzuceniem i ponownym wysłaniem"""
        context = DocumentContext("Report")

        # Initial submission
        context.edit("First draft")
        context.submit_for_review()

        # Rejection
        context.reject("Missing key sections")
        assert context.get_current_state_name() == "draft"

        # Improvements and resubmission
        context.edit("Improved draft with all sections")
        context.submit_for_review()

        # Final approval and publication
        context.approve()
        context.publish()

        assert context.get_current_state_name() == "published"

    def test_state_transition_restrictions(self):
        """Test ograniczeń przejść między stanami"""
        context = DocumentContext("Test Document")
        context.edit("Content")

        # Nie można przeskoczyć stanów
        with pytest.raises(OperationNotAllowedError):
            context.approve()  # Nie w review

        with pytest.raises(OperationNotAllowedError):
            context.publish()  # Nie w approved

        context.submit_for_review()

        # W review nie można publikować
        with pytest.raises(OperationNotAllowedError):
            context.publish()  # Musi być approved

    def test_multiple_documents_independence(self):
        """Test niezależności wielu dokumentów"""
        doc1 = DocumentContext("Document 1")
        doc2 = DocumentContext("Document 2")

        # Różne ścieżki dla różnych dokumentów
        doc1.edit("Content 1")
        doc1.submit_for_review()

        doc2.edit("Content 2")
        # doc2 pozostaje w draft

        # Sprawdź niezależność stanów
        assert doc1.get_current_state_name() == "review"
        assert doc2.get_current_state_name() == "draft"

        # doc2 może być nadal edytowany
        doc2.edit("Updated content 2")
        assert doc2.content == "Updated content 2"

        # doc1 nie może być edytowany
        with pytest.raises(OperationNotAllowedError):
            doc1.edit("Cannot edit")

    def test_state_object_reuse(self):
        """Test ponownego użycia obiektów stanów"""
        doc1 = DocumentContext("Doc 1")
        doc2 = DocumentContext("Doc 2")

        # Oba dokumenty przechodzą przez review
        doc1.edit("Content 1")
        doc1.submit_for_review()
        doc1.reject("Needs work")  # Wraca do draft

        doc2.edit("Content 2")
        doc2.submit_for_review()

        # Oba powinny działać niezależnie
        assert doc1.get_current_state_name() == "draft"
        assert doc2.get_current_state_name() == "review"

    def test_edge_cases(self):
        """Test przypadków brzegowych"""
        context = DocumentContext("Edge Case Doc")

        # Próba submit pustego dokumentu
        with pytest.raises(OperationNotAllowedError):
            context.submit_for_review()

        # Edycja pustym stringiem
        context.edit("")
        assert context.content == ""

        # Odrzucenie z pustym powodem
        context.edit("Content")
        context.submit_for_review()
        context.reject("")  # Pusty powód
        assert context.rejection_reason == ""


class TestDemonstrateDocumentWorkflow:
    """Testy demonstracji workflow (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_document_workflow(self):
        """Test demonstracji workflow dokumentu"""
        results = demonstrate_document_workflow()

        assert isinstance(results, dict)
        assert "workflow_steps" in results
        assert "final_state" in results
        assert "rejected_count" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
