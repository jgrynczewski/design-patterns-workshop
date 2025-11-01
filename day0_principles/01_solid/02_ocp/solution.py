"""
Open/Closed Principle SOLUTION
Klasa otwarta na rozszerzenie, zamknięta na modyfikacje
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.95


class PremiumDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.90


class VIPDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.85

class DiscountCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, amount):
        return self.strategy.calculate(amount)

# ROZWIĄZANIE: Nowe typy = nowe klasy (rozszerzenie)
# DiscountCalculator nie zmienia się (zamknięty na modyfikacje)

# Dodajemy nowy typ — bez modyfikacji istniejącego kodu — (otwarty na rozszerzenie)
class StudentDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.80


if __name__ == "__main__":
    regular_calc = DiscountCalculator(RegularDiscount())
    premium_calc = DiscountCalculator(PremiumDiscount())
    student_calc = DiscountCalculator(StudentDiscount())  # Nowy typ! Zmian

    print(regular_calc.calculate(100))  # 95.0
    print(premium_calc.calculate(100))  # 90.0
    print(student_calc.calculate(100))  # 80.0 - dodane bez zmian w kodzie!
