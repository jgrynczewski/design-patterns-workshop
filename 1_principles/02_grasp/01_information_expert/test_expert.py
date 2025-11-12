"""
Testy dla GRASP Information Expert - Student
"""

import pytest
from starter import Student

pytestmark = pytest.mark.grasp_expert


class TestInformationExpert:
    """Testy GRASP Information Expert"""

    def test_student_creation(self):
        student = Student("Alice", [85, 90, 78])
        assert student.get_name() == "Alice"
        assert student.get_grades() == [85, 90, 78]

    def test_calculate_average_basic(self):
        student = Student("Bob", [80, 90, 70])
        assert student.calculate_average() == 80.0

    def test_calculate_average_float_result(self):
        student = Student("Charlie", [85, 90, 78, 92])
        assert student.calculate_average() == 86.25

    def test_calculate_average_single_grade(self):
        student = Student("Dave", [95])
        assert student.calculate_average() == 95.0

    def test_calculate_average_empty_grades(self):
        """Test przypadku brzegowego - brak ocen"""
        student = Student("Eve", [])
        assert student.calculate_average() == 0.0

    def test_information_expert_encapsulation(self):
        """
        Information Expert: Student ma grades,
        więc Student oblicza średnią (nie zewnętrzna klasa)
        """
        student = Student("Frank", [70, 80, 90])

        # Student ma metodę calculate_average
        assert hasattr(student, 'calculate_average')
        assert callable(student.calculate_average)

        # Obliczenie jest wewnątrz Student, nie na zewnątrz
        average = student.calculate_average()
        assert average == 80.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
