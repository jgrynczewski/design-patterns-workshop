"""BASIC: Business Logic Violation - tylko istota problemu"""


class Order:
    def calculate_total(self, amount, is_premium):
        # BUSINESS: Premium customers get 20% discount
        discount = amount * 0.20 if is_premium else 0

        # PROBLEM: Business mixed with technical
        import sqlite3  # ← TECHNICAL
        conn = sqlite3.connect('db')  # ← TECHNICAL
        conn.execute("INSERT INTO orders VALUES (?)", (amount,))  # ← TECHNICAL

        return amount - discount  # ← BUSINESS

# PROBLEM: Cannot test business rule without database dependency
