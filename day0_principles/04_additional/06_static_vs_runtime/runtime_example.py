"""
Runtime Example - Decisions made during program execution
"""

import json
import os
from datetime import datetime


# RUNTIME: Object creation depends on user input
def create_user_based_on_input():
    """RUNTIME: User type determined during execution"""
    user_input = input("Enter user type (admin/regular): ")  # RUNTIME: user decides

    if user_input == "admin":  # RUNTIME: condition evaluated
        return AdminUser("Admin")  # RUNTIME: object type chosen
    else:
        return RegularUser("User")  # RUNTIME: different object type


# RUNTIME: Method calls depend on object type (polymorphism)
def process_users(users):
    """RUNTIME: Which method gets called depends on actual object type"""
    for user in users:
        # RUNTIME: Actual method called depends on user's real type
        print(user.get_permissions())  # Could be AdminUser.get_permissions() or RegularUser.get_permissions()


class RegularUser:
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        return "read"  # RUNTIME: this specific implementation called


class AdminUser:
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        return "read, write, delete"  # RUNTIME: this specific implementation called


# RUNTIME: Configuration loaded during execution
def load_config():
    """RUNTIME: Configuration depends on what's actually on disk"""
    try:
        with open("config.json", "r") as f:  # RUNTIME: file may or may not exist
            return json.load(f)  # RUNTIME: content unknown until read
    except FileNotFoundError:  # RUNTIME: exception handling
        return {"default": True}  # RUNTIME: fallback executed


# RUNTIME: Database queries and external API calls
def get_user_from_database(user_id):
    """RUNTIME: Result depends on current database state"""
    # Simulating database call
    if user_id == 1:  # RUNTIME: data lookup
        return {"name": "John", "active": True}
    elif user_id == 2:  # RUNTIME: different data
        return {"name": "Jane", "active": False}
    else:
        return None  # RUNTIME: not found


# RUNTIME: Strategy pattern - behavior chosen at runtime
class PaymentProcessor:
    def __init__(self):
        self.strategies = {
            "credit_card": CreditCardStrategy(),
            "paypal": PayPalStrategy(),
            "bank_transfer": BankTransferStrategy()
        }

    def process_payment(self, amount, method):
        """RUNTIME: Payment method chosen during execution"""
        strategy = self.strategies.get(method)  # RUNTIME: strategy selection
        if strategy:
            return strategy.process(amount)  # RUNTIME: specific method called
        else:
            raise ValueError("Unknown payment method")  # RUNTIME: error


class CreditCardStrategy:
    def process(self, amount):
        return f"Processing ${amount} via credit card"


class PayPalStrategy:
    def process(self, amount):
        return f"Processing ${amount} via PayPal"


class BankTransferStrategy:
    def process(self, amount):
        return f"Processing ${amount} via bank transfer"


# RUNTIME: Conditional execution based on environment
def setup_logging():
    """RUNTIME: Logging setup depends on current environment"""
    environment = os.getenv("ENV", "development")  # RUNTIME: environment variable

    if environment == "production":  # RUNTIME: condition
        setup_production_logging()  # RUNTIME: specific setup
    elif environment == "testing":  # RUNTIME: different condition
        setup_test_logging()  # RUNTIME: different setup
    else:
        setup_development_logging()  # RUNTIME: default setup


# RUNTIME: Time-dependent behavior
def get_greeting():
    """RUNTIME: Greeting depends on current time"""
    current_hour = datetime.now().hour  # RUNTIME: current time

    if current_hour < 12:  # RUNTIME: time-based condition
        return "Good morning!"
    elif current_hour < 18:  # RUNTIME: different condition
        return "Good afternoon!"
    else:
        return "Good evening!"  # RUNTIME: time-dependent result


# RUNTIME: User interaction and event handling
def handle_user_actions():
    """RUNTIME: Actions depend on user choices"""
    while True:
        action = input("Choose action (save/load/quit): ")  # RUNTIME: user input

        if action == "save":  # RUNTIME: user decision
            filename = input("Enter filename: ")  # RUNTIME: user data
            save_data(filename)  # RUNTIME: specific action
        elif action == "load":  # RUNTIME: different choice
            filename = input("Enter filename: ")  # RUNTIME: user data
            load_data(filename)  # RUNTIME: different action
        elif action == "quit":  # RUNTIME: exit condition
            break  # RUNTIME: loop termination
        else:
            print("Unknown action")  # RUNTIME: error feedback


# RUNTIME: Dynamic imports and module loading
def load_plugin(plugin_name):
    """RUNTIME: Module imported based on runtime parameter"""
    try:
        module = __import__(f"plugins.{plugin_name}")  # RUNTIME: dynamic import
        return module.get_plugin()  # RUNTIME: plugin loaded
    except ImportError:
        return None  # RUNTIME: plugin not found

# RUNTIME: All these decisions happen during program execution:
# - User input and choices
# - File system state and external data
# - Current time and environment variables
# - Database query results
# - Network responses and API calls
# - Exception handling and error conditions
# - Polymorphic method dispatch
# - Strategy and state pattern decisions
