"""
Static Example - Decisions made before program runs
"""


# STATIC: Class structure defined at code time
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):  # STATIC: method always exists
        return self.name

    def is_admin(self):  # STATIC: method signature known
        return False


class AdminUser(User):
    def is_admin(self):  # STATIC: override known at definition
        return True


# STATIC: Function signature defined
def process_user(user: User) -> str:  # STATIC: types declared
    """STATIC: docstring and behavior known"""
    return f"Processing {user.get_name()}"  # STATIC: method call structure


# STATIC: Import decisions made at code time
import json  # STATIC: module imported before runtime
from datetime import datetime  # STATIC: specific imports


# STATIC: Class hierarchy and inheritance
class Shape:
    def area(self):
        raise NotImplementedError  # STATIC: method contract


class Circle(Shape):  # STATIC: inheritance relationship
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # STATIC: method implementation
        return 3.14 * self.radius ** 2


# STATIC: Constants and configuration
MAX_USERS = 100  # STATIC: value known
CONFIG_FILE = "app.json"  # STATIC: filename known
DEFAULT_ROLE = "user"  # STATIC: default value


# STATIC: Function definitions and structure
def calculate_discount(amount: float, user_type: str) -> float:
    """STATIC: All logic branches defined at code time"""
    if user_type == "premium":  # STATIC: condition logic
        return amount * 0.20  # STATIC: calculation formula
    elif user_type == "regular":  # STATIC: condition logic
        return amount * 0.10  # STATIC: calculation formula
    else:
        return 0.0  # STATIC: default case


# STATIC: Class factory with known types
class UserFactory:
    @staticmethod
    def create_user(user_type: str, name: str):
        """STATIC: All possible return types known"""
        if user_type == "admin":
            return AdminUser(name)  # STATIC: AdminUser construction
        else:
            return User(name)  # STATIC: User construction


# STATIC: Module-level code execution order
print("Module loading...")  # STATIC: always executes when imported


# STATIC: Decorator definitions
def log_calls(func):
    """STATIC: decorator structure defined"""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")  # STATIC: logging format
        return func(*args, **kwargs)

    return wrapper


@log_calls  # STATIC: decoration applied at definition
def greet(name: str) -> str:
    return f"Hello, {name}!"

# STATIC: All these decisions are made at code-writing time:
# - Class definitions and methods
# - Function signatures and type hints
# - Import statements
# - Inheritance relationships
# - Constants and default values
# - Code structure and flow
