# %% About
# - Name: Template Method - Document Templates
# - Difficulty: easy
# - Lines: 18
# - Minutes: 15
# - Focus: Template Method pattern - algorithm skeleton with customizable steps

# %% Description
"""
Implementuj wzorzec Template Method do generowania różnych typów
dokumentów w workflow system.

Zadanie: Zdefiniuj szkielet procesu generowania z customizowalnymi krokami
"""

# %% Hints
# - DocumentGenerator ma template method generate_document()
# - Abstract methods definiują primitive operations
# - Hook methods to opcjonalne rozszerzenia (mogą być puste)
# - Concrete classes implementują tylko specyficzne kroki

# %% Doctests
"""
>>> # Test generatora raportów projektowych
>>> generator = ProjectReportGenerator("Q4 Financial Report", "2024")
>>> doc = generator.generate_document()
>>> "PROJECT REPORT" in doc
True
>>> "Q4 Financial Report" in doc
True

>>> # Test generatora notatek
>>> meeting_gen = MeetingNotesGenerator("Daily Standup", "2024-01-15")
>>> notes = meeting_gen.generate_document()
>>> "MEETING NOTES" in notes
True
>>> "Daily Standup" in notes
True

>>> # Test długości dokumentów
>>> len(doc) > 100
True
>>> len(notes) > 100
True

>>> # Test walidacji
>>> generator.document_data["validation_passed"]
True
"""

# %% Imports
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any


# %% TODO: Implement DocumentGenerator (Template Method)

class DocumentGenerator(ABC):
    """Abstract base class dla generatorów dokumentów"""

    def __init__(self, title: str):
        """Inicjalizuj generator z tytułem"""
        # TODO:
        # self.title = title
        # self.document_data = {}  # Przechowuje dane dokumentu
        # self.creation_time = datetime.now()
        pass

    def generate_document(self) -> str:
        """Template method - szkielet procesu generowania dokumentu"""
        # TODO: Implementuj szkielet:
        # 1. header = self.create_header()
        # 2. content = self.create_content()
        # 3. self.add_metadata()  # Hook method
        # 4. validation_result = self.validate_content(content)
        # 5. footer = self.create_footer()
        # 6. if validation_result: return self.format_output(header, content, footer)
        # 7. else: raise ValueError("Document validation failed")
        pass

    @abstractmethod
    def create_header(self) -> str:
        """Stwórz nagłówek dokumentu (primitive operation)"""
        pass

    @abstractmethod
    def create_content(self) -> str:
        """Stwórz główną treść dokumentu (primitive operation)"""
        pass

    @abstractmethod
    def create_footer(self) -> str:
        """Stwórz stopkę dokumentu (primitive operation)"""
        pass

    def add_metadata(self) -> None:
        """Hook method - dodaj metadane (opcjonalne)"""
        # TODO: Domyślna implementacja - dodaj podstawowe metadane:
        # self.document_data["created_at"] = self.creation_time
        # self.document_data["title"] = self.title
        pass

    def validate_content(self, content: str) -> bool:
        """Hook method - walidacja treści (opcjonalne)"""
        # TODO: Podstawowa walidacja:
        # 1. Sprawdź czy content nie jest pusty
        # 2. Sprawdź czy ma więcej niż 10 znaków
        # 3. Ustaw self.document_data["validation_passed"] = True/False
        # 4. Zwróć wynik walidacji
        pass

    def format_output(self, header: str, content: str, footer: str) -> str:
        """Hook method - formatowanie wyjścia (opcjonalne)"""
        # TODO: Domyślne formatowanie:
        # Połącz header + "\n\n" + content + "\n\n" + footer
        pass


# %% TODO: Implement Concrete Generators

class ProjectReportGenerator:
    """Generator raportów projektowych"""

    def __init__(self, title: str, project_year: str):
        """Inicjalizuj generator raportów"""
        # TODO:
        # super().__init__(title)
        # self.project_year = project_year
        pass

    def create_header(self) -> str:
        """Stwórz nagłówek raportu projektowego"""
        # TODO: Zwróć nagłówek w formacie:
        # "=" * 50
        # "PROJECT REPORT"
        # "=" * 50
        # f"Title: {self.title}"
        # f"Year: {self.project_year}"
        # f"Generated: {self.creation_time.strftime('%Y-%m-%d %H:%M')}"
        pass

    def create_content(self) -> str:
        """Stwórz treść raportu projektowego"""
        # TODO: Zwróć treść raportu:
        # "EXECUTIVE SUMMARY"
        # Przykładową treść raportu (kilka linii)
        # "FINANCIAL OVERVIEW", "PROJECT MILESTONES", "RECOMMENDATIONS"
        pass

    def create_footer(self) -> str:
        """Stwórz stopkę raportu"""
        # TODO: Zwróć stopkę:
        # "-" * 50
        # "End of Project Report"
        # f"Document ID: PROJ_{self.project_year}_{hash(self.title) % 10000}"
        pass

    def validate_content(self, content: str) -> bool:
        """Rozszerzona walidacja dla raportów"""
        # TODO:
        # 1. Wywołaj super().validate_content(content)
        # 2. Sprawdź czy content zawiera "EXECUTIVE SUMMARY"
        # 3. Sprawdź czy content zawiera "RECOMMENDATIONS"
        # 4. Ustaw validation_passed odpowiednio
        # 5. Zwróć wynik
        pass


class MeetingNotesGenerator:
    """Generator notatek ze spotkań"""

    def __init__(self, title: str, meeting_date: str):
        """Inicjalizuj generator notatek"""
        # TODO:
        # super().__init__(title)
        # self.meeting_date = meeting_date
        pass

    def create_header(self) -> str:
        """Stwórz nagłówek notatek"""
        # TODO: Zwróć nagłówek w formacie:
        # "MEETING NOTES"
        # "=" * 30
        # f"Meeting: {self.title}"
        # f"Date: {self.meeting_date}"
        pass

    def create_content(self) -> str:
        """Stwórz treść notatek"""
        # TODO: Zwróć treść notatek:
        # "ATTENDEES", "AGENDA", "DISCUSSION POINTS", "ACTION ITEMS"
        # Z przykładową treścią dla każdej sekcji
        pass

    def create_footer(self) -> str:
        """Stwórz stopkę notatek"""
        # TODO: Zwróć stopkę:
        # f"Notes compiled by: System"
        # f"Next meeting: TBD"
        pass

    def add_metadata(self) -> None:
        """Dodaj metadane specyficzne dla spotkań"""
        # TODO:
        # 1. Wywołaj super().add_metadata()
        # 2. Dodaj self.document_data["meeting_date"] = self.meeting_date
        # 3. Dodaj self.document_data["document_type"] = "meeting_notes"
        pass


class TechnicalSpecGenerator:
    """Generator specyfikacji technicznych"""

    def __init__(self, title: str, version: str, system_name: str):
        """Inicjalizuj generator specyfikacji"""
        # TODO:
        # super().__init__(title)
        # self.version = version
        # self.system_name = system_name
        pass

    def create_header(self) -> str:
        """Stwórz nagłówek specyfikacji"""
        # TODO: Zwróć nagłówek w formacie:
        # "TECHNICAL SPECIFICATION"
        # "=" * 40
        # f"System: {self.system_name}"
        # f"Version: {self.version}"
        # f"Specification: {self.title}"
        pass

    def create_content(self) -> str:
        """Stwórz treść specyfikacji"""
        # TODO: Zwróć treść specyfikacji:
        # "OVERVIEW", "ARCHITECTURE", "API ENDPOINTS", "DATA MODELS", "SECURITY"
        # Z przykładową treścią techniczną
        pass

    def create_footer(self) -> str:
        """Stwórz stopkę specyfikacji"""
        # TODO: Zwróć stopkę:
        # f"Specification Version: {self.version}"
        # f"Last Updated: {self.creation_time.strftime('%Y-%m-%d')}"
        # "Status: Draft"
        pass

    def validate_content(self, content: str) -> bool:
        """Walidacja specyficzna dla specyfikacji technicznych"""
        # TODO:
        # 1. Wywołaj super().validate_content(content)
        # 2. Sprawdź czy content zawiera "ARCHITECTURE"
        # 3. Sprawdź czy content zawiera "API ENDPOINTS"
        # 4. Sprawdź czy content zawiera "SECURITY"
        # 5. Ustaw validation_passed i zwróć wynik
        pass

    def format_output(self, header: str, content: str, footer: str) -> str:
        """Specjalne formatowanie dla dokumentów technicznych"""
        # TODO: Zwróć format:
        # f"<!DOCTYPE techspec>\n{header}\n\n{content}\n\n{footer}\n</techspec>"
        pass


# %% Example Usage (Optional)

def demonstrate_template_method():
    """Demonstracja wzorca Template Method"""
    # TODO (Opcjonalne):
    # 1. Stwórz różne generatory
    # 2. Wygeneruj dokumenty
    # 3. Porównaj struktury i treści
    # 4. Przetestuj walidację
    # 5. Zwróć wyniki
    pass
