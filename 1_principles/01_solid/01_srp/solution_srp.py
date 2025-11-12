"""
Single Responsibility Principle - Report System - SOLUTION

>>> report = Report("Sales Q4", ["Revenue: $100k", "Growth: 15%"])
>>> report.get_title()
'Sales Q4'
>>> len(report.get_lines())
2

>>> printer = ReportPrinter()
>>> output = printer.print_to_console(report)
>>> "Sales Q4" in output
True
>>> "Revenue: $100k" in output
True

>>> import os
>>> printer.save_to_file(report, "test_report.txt")
>>> os.path.exists("test_report.txt")
True
>>> os.remove("test_report.txt")
"""


class Report:
    """Odpowiada TYLKO za przechowywanie danych raportu"""

    def __init__(self, title: str, lines: list[str]):
        self.title = title
        self.lines = lines

    def get_title(self) -> str:
        return self.title

    def get_lines(self) -> list[str]:
        return self.lines


class ReportPrinter:
    """Odpowiada TYLKO za prezentację raportu"""

    def print_to_console(self, report: Report) -> str:
        """Drukuje raport do konsoli"""
        output = f"=== {report.get_title()} ===\n"
        for line in report.get_lines():
            output += f"{line}\n"
        print(output)
        return output

    def save_to_file(self, report: Report, filename: str) -> None:
        """Zapisuje raport do pliku"""
        content = f"=== {report.get_title()} ===\n"
        for line in report.get_lines():
            content += f"{line}\n"

        with open(filename, 'w') as f:
            f.write(content)


if __name__ == "__main__":
    # Demo
    report = Report("Q4 Sales Report", [
        "Revenue: $100,000",
        "Growth: 15%",
        "New customers: 250"
    ])

    printer = ReportPrinter()
    printer.print_to_console(report)
    printer.save_to_file(report, "sales_report.txt")
    print("\nReport saved to sales_report.txt")
