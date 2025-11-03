"""
Business Logic Violation - Mieszanie business logic z technical logic
"""


class Order:
    """PROBLEM: Business logic zmieszana z technical details"""

    def __init__(self, amount, customer_type):
        self.amount = amount
        self.customer_type = customer_type

    def calculate_total(self):
        # BUSINESS LOGIC: Premium customers get 20% discount
        if self.customer_type == "premium":
            discount = self.amount * 0.20
        else:
            discount = 0

        # PROBLEM: Business logic mixed with technical implementation
        import sqlite3
        import hashlib
        import json

        # TECHNICAL LOGIC: Database operations
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()

        total = self.amount - discount

        # TECHNICAL LOGIC: Data serialization
        order_data = json.dumps({
            'amount': self.amount,
            'discount': discount,
            'total': total
        })

        # TECHNICAL LOGIC: Hashing
        order_hash = hashlib.md5(order_data.encode()).hexdigest()

        # TECHNICAL LOGIC: Database save
        cursor.execute("""
            INSERT INTO orders (data, hash, total) VALUES (?, ?, ?)
        """, (order_data, order_hash, total))

        conn.commit()
        conn.close()

        # BUSINESS LOGIC: Return calculated total
        return total


class User:
    """PROBLEM: Cannot test business rules without database"""

    def __init__(self, age, email):
        self.age = age
        self.email = email

    def can_buy_alcohol(self):
        # BUSINESS RULE: Must be 18+ to buy alcohol
        age_check = self.age >= 18

        # PROBLEM: Business rule mixed with technical validation
        import re
        email_valid = re.match(r'^[^@]+@[^@]+\.[^@]+$', self.email)

        # PROBLEM: Business rule mixed with database check
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT banned FROM users WHERE email = ?", (self.email,))
        result = cursor.fetchone()
        is_banned = result and result[0] == 1
        conn.close()

        return age_check and email_valid and not is_banned

# PROBLEM: Impossible to test business rules in isolation
# - Cannot test discount calculation without database
# - Cannot test age validation without email regex
# - Business rules buried in technical implementation
