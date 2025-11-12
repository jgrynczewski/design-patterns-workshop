"""
GRASP Information Expert - Student Grades

>>> student = Student("Alice", [85, 90, 78, 92])
>>> student.get_name()
'Alice'
>>> student.get_grades()
[85, 90, 78, 92]
>>> student.calculate_average()
86.25

>>> student2 = Student("Bob", [70, 80, 75])
>>> student2.calculate_average()
75.0
"""


# TODO: Zaimplementuj Student
# Hint: __init__ przyjmuje name i grades (lista ocen)
# Hint: calculate_average() oblicza średnią z grades
# Hint: Information Expert - Student ma dane (grades), więc powinien obliczać średnią

class Student:
    """
    Student - INFORMATION EXPERT dla obliczania średniej

    GRASP Information Expert: Student ma dane (grades),
    więc to Student powinien obliczać średnią
    """

    def __init__(self, name: str, grades: list[int]):
        """
        TODO: Zaimplementuj
        - Zapisz name
        - Zapisz grades
        """
        pass

    def get_name(self) -> str:
        """Zwraca imię studenta"""
        pass

    def get_grades(self) -> list[int]:
        """Zwraca oceny"""
        pass

    def calculate_average(self) -> float:
        """
        Oblicza średnią ocen

        Information Expert: Student ma grades, więc on oblicza średnią
        """
        pass


# GRASP Information Expert:
# Przypisz odpowiedzialność klasie, która ma informacje potrzebne do jej realizacji
#
# Dlaczego Student, a nie np. GradeCalculator?
# → Student MA grades, więc jest ekspertem w temacie swoich ocen
