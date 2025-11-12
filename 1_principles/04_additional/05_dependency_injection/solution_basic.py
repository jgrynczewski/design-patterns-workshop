"""BASIC: Dependency Injection Solution - clean approach"""


class OrderService:
    def __init__(self, database, logger, emailer):
        # CLEAN: Dependencies injected from outside
        self.database = database  # ← Injected
        self.logger = logger  # ← Injected
        self.emailer = emailer  # ← Injected

    def create_order(self, order_data):
        # Same business logic, but testable!
        self.logger.log("Creating order")
        order_id = self.database.save(order_data)
        self.emailer.send_confirmation(order_data['email'])
        return order_id


# IMPLEMENTATIONS - can be swapped easily
class PostgreSQLDatabase:
    def save(self, data):
        return "Saving to PostgreSQL..."


class FileLogger:
    def log(self, message):
        return "Writing to file..."


class SMTPEmailer:
    def send_confirmation(self, email):
        return "Sending SMTP email..."


# PRODUCTION USAGE
service = OrderService(
    PostgreSQLDatabase(),
    FileLogger(),
    SMTPEmailer()
)


# TESTING USAGE - easy mocking!
class MockDatabase:
    def save(self, data): return "mock_id"


test_service = OrderService(MockDatabase(), MockLogger(), MockEmailer())

# RESULT: Flexible, testable, configurable
# Kluczowa korzyść: Zależności przekazywane z zewnątrz, więc łatwe testowanie z mockami i zmiana implementacji.
