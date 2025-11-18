"""
Testy dla Template Method Pattern - Document Generation
"""

import pytest
from starter import DocumentGenerator, ReportDocument, EmailDocument


class TestDocumentGenerator:
    """Testy abstract base class DocumentGenerator"""

    def test_document_generator_is_abstract(self):
        """Test że DocumentGenerator jest abstract"""
        with pytest.raises(TypeError):
            DocumentGenerator("Test")

    def test_concrete_generators_inherit(self):
        """Test że concrete generators dziedziczą po DocumentGenerator"""
        report = ReportDocument("Test Report")
        email = EmailDocument("Test Email")

        assert isinstance(report, DocumentGenerator)
        assert isinstance(email, DocumentGenerator)


class TestReportDocument:
    """Testy generatora raportów"""

    def test_report_creation(self):
        """Test tworzenia generatora raportów"""
        report = ReportDocument("Q4 Sales")

        assert report.title == "Q4 Sales"

    def test_report_header(self):
        """Test nagłówka raportu"""
        report = ReportDocument("Test Report")
        header = report.create_header()

        assert "REPORT" in header
        assert "Test Report" in header
        assert "=" in header

    def test_report_body(self):
        """Test treści raportu"""
        report = ReportDocument("Test Report")
        body = report.create_body()

        assert "body" in body.lower() or "report" in body.lower()
        assert "Test Report" in body
        assert len(body) > 10

    def test_report_footer(self):
        """Test stopki raportu"""
        report = ReportDocument("Test Report")
        footer = report.create_footer()

        assert "End of Report" in footer or "Report" in footer
        assert len(footer) > 5

    def test_report_signature_default(self):
        """Test że raport używa domyślnej signature (pusty string)"""
        report = ReportDocument("Test Report")
        signature = report.add_signature()

        assert signature == ""

    def test_report_full_generation(self):
        """Test pełnego generowania raportu"""
        report = ReportDocument("Annual Report")
        document = report.generate_document()

        # Sprawdź że zawiera wszystkie sekcje
        assert "REPORT" in document
        assert "Annual Report" in document
        assert "body" in document.lower() or "report" in document.lower()
        assert "End of Report" in document or "Report" in document

        # Sprawdź że jest odpowiednio długi
        assert len(document) > 100


class TestEmailDocument:
    """Testy generatora emaili"""

    def test_email_creation(self):
        """Test tworzenia generatora emaili"""
        email = EmailDocument("Meeting Reminder")

        assert email.title == "Meeting Reminder"

    def test_email_header(self):
        """Test nagłówka emaila"""
        email = EmailDocument("Test Email")
        header = email.create_header()

        assert "Subject" in header or "From" in header
        assert "Test Email" in header

    def test_email_body(self):
        """Test treści emaila"""
        email = EmailDocument("Test Email")
        body = email.create_body()

        assert "Dear" in body or "email" in body.lower()
        assert "Test Email" in body
        assert len(body) > 10

    def test_email_footer(self):
        """Test stopki emaila"""
        email = EmailDocument("Test Email")
        footer = email.create_footer()

        assert "automated" in footer.lower() or "email" in footer.lower()
        assert len(footer) > 5

    def test_email_signature_overridden(self):
        """Test że email nadpisuje signature"""
        email = EmailDocument("Test Email")
        signature = email.add_signature()

        # Email powinien mieć podpis (nie pusty string)
        assert signature != ""
        assert "regards" in signature.lower() or "team" in signature.lower()

    def test_email_full_generation(self):
        """Test pełnego generowania emaila"""
        email = EmailDocument("Meeting Reminder")
        document = email.generate_document()

        # Sprawdź że zawiera wszystkie sekcje
        assert "Meeting Reminder" in document
        assert "Dear" in document or "email" in document.lower()
        assert "automated" in document.lower() or "email" in document.lower()

        # Sprawdź że zawiera signature
        assert "regards" in document.lower() or "team" in document.lower()

        # Sprawdź że jest odpowiednio długi
        assert len(document) > 100


class TestTemplateMethodPattern:
    """Testy wzorca Template Method"""

    def test_template_method_consistency(self):
        """Test że template method zapewnia spójny flow"""
        report = ReportDocument("Test Report")
        email = EmailDocument("Test Email")

        # Oba generatory używają tego samego template method
        report_doc = report.generate_document()
        email_doc = email.generate_document()

        # Oba powinny wygenerować dokumenty
        assert len(report_doc) > 50
        assert len(email_doc) > 50

    def test_hook_method_optional(self):
        """Test że hook method jest opcjonalny"""
        # ReportDocument nie nadpisuje add_signature - używa domyślnej
        report = ReportDocument("Test")
        assert report.add_signature() == ""

        # EmailDocument nadpisuje add_signature
        email = EmailDocument("Test")
        assert email.add_signature() != ""

    def test_primitive_operations_required(self):
        """Test że wszystkie primitive operations muszą być zaimplementowane"""
        # Próba stworzenia klasy bez implementacji wszystkich abstract methods
        with pytest.raises(TypeError):
            class IncompleteGenerator(DocumentGenerator):
                def create_header(self):
                    return "Header"
                # Brak create_body i create_footer

            IncompleteGenerator("Test")

    def test_template_method_not_overridden(self):
        """Test że subklasy NIE nadpisują template method"""
        report = ReportDocument("Test")
        email = EmailDocument("Test")

        # Obie klasy powinny używać tej samej metody generate_document z base class
        assert type(report).generate_document == type(email).generate_document

    def test_different_documents_different_content(self):
        """Test że różne generatory produkują różną treść"""
        report = ReportDocument("Sales Report")
        email = EmailDocument("Sales Report")

        report_doc = report.generate_document()
        email_doc = email.generate_document()

        # Dokumenty powinny się różnić (różne implementacje kroków)
        assert report_doc != email_doc

    def test_multiple_generations_consistent(self):
        """Test że wielokrotne generowanie daje ten sam wynik"""
        report = ReportDocument("Test")

        doc1 = report.generate_document()
        doc2 = report.generate_document()

        # Powinny być identyczne
        assert doc1 == doc2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
