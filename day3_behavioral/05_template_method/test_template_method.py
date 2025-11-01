"""
Testy dla Template Method Pattern - Document Templates
"""

import pytest
from datetime import datetime
from starter import (
    DocumentGenerator,
    ProjectReportGenerator, MeetingNotesGenerator, TechnicalSpecGenerator,
    demonstrate_template_method
)


class TestDocumentGenerator:
    """Testy abstract base class DocumentGenerator"""

    def test_document_generator_is_abstract(self):
        """Test że DocumentGenerator jest abstract"""
        with pytest.raises(TypeError):
            DocumentGenerator("Test")

    def test_concrete_generator_inheritance(self):
        """Test że concrete generators dziedziczą po DocumentGenerator"""
        project_gen = ProjectReportGenerator("Test Report", "2024")
        meeting_gen = MeetingNotesGenerator("Test Meeting", "2024-01-15")
        tech_gen = TechnicalSpecGenerator("Test Spec", "1.0", "TestSystem")

        assert isinstance(project_gen, DocumentGenerator)
        assert isinstance(meeting_gen, DocumentGenerator)
        assert isinstance(tech_gen, DocumentGenerator)


class TestProjectReportGenerator:
    """Testy generatora raportów projektowych"""

    def test_project_report_creation(self):
        """Test tworzenia generatora raportów"""
        generator = ProjectReportGenerator("Q4 Financial Report", "2024")

        assert generator.title == "Q4 Financial Report"
        assert generator.project_year == "2024"
        assert isinstance(generator.creation_time, datetime)

    def test_project_report_header(self):
        """Test nagłówka raportu projektowego"""
        generator = ProjectReportGenerator("Test Report", "2024")
        header = generator.create_header()

        assert "PROJECT REPORT" in header
        assert "Test Report" in header
        assert "2024" in header
        assert "Generated:" in header

    def test_project_report_content(self):
        """Test treści raportu projektowego"""
        generator = ProjectReportGenerator("Test Report", "2024")
        content = generator.create_content()

        assert "EXECUTIVE SUMMARY" in content
        assert "FINANCIAL OVERVIEW" in content
        assert "PROJECT MILESTONES" in content
        assert "RECOMMENDATIONS" in content
        assert len(content) > 100

    def test_project_report_footer(self):
        """Test stopki raportu"""
        generator = ProjectReportGenerator("Test Report", "2024")
        footer = generator.create_footer()

        assert "End of Project Report" in footer
        assert "Document ID:" in footer
        assert "PROJ_2024" in footer

    def test_project_report_validation(self):
        """Test walidacji raportu projektowego"""
        generator = ProjectReportGenerator("Test Report", "2024")
        content = generator.create_content()

        result = generator.validate_content(content)
        assert result is True
        assert generator.document_data["validation_passed"] is True

    def test_project_report_validation_failure(self):
        """Test nieudanej walidacji raportu"""
        generator = ProjectReportGenerator("Test Report", "2024")

        # Treść bez wymaganych sekcji
        invalid_content = "Just some text without required sections"
        result = generator.validate_content(invalid_content)

        assert result is False
        assert generator.document_data["validation_passed"] is False

    def test_project_report_generation(self):
        """Test pełnego generowania raportu"""
        generator = ProjectReportGenerator("Annual Report", "2024")
        document = generator.generate_document()

        assert "PROJECT REPORT" in document
        assert "Annual Report" in document
        assert "EXECUTIVE SUMMARY" in document
        assert "End of Project Report" in document
        assert len(document) > 200

    def test_project_report_metadata(self):
        """Test metadanych raportu"""
        generator = ProjectReportGenerator("Test Report", "2024")
        generator.add_metadata()

        assert "created_at" in generator.document_data
        assert "title" in generator.document_data
        assert generator.document_data["title"] == "Test Report"


class TestMeetingNotesGenerator:
    """Testy generatora notatek ze spotkań"""

    def test_meeting_notes_creation(self):
        """Test tworzenia generatora notatek"""
        generator = MeetingNotesGenerator("Daily Standup", "2024-01-15")

        assert generator.title == "Daily Standup"
        assert generator.meeting_date == "2024-01-15"

    def test_meeting_notes_header(self):
        """Test nagłówka notatek"""
        generator = MeetingNotesGenerator("Team Meeting", "2024-01-15")
        header = generator.create_header()

        assert "MEETING NOTES" in header
        assert "Team Meeting" in header
        assert "2024-01-15" in header

    def test_meeting_notes_content(self):
        """Test treści notatek"""
        generator = MeetingNotesGenerator("Team Meeting", "2024-01-15")
        content = generator.create_content()

        assert "ATTENDEES" in content
        assert "AGENDA" in content
        assert "DISCUSSION POINTS" in content
        assert "ACTION ITEMS" in content
        assert len(content) > 50

    def test_meeting_notes_footer(self):
        """Test stopki notatek"""
        generator = MeetingNotesGenerator("Team Meeting", "2024-01-15")
        footer = generator.create_footer()

        assert "Notes compiled by:" in footer
        assert "Next meeting:" in footer

    def test_meeting_notes_generation(self):
        """Test pełnego generowania notatek"""
        generator = MeetingNotesGenerator("Sprint Planning", "2024-01-15")
        document = generator.generate_document()

        assert "MEETING NOTES" in document
        assert "Sprint Planning" in document
        assert "ATTENDEES" in document
        assert "ACTION ITEMS" in document

    def test_meeting_notes_extended_metadata(self):
        """Test rozszerzonych metadanych dla notatek"""
        generator = MeetingNotesGenerator("Daily Standup", "2024-01-15")
        generator.add_metadata()

        assert "meeting_date" in generator.document_data
        assert "document_type" in generator.document_data
        assert generator.document_data["meeting_date"] == "2024-01-15"
        assert generator.document_data["document_type"] == "meeting_notes"


class TestTechnicalSpecGenerator:
    """Testy generatora specyfikacji technicznych"""

    def test_technical_spec_creation(self):
        """Test tworzenia generatora specyfikacji"""
        generator = TechnicalSpecGenerator("API Specification", "2.1", "PaymentSystem")

        assert generator.title == "API Specification"
        assert generator.version == "2.1"
        assert generator.system_name == "PaymentSystem"

    def test_technical_spec_header(self):
        """Test nagłówka specyfikacji"""
        generator = TechnicalSpecGenerator("API Spec", "1.0", "TestSystem")
        header = generator.create_header()

        assert "TECHNICAL SPECIFICATION" in header
        assert "TestSystem" in header
        assert "1.0" in header
        assert "API Spec" in header

    def test_technical_spec_content(self):
        """Test treści specyfikacji"""
        generator = TechnicalSpecGenerator("API Spec", "1.0", "TestSystem")
        content = generator.create_content()

        assert "OVERVIEW" in content
        assert "ARCHITECTURE" in content
        assert "API ENDPOINTS" in content
        assert "DATA MODELS" in content
        assert "SECURITY" in content

    def test_technical_spec_footer(self):
        """Test stopki specyfikacji"""
        generator = TechnicalSpecGenerator("API Spec", "1.0", "TestSystem")
        footer = generator.create_footer()

        assert "Specification Version: 1.0" in footer
        assert "Last Updated:" in footer
        assert "Status: Draft" in footer

    def test_technical_spec_validation(self):
        """Test walidacji specyfikacji technicznej"""
        generator = TechnicalSpecGenerator("API Spec", "1.0", "TestSystem")
        content = generator.create_content()

        result = generator.validate_content(content)
        assert result is True

    def test_technical_spec_validation_failure(self):
        """Test nieudanej walidacji specyfikacji"""
        generator = TechnicalSpecGenerator("API Spec", "1.0", "TestSystem")

        # Treść bez wymaganych sekcji technicznych
        invalid_content = "Just basic text without technical sections"
        result = generator.validate_content(invalid_content)

        assert result is False

    def test_technical_spec_custom_formatting(self):
        """Test niestandardowego formatowania specyfikacji"""
        generator = TechnicalSpecGenerator("API Spec", "1.0", "TestSystem")
        header = "Header"
        content = "Content"
        footer = "Footer"

        formatted = generator.format_output(header, content, footer)

        assert formatted.startswith("<!DOCTYPE techspec>")
        assert formatted.endswith("</techspec>")
        assert "Header" in formatted
        assert "Content" in formatted
        assert "Footer" in formatted

    def test_technical_spec_generation(self):
        """Test pełnego generowania specyfikacji"""
        generator = TechnicalSpecGenerator("REST API", "2.0", "UserService")
        document = generator.generate_document()

        assert "TECHNICAL SPECIFICATION" in document
        assert "UserService" in document
        assert "ARCHITECTURE" in document
        assert "SECURITY" in document
        assert document.startswith("<!DOCTYPE techspec>")


class TestTemplateMethodPattern:
    """Testy wzorca Template Method w kompleksowych scenariuszach"""

    def test_template_method_algorithm_consistency(self):
        """Test spójności algorytmu template method"""
        generators = [
            ProjectReportGenerator("Test Report", "2024"),
            MeetingNotesGenerator("Test Meeting", "2024-01-15"),
            TechnicalSpecGenerator("Test Spec", "1.0", "TestSystem")
        ]

        for generator in generators:
            # Każdy generator powinien przejść przez te same kroki
            document = generator.generate_document()

            # Sprawdź że dokument został wygenerowany
            assert len(document) > 50

            # Sprawdź że metadane zostały dodane
            assert "created_at" in generator.document_data
            assert "title" in generator.document_data
            assert "validation_passed" in generator.document_data

    def test_hook_methods_customization(self):
        """Test customizacji hook methods"""
        # Meeting notes mają rozszerzone metadane
        meeting_gen = MeetingNotesGenerator("Test Meeting", "2024-01-15")
        meeting_gen.add_metadata()

        # Sprawdź dodatkowe metadane
        assert "meeting_date" in meeting_gen.document_data
        assert "document_type" in meeting_gen.document_data

        # Technical spec ma inne formatowanie
        tech_gen = TechnicalSpecGenerator("Test Spec", "1.0", "TestSystem")
        formatted = tech_gen.format_output("H", "C", "F")

        assert formatted != "H\n\nC\n\nF"  # Nie domyślne formatowanie
        assert "<!DOCTYPE techspec>" in formatted

    def test_validation_differences(self):
        """Test różnic w walidacji między generatorami"""
        # Project report wymaga określonych sekcji
        project_gen = ProjectReportGenerator("Test", "2024")
        valid_project_content = project_gen.create_content()
        invalid_project_content = "Missing required sections"

        assert project_gen.validate_content(valid_project_content) is True
        assert project_gen.validate_content(invalid_project_content) is False

        # Technical spec wymaga innych sekcji
        tech_gen = TechnicalSpecGenerator("Test", "1.0", "System")
        valid_tech_content = tech_gen.create_content()

        assert tech_gen.validate_content(valid_tech_content) is True
        assert tech_gen.validate_content(invalid_project_content) is False

    def test_document_generation_failure(self):
        """Test niepowodzenia generowania dokumentu"""

        # Stwórz generator z niestandardową walidacją
        class FailingGenerator(DocumentGenerator):
            def create_header(self):
                return "Header"

            def create_content(self):
                return "Short"  # Za krótkie

            def create_footer(self):
                return "Footer"

            def validate_content(self, content):
                self.document_data["validation_passed"] = False
                return False

        failing_gen = FailingGenerator("Failing Doc")

        with pytest.raises(ValueError, match="Document validation failed"):
            failing_gen.generate_document()

    def test_multiple_generations(self):
        """Test wielokrotnego generowania dokumentów"""
        generator = ProjectReportGenerator("Multi Test", "2024")

        # Pierwsze generowanie
        doc1 = generator.generate_document()

        # Drugie generowanie (powinno działać)
        doc2 = generator.generate_document()

        # Dokumenty powinny być identyczne (ten sam generator)
        assert doc1 == doc2

    def test_generator_independence(self):
        """Test niezależności różnych generatorów"""
        gen1 = ProjectReportGenerator("Report 1", "2024")
        gen2 = ProjectReportGenerator("Report 2", "2023")

        doc1 = gen1.generate_document()
        doc2 = gen2.generate_document()

        # Dokumenty powinny być różne
        assert doc1 != doc2
        assert "Report 1" in doc1
        assert "Report 2" in doc2
        assert "2024" in doc1
        assert "2023" in doc2

    def test_primitive_operations_implementation(self):
        """Test że wszystkie primitive operations są zaimplementowane"""
        generators = [
            ProjectReportGenerator("Test", "2024"),
            MeetingNotesGenerator("Test", "2024-01-15"),
            TechnicalSpecGenerator("Test", "1.0", "System")
        ]

        for generator in generators:
            # Wszystkie primitive operations powinny działać
            header = generator.create_header()
            content = generator.create_content()
            footer = generator.create_footer()

            assert len(header) > 0
            assert len(content) > 0
            assert len(footer) > 0


class TestDemonstrateTemplateMethod:
    """Testy demonstracji Template Method (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_template_method(self):
        """Test demonstracji wzorca Template Method"""
        results = demonstrate_template_method()

        assert isinstance(results, dict)
        assert "generators_tested" in results
        assert "documents_generated" in results
        assert "validation_results" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
