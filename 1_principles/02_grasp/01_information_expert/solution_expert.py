"""
GRASP Information Expert - Student Grades - SOLUTION

>>> student = Student("Alice", [85, 90, 78, 92])
>>> student.calculate_average()
86.25
"""


class Student:
    """Student - INFORMATION EXPERT dla obliczania średniej"""

    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def get_name(self) -> str:
        return self.name

    def get_grades(self) -> list[int]:
        return self.grades

    def calculate_average(self) -> float:
        """Information Expert: Student ma grades, więc on oblicza"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    print("=== GRASP Information Expert ===\n")

    student1 = Student("Alice", [85, 90, 78, 92])
    print(f"{student1.get_name()}: {student1.calculate_average():.2f}")

    student2 = Student("Bob", [70, 80, 75, 85, 90])
    print(f"{student2.get_name()}: {student2.calculate_average():.2f}")

    print("\nInformation Expert: Student ma grades → Student oblicza średnią")
