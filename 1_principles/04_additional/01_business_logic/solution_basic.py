"""BASIC: Business Logic Solution - clean separation"""


# BUSINESS LAYER - pure rules
class Order:
    def calculate_discount(self, amount, is_premium):
        return amount * 0.20 if is_premium else 0  # BUSINESS RULE


# TECHNICAL LAYER - infrastructure
class Database:
    def save_order(self, amount):
        import sqlite3
        conn = sqlite3.connect('db')
        conn.execute("INSERT INTO orders VALUES (?)", (amount,))
        conn.close()

# RESULT: Business rules testable without technical dependencies
