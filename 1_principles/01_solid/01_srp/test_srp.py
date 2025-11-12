"""
Testy dla SRP - Report System
"""

import pytest
import os
from starter import Report, ReportPrinter

pytestmark = pytest.mark.solid_srp


class TestSRP:
    """Testy Single Responsibility Principle"""

    def test_report_stores_data(self):
        """Test czy Report przechowuje dane"""
        report = Report("Test Report", ["Line 1", "Line 2"])

        assert report.get_title() == "Test Report"
        assert report.get_lines() == ["Line 1", "Line 2"]
        assert len(report.get_lines()) == 2

    def test_printer_console_output(self):
        """Test drukowania do konsoli"""
        report = Report("Sales", ["Revenue: $100k"])
        printer = ReportPrinter()

        output = printer.print_to_console(report)

        assert isinstance(output, str)
        assert "Sales" in output
        assert "Revenue: $100k" in output
        assert "===" in output

    def test_printer_file_save(self):
        """Test zapisu do pliku"""
        report = Report("Test", ["Data 1", "Data 2"])
        printer = ReportPrinter()
        filename = "test_output.txt"

        try:
            printer.save_to_file(report, filename)

            assert os.path.exists(filename)

            with open(filename, 'r') as f:
                content = f.read()

            assert "Test" in content
            assert "Data 1" in content
            assert "Data 2" in content

        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_report_immutable_after_creation(self):
        """Test czy dane raportu są odczytywalne"""
        lines = ["A", "B", "C"]
        report = Report("Title", lines)

        # Report przechowuje dane, nie modyfikuje
        assert report.get_lines() == lines

    def test_multiple_reports_with_same_printer(self):
        """Test czy ten sam printer może obsłużyć wiele raportów"""
        printer = ReportPrinter()

        report1 = Report("Report 1", ["Data A"])
        report2 = Report("Report 2", ["Data B"])

        output1 = printer.print_to_console(report1)
        output2 = printer.print_to_console(report2)

        assert "Report 1" in output1
        assert "Report 2" in output2
        assert "Data A" in output1
        assert "Data B" in output2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
