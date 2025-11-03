"""
DRY Violation - Don't Repeat Yourself
Duplikacja kodu w różnych miejscach
"""


class UserValidator:
    def validate_email(self, email):
        # PROBLEM: Duplikacja logiki walidacji
        if "@" not in email or "." not in email:
            return False
        if len(email) < 5:
            return False
        return True

    def validate_admin_email(self, email):
        # PROBLEM: Ta sama logika co wyżej - duplikacja!
        if "@" not in email or "." not in email:
            return False
        if len(email) < 5:
            return False
        # Plus dodatkowa logika
        if not email.endswith("@company.com"):
            return False
        return True


class OrderProcessor:
    def calculate_discount_for_regular(self, amount):
        # PROBLEM: Identyczna logika obliczania
        tax = amount * 0.23
        service_fee = amount * 0.05
        total_fees = tax + service_fee
        return amount - (amount * 0.10) + total_fees

    def calculate_discount_for_premium(self, amount):
        # PROBLEM: Kopia powyższej metody z innym procentem
        tax = amount * 0.23
        service_fee = amount * 0.05
        total_fees = tax + service_fee
        return amount - (amount * 0.15) + total_fees  # Tylko ta linijka się różni

    def calculate_discount_for_vip(self, amount):
        # PROBLEM: Znowu ta sama logika
        tax = amount * 0.23
        service_fee = amount * 0.05
        total_fees = tax + service_fee
        return amount - (amount * 0.20) + total_fees


class DatabaseLogger:
    def log_user_action(self, user_id, action):
        timestamp = "2024-01-15 10:30:00"  # PROBLEM: Duplikacja formatowania
        message = f"[{timestamp}] User {user_id}: {action}"
        print(f"INSERT INTO logs VALUES('{message}')")

    def log_system_event(self, event):
        timestamp = "2024-01-15 10:30:00"  # PROBLEM: Ta sama logika timestampu
        message = f"[{timestamp}] System: {event}"
        print(f"INSERT INTO logs VALUES('{message}')")

    def log_error(self, error):
        timestamp = "2024-01-15 10:30:00"  # PROBLEM: Znowu duplikacja
        message = f"[{timestamp}] ERROR: {error}"
        print(f"INSERT INTO logs VALUES('{message}')")


if __name__ == "__main__":
    validator = UserValidator()
    print(validator.validate_email("test@example.com"))
    print(validator.validate_admin_email("admin@company.com"))

    processor = OrderProcessor()
    print(f"Regular: ${processor.calculate_discount_for_regular(100)}")
    print(f"Premium: ${processor.calculate_discount_for_premium(100)}")

    logger = DatabaseLogger()
    logger.log_user_action(123, "login")
    logger.log_system_event("startup")

    print("❌ Duplikacja kodu w wielu miejscach - naruszenie DRY")
    print("❌ Zmiana walidacji email = 2 miejsca do edycji")
    print("❌ Zmiana formatu timestamp = 3 miejsca do edycji")
