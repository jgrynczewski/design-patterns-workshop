"""
Template Method Pattern - Document Generation

>>> # Test Report Document
>>> report = ReportDocument("Q4 Sales")
>>> doc = report.generate_document()
>>> "REPORT" in doc
True
>>> "Q4 Sales" in doc
True
>>> "End of Report" in doc
True

>>> # Test Email Document
>>> email = EmailDocument("Meeting Reminder")
>>> doc = email.generate_document()
>>> "Subject: Meeting Reminder" in doc
True
>>> "Dear User" in doc
True
>>> "automated email" in doc
True

>>> # Test hook method - signature
>>> report = ReportDocument("Test")
>>> report.add_signature()  # Hook method - domyślnie pusta implementacja
''
>>> email = EmailDocument("Test")
>>> email.add_signature()  # Email ma własną implementację
'Best regards,\\nThe Team'
"""

from abc import ABC, abstractmethod


# Document Generator - CZĘŚCIOWO GOTOWE
# WZORZEC: Base class z template method

class DocumentGenerator(ABC):
    """Bazowa klasa dla generatorów dokumentów"""

    def __init__(self, title: str):
        self.title = title

    def generate_document(self) -> str:
        """
        TEMPLATE METHOD - definiuje szkielet algorytmu

        KLUCZOWE: Ta metoda NIE jest abstrakcyjna - definiuje flow
        Subklasy NIE nadpisują tej metody, tylko implementują kroki
        """
        # TODO: Zaimplementuj szkielet algorytmu:
        # 1. header = self.create_header()
        # 2. body = self.create_body()
        # 3. signature = self.add_signature()  # Hook method
        # 4. footer = self.create_footer()
        # 5. Połącz wszystko w result (z "\n\n" między sekcjami)
        # 6. return result
        pass

    @abstractmethod
    def create_header(self) -> str:
        """Stwórz nagłówek - ABSTRACT (primitive operation)"""
        pass

    @abstractmethod
    def create_body(self) -> str:
        """Stwórz główną treść - ABSTRACT (primitive operation)"""
        pass

    @abstractmethod
    def create_footer(self) -> str:
        """Stwórz stopkę - ABSTRACT (primitive operation)"""
        pass

    def add_signature(self) -> str:
        """
        Hook method - opcjonalny podpis

        KLUCZOWE: Ma domyślną implementację (pusty string)
        Subklasy MOGĄ nadpisać, ale nie muszą
        """
        return ""  # Domyślnie brak podpisu


# Concrete Generators - DO IMPLEMENTACJI
# WZORZEC: Konkretne implementacje primitive operations

# TODO: Zaimplementuj ReportDocument
# Dziedziczy po DocumentGenerator
# Implementuje create_header(), create_body(), create_footer()
# Może nadpisać add_signature() jeśli chce (hook method)

class ReportDocument:
    pass


# TODO: Zaimplementuj EmailDocument
# Dziedziczy po DocumentGenerator
# Implementuje create_header(), create_body(), create_footer()
# NADPISUJE add_signature() - zwraca "Best regards,\nThe Team"

class EmailDocument:
    pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     print("=== REPORT DOCUMENT ===")
#     report = ReportDocument("Q4 Sales Report")
#     print(report.generate_document())
#
#     print("\n" + "=" * 60 + "\n")
#
#     print("=== EMAIL DOCUMENT ===")
#     email = EmailDocument("Meeting Reminder")
#     print(email.generate_document())
