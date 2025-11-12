# 🎓 GRASP Information Expert - Student

**Difficulty**: easy
**Time**: 5 minutes
**Focus**: GRASP Information Expert

## 🎯 Zadanie
Zaimplementuj `Student` - oblicza średnią swoich ocen (Information Expert).

## 📋 Wymagania
- [ ] `Student.__init__(name, grades)` - przechowuje dane
- [ ] `calculate_average()` - zwraca średnią z grades
- [ ] Obsługa pustej listy (zwróć 0.0)

## 🚀 Jak zacząć
```bash
cd day0_principles/02_grasp/01_information_expert
pytest test_expert.py -v
```

## 💡 GRASP Information Expert w pigułce

**Przypisz odpowiedzialność klasie, która ma potrzebne informacje**

❌ **Źle** (obcy kalkuluje średnią):
```python
class Student:
    def __init__(self, grades):
        self.grades = grades

class GradeCalculator:  # Zewnętrzna klasa ❌
    def calculate_average(self, student):
        return sum(student.grades) / len(student.grades)

# Klient musi użyć 2 klas
calc = GradeCalculator()
avg = calc.calculate_average(student)
```

✅ **Dobrze** (Student sam oblicza):
```python
class Student:
    def __init__(self, grades):
        self.grades = grades

    def calculate_average(self):  # Expert - ma dane ✅
        return sum(self.grades) / len(self.grades)

# Klient używa tylko Student
avg = student.calculate_average()
```

**Korzyść**: Student ma grades → Student jest ekspertem → Student oblicza.

Sprawdź `solution_expert.py` po wykonaniu.
