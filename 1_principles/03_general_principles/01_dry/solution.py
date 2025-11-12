"""
DRY Solution - Don't Repeat Yourself
Eliminacja duplikacji poprzez wydzielenie wspólnej logiki
"""

from datetime import datetime


class UserValidator:
    def _is_valid_email_format(self, email):
        # DRY: Jedna implementacja podstawowej walidacji
        return "@" in email and "." in email and len(email) >= 5

    def validate_email(self, email):
        return self._is_valid_email_format(email)

    def validate_admin_email(self, email):
        # Reużywa podstawowej walidacji + dodaje specyficzną logikę
        return (self._is_valid_email_format(email) and
                email.endswith("@company.com"))


class OrderProcessor:
    TAX_RATE = 0.23
    SERVICE_FEE_RATE = 0.05

    def _calculate_base_fees(self, amount):
        # DRY: Wspólna logika obliczania opłat
        tax = amount * self.TAX_RATE
        service_fee = amount * self.SERVICE_FEE_RATE
        return tax + service_fee

    def _apply_discount(self, amount, discount_rate):
        # DRY: Wspólna logika aplicacji zniżki
        base_fees = self._calculate_base_fees(amount)
        discount = amount * discount_rate
        return amount - discount + base_fees

    def calculate_discount_for_regular(self, amount):
        return self._apply_discount(amount, 0.10)

    def calculate_discount_for_premium(self, amount):
        return self._apply_discount(amount, 0.15)

    def calculate_discount_for_vip(self, amount):
        return self._apply_discount(amount, 0.20)


class DatabaseLogger:
    def _get_timestamp(self):
        # DRY: Jedna implementacja timestampu
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _log_message(self, message):
        # DRY: Wspólna logika logowania
        timestamp = self._get_timestamp()
        formatted_message = f"[{timestamp}] {message}"
        print(f"INSERT INTO logs VALUES('{formatted_message}')")

    def log_user_action(self, user_id, action):
        self._log_message(f"User {user_id}: {action}")

    def log_system_event(self, event):
        self._log_message(f"System: {event}")

    def log_error(self, error):
        self._log_message(f"ERROR: {error}")


# Bonus: Configuration-driven approach dla jeszcze lepszego DRY
class AdvancedOrderProcessor:
    """Przykład data-driven approach dla eliminacji duplikacji"""

    DISCOUNT_RATES = {
        'regular': 0.10,
        'premium': 0.15,
        'vip': 0.20
    }

    TAX_RATE = 0.23
    SERVICE_FEE_RATE = 0.05

    def calculate_discount(self, amount, customer_type):
        # DRY: Jedna metoda dla wszystkich typów klientów
        if customer_type not in self.DISCOUNT_RATES:
            raise ValueError(f"Unknown customer type: {customer_type}")

        discount_rate = self.DISCOUNT_RATES[customer_type]
        base_fees = amount * (self.TAX_RATE + self.SERVICE_FEE_RATE)
        discount = amount * discount_rate

        return amount - discount + base_fees


if __name__ == "__main__":
    validator = UserValidator()
    print(validator.validate_email("test@example.com"))
    print(validator.validate_admin_email("admin@company.com"))

    processor = OrderProcessor()
    print(f"Regular: ${processor.calculate_discount_for_regular(100):.2f}")
    print(f"Premium: ${processor.calculate_discount_for_premium(100):.2f}")

    # Bonus: Data-driven approach
    advanced = AdvancedOrderProcessor()
    print(f"VIP (advanced): ${advanced.calculate_discount(100, 'vip'):.2f}")

    logger = DatabaseLogger()
    logger.log_user_action(123, "login")
    logger.log_system_event("startup")
    logger.log_error("Database connection failed")

    print("✅ Jedna implementacja dla każdej logiki")
    print("✅ Zmiana walidacji = 1 miejsce do edycji")
    print("✅ Zmiana timestamp = 1 miejsce do edycji")
    print("✅ Nowe typy klientów = dodanie do dictionary")
