"""
Single Responsibility Principle - Report System

>>> report = Report("Sales Q4", ["Revenue: $100k", "Growth: 15%"])
>>> report.get_title()
'Sales Q4'
>>> len(report.get_lines())
2

>>> # Test ReportPrinter console output
>>> printer = ReportPrinter()
>>> output = printer.print_to_console(report)
>>> "Sales Q4" in output
True
>>> "Revenue: $100k" in output
True

>>> # Test ReportPrinter file save
>>> import os
>>> printer.save_to_file(report, "test_report.txt")
>>> os.path.exists("test_report.txt")
True
>>> os.remove("test_report.txt")
"""

# SRP: Single Responsibility Principle
# Każda klasa powinna mieć tylko jeden powód do zmiany

class Report:
    """Odpowiada TYLKO za przechowywanie danych raportu"""

    def __init__(self, title: str, lines: list[str]):
        self.title = title
        self.lines = lines

    def get_title(self) -> str:
        return self.title

    def get_lines(self) -> list[str]:
        return self.lines


# TODO: Zaimplementuj klasę ReportPrinter
# Hint: Odpowiada TYLKO za drukowanie/zapisywanie raportu
# Hint: Przyjmuje Report jako parametr w metodach

class ReportPrinter:
    """Odpowiada TYLKO za prezentację raportu"""

    def print_to_console(self, report: Report) -> str:
        """
        Drukuje raport do konsoli

        Zwraca sformatowany string z tytułem i liniami
        Format: "=== {title} ===\n{lines}"
        """
        pass

    def save_to_file(self, report: Report, filename: str) -> None:
        """
        Zapisuje raport do pliku

        Format taki sam jak print_to_console
        """
        pass


# Dlaczego SRP?
# Report: zmienia się gdy zmienia się STRUKTURA danych
# ReportPrinter: zmienia się gdy zmienia się FORMAT prezentacji
# Dwa różne powody do zmiany = dwie klasy
