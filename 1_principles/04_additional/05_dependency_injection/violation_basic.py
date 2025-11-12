"""BASIC: Dependency Injection Violation - tylko istota problemu"""


class OrderService:
    def __init__(self):
        # PROBLEM: Hard dependencies created inside
        self.database = PostgreSQLDatabase()  # ← Hard dependency
        self.logger = FileLogger()  # ← Hard dependency
        self.email = SMTPEmailer()  # ← Hard dependency

    def create_order(self, order_data):
        # Cannot test without real database/email/file system
        self.logger.log("Creating order")
        order_id = self.database.save(order_data)
        self.email.send_confirmation(order_data['email'])
        return order_id


class PostgreSQLDatabase:
    def save(self, data):
        return "Saving to PostgreSQL..."


class FileLogger:
    def log(self, message):
        return "Writing to file..."


class SMTPEmailer:
    def send_confirmation(self, email):
        return "Sending SMTP email..."


# PROBLEM: Cannot test OrderService without real PostgreSQL, files, and SMTP
# Kluczowy problem: OrderService tworzy swoje zależności wewnątrz, więc nie można ich zamockować
# do testów ani zmienić implementacji.
