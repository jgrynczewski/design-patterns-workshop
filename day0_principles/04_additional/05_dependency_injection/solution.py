"""
Dependency Injection Solution - Flexible and testable architecture
"""

from abc import ABC, abstractmethod
from datetime import datetime


# INTERFACES - Define contracts for dependencies
class Database(ABC):
    @abstractmethod
    def execute(self, query, params=None): pass

    @abstractmethod
    def close(self): pass


class EmailService(ABC):
    @abstractmethod
    def send_email(self, to_email, subject, body): pass


class Logger(ABC):
    @abstractmethod
    def log_info(self, message): pass

    @abstractmethod
    def log_error(self, message): pass


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount, card_details): pass


# IMPLEMENTATIONS - Can be easily swapped
class SQLiteDatabase(Database):
    def __init__(self, db_path):
        import sqlite3
        self.connection = sqlite3.connect(db_path)

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.connection.close()


class PostgreSQLDatabase(Database):
    def __init__(self, host, database, user, password):
        # In real implementation, would use psycopg2
        self.config = {"host": host, "database": database, "user": user, "password": password}

    def execute(self, query, params=None):
        # PostgreSQL implementation
        return [("mock_result",)]

    def close(self):
        pass


class SMTPEmailService(EmailService):
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        import smtplib
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login(self.username, self.password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(self.username, to_email, message)
        server.quit()
        return True


class FileLogger(Logger):
    def __init__(self, log_file):
        import logging
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)


class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f"INFO: {message}")

    def log_error(self, message):
        print(f"ERROR: {message}")


class PayPalGateway(PaymentGateway):
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def process_payment(self, amount, card_details):
        # PayPal implementation
        return {"transaction_id": f"paypal_{amount}", "status": "success"}


class StripeGateway(PaymentGateway):
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount, card_details):
        # Stripe implementation
        return {"transaction_id": f"stripe_{amount}", "status": "success"}


# SERVICES - Clean business logic with injected dependencies
class NotificationService:
    def __init__(self, email_service: EmailService, logger: Logger):
        self.email_service = email_service  # Injected
        self.logger = logger  # Injected

    def send_notification(self, user_email, message):
        try:
            self.email_service.send_email(user_email, "Notification", message)
            self.logger.log_info(f"Notification sent to {user_email}")
            return True
        except Exception as e:
            self.logger.log_error(f"Failed to send notification: {str(e)}")
            return False


class UserService:
    def __init__(self, database: Database, logger: Logger, notification_service: NotificationService):
        self.database = database  # Injected
        self.logger = logger  # Injected
        self.notification_service = notification_service  # Injected

    def create_user(self, username, email, password):
        try:
            self.logger.log_info(f"Creating user: {username}")

            query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
            self.database.execute(query, (username, email, password))

            self.notification_service.send_notification(
                email,
                f"Welcome {username}! Your account has been created."
            )

            self.logger.log_info(f"User created successfully: {username}")
            return True

        except Exception as e:
            self.logger.log_error(f"Failed to create user: {str(e)}")
            return False


class OrderService:
    def __init__(self,
                 database: Database,
                 payment_gateway: PaymentGateway,
                 logger: Logger,
                 notification_service: NotificationService):
        self.database = database  # Injected
        self.payment_gateway = payment_gateway  # Injected
        self.logger = logger  # Injected
        self.notification_service = notification_service  # Injected

    def process_order(self, user_id, items, payment_details):
        try:
            self.logger.log_info(f"Processing order for user {user_id}")

            total = sum(item['price'] * item['quantity'] for item in items)

            payment_result = self.payment_gateway.process_payment(total, payment_details)

            if payment_result['status'] != 'success':
                self.logger.log_error("Payment failed")
                return False

            order_query = """
                INSERT INTO orders (user_id, total, transaction_id, created_at) 
                VALUES (?, ?, ?, ?)
            """
            self.database.execute(order_query, (
                user_id, total, payment_result['transaction_id'], datetime.now()
            ))

            user_query = "SELECT email FROM users WHERE id = ?"
            user_result = self.database.execute(user_query, (user_id,))

            if user_result:
                user_email = user_result[0][0]
                self.notification_service.send_notification(
                    user_email,
                    f"Order confirmed! Total: ${total}"
                )

            self.logger.log_info("Order processed successfully")
            return True

        except Exception as e:
            self.logger.log_error(f"Order processing failed: {str(e)}")
            return False


# DEPENDENCY INJECTION CONTAINER / FACTORY
class ServiceContainer:
    def __init__(self, config):
        self.config = config
        self._services = {}

    def get_database(self) -> Database:
        if 'database' not in self._services:
            if self.config['database']['type'] == 'sqlite':
                self._services['database'] = SQLiteDatabase(self.config['database']['path'])
            elif self.config['database']['type'] == 'postgresql':
                self._services['database'] = PostgreSQLDatabase(
                    self.config['database']['host'],
                    self.config['database']['name'],
                    self.config['database']['user'],
                    self.config['database']['password']
                )
        return self._services['database']

    def get_logger(self) -> Logger:
        if 'logger' not in self._services:
            if self.config['logger']['type'] == 'file':
                self._services['logger'] = FileLogger(self.config['logger']['path'])
            elif self.config['logger']['type'] == 'console':
                self._services['logger'] = ConsoleLogger()
        return self._services['logger']

    def get_email_service(self) -> EmailService:
        if 'email' not in self._services:
            email_config = self.config['email']
            self._services['email'] = SMTPEmailService(
                email_config['smtp_server'],
                email_config['port'],
                email_config['username'],
                email_config['password']
            )
        return self._services['email']

    def get_payment_gateway(self) -> PaymentGateway:
        if 'payment' not in self._services:
            if self.config['payment']['provider'] == 'paypal':
                self._services['payment'] = PayPalGateway(
                    self.config['payment']['api_key'],
                    self.config['payment']['endpoint']
                )
            elif self.config['payment']['provider'] == 'stripe':
                self._services['payment'] = StripeGateway(
                    self.config['payment']['api_key']
                )
        return self._services['payment']

    def get_notification_service(self) -> NotificationService:
        if 'notification' not in self._services:
            self._services['notification'] = NotificationService(
                self.get_email_service(),
                self.get_logger()
            )
        return self._services['notification']

    def get_user_service(self) -> UserService:
        if 'user_service' not in self._services:
            self._services['user_service'] = UserService(
                self.get_database(),
                self.get_logger(),
                self.get_notification_service()
            )
        return self._services['user_service']

    def get_order_service(self) -> OrderService:
        if 'order_service' not in self._services:
            self._services['order_service'] = OrderService(
                self.get_database(),
                self.get_payment_gateway(),
                self.get_logger(),
                self.get_notification_service()
            )
        return self._services['order_service']


# USAGE EXAMPLES

# Production configuration
production_config = {
    'database': {'type': 'postgresql', 'host': 'prod-db.com', 'name': 'prod_db', 'user': 'prod_user',
                 'password': 'prod_pass'},
    'logger': {'type': 'file', 'path': 'production.log'},
    'email': {'smtp_server': 'smtp.company.com', 'port': 587, 'username': 'service@company.com',
              'password': 'prod_pass'},
    'payment': {'provider': 'stripe', 'api_key': 'sk_live_...'}
}

# Test configuration
test_config = {
    'database': {'type': 'sqlite', 'path': ':memory:'},
    'logger': {'type': 'console'},
    'email': {'smtp_server': 'localhost', 'port': 1025, 'username': 'test', 'password': 'test'},
    'payment': {'provider': 'paypal', 'api_key': 'test_key', 'endpoint': 'https://api.sandbox.paypal.com'}
}

# Easy to switch between environments
container = ServiceContainer(production_config)  # or test_config
order_service = container.get_order_service()

# BENEFITS:
# 1. Easy unit testing with mocks
# 2. Flexible configuration for different environments
# 3. Loose coupling between components
# 4. Single Responsibility Principle maintained
# 5. Easy to swap implementations
# 6. Centralized dependency management
# 7. Clear interfaces and contracts
# 8. Testable in isolation
