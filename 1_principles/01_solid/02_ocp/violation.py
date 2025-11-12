"""
Open/Closed Principle VIOLATION
Klasa wymagająca modyfikacji przy dodaniu nowych typów
"""


class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.95
        elif customer_type == "premium":
            return amount * 0.90
        elif customer_type == "vip":
            return amount * 0.85
        else:
            return amount

# PROBLEM: Jak dodać "student" discount?
# Muszę modyfikować metodę calculate() - łamie OCP

# Każdy nowy typ klienta = zmiana w istniejącym kodzie
if __name__ == "__main__":
    calc = DiscountCalculator()

    print(calc.calculate("regular", 100))  # 95.0
    print(calc.calculate("premium", 100))  # 90.0

    # Żeby dodać "student" - muszę zmienić klasę DiscountCalculator!
    print(calc.calculate("student", 100))  # wymaga wprowadzenia zmian w istniejącej
    # metodzie calculate klasy DiscountCalculator

