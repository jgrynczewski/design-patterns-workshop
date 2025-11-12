"""
Business Logic Solution - Clean separation of concerns
"""


# ============================================================================
# DOMAIN LAYER - Pure Business Logic
# ============================================================================

class Order:
    """CLEAN: Only business logic, no technical details"""

    def __init__(self, amount: float, customer_type: str):
        self.amount = amount
        self.customer_type = customer_type

    def calculate_discount(self) -> float:
        """BUSINESS RULE: Premium customers get 20% discount"""
        if self.customer_type == "premium":
            return self.amount * 0.20
        return 0.0

    def calculate_total(self) -> float:
        """BUSINESS LOGIC: Total = amount - discount"""
        return self.amount - self.calculate_discount()


class User:
    """CLEAN: Only business logic"""

    def __init__(self, age: int):
        self.age = age

    def can_buy_alcohol(self) -> bool:
        """BUSINESS RULE: Must be 18+ to buy alcohol"""
        return self.age >= 18


# ============================================================================
# INFRASTRUCTURE LAYER - Technical Details
# ============================================================================

class OrderRepository:
    """TECHNICAL: Database operations"""

    def save(self, order: Order) -> None:
        import sqlite3
        import hashlib
        import json

        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()

        # Technical: serialization
        order_data = json.dumps({
            'amount': order.amount,
            'customer_type': order.customer_type,
            'total': order.calculate_total()
        })

        # Technical: hashing
        order_hash = hashlib.md5(order_data.encode()).hexdigest()

        # Technical: database
        cursor.execute("""
            INSERT INTO orders (data, hash, total) VALUES (?, ?, ?)
        """, (order_data, order_hash, order.calculate_total()))

        conn.commit()
        conn.close()


class UserRepository:
    """TECHNICAL: User persistence"""

    def is_banned(self, email: str) -> bool:
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT banned FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        conn.close()
        return result and result[0] == 1


class EmailValidator:
    """TECHNICAL: Email format validation"""

    @staticmethod
    def is_valid(email: str) -> bool:
        import re
        return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))


# ============================================================================
# APPLICATION LAYER - Coordination
# ============================================================================

class OrderService:
    """CLEAN: Coordinates business logic with infrastructure"""

    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def process_order(self, amount: float, customer_type: str) -> float:
        # Business logic
        order = Order(amount, customer_type)
        total = order.calculate_total()

        # Infrastructure
        self.order_repo.save(order)

        return total


class UserService:
    """CLEAN: Business logic + technical validation"""

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def can_user_buy_alcohol(self, age: int, email: str) -> bool:
        # Business logic
        user = User(age)
        business_rule_ok = user.can_buy_alcohol()

        # Technical validation
        email_valid = EmailValidator.is_valid(email)
        not_banned = not self.user_repo.is_banned(email)

        return business_rule_ok and email_valid and not_banned

# RESULT:
# - Business rules are testable in isolation
# - Technical details separated
# - Domain expert can validate business logic
# - Easy to change database/email validation without touching business rules
