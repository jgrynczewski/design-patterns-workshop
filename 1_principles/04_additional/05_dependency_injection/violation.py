"""
Dependency Injection Violation - Hard dependencies everywhere
"""

import sqlite3
import smtplib
import logging
from datetime import datetime


class DatabaseConnection:
    def __init__(self):
        # Hard-coded database configuration
        self.connection = sqlite3.connect('production.db')

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.connection.close()


class EmailService:
    def __init__(self):
        # Hard-coded SMTP configuration
        self.smtp_server = "smtp.production.com"
        self.port = 587
        self.username = "service@company.com"
        self.password = "production_password"

    def send_email(self, to_email, subject, body):
        # Real SMTP connection
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login(self.username, self.password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(self.username, to_email, message)
        server.quit()
        return True


class LoggingService:
    def __init__(self):
        # Hard-coded logging configuration
        logging.basicConfig(
            filename='production.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)


class PaymentGateway:
    def __init__(self):
        # Hard-coded payment gateway
        self.api_key = "production_api_key"
        self.endpoint = "https://api.paypal.com/v1/payments"

    def process_payment(self, amount, card_details):
        # Real payment processing
        # In reality, this would make HTTP requests
        return {"transaction_id": "real_transaction_123", "status": "success"}


class NotificationService:
    def __init__(self):
        # PROBLEM: Creates its own dependencies
        self.email_service = EmailService()  # Hard dependency
        self.logging_service = LoggingService()  # Hard dependency

    def send_notification(self, user_email, message):
        try:
            self.email_service.send_email(user_email, "Notification", message)
            self.logging_service.log_info(f"Notification sent to {user_email}")
            return True
        except Exception as e:
            self.logging_service.log_error(f"Failed to send notification: {str(e)}")
            return False


class UserService:
    def __init__(self):
        # PROBLEM: Hard dependencies created internally
        self.database = DatabaseConnection()  # Hard dependency
        self.logging_service = LoggingService()  # Hard dependency
        self.notification_service = NotificationService()  # Hard dependency

    def create_user(self, username, email, password):
        try:
            # Business logic mixed with infrastructure concerns
            self.logging_service.log_info(f"Creating user: {username}")

            # Database operation with hard dependency
            query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
            self.database.execute(query, (username, email, password))

            # Notification with hard dependency
            self.notification_service.send_notification(
                email,
                f"Welcome {username}! Your account has been created."
            )

            self.logging_service.log_info(f"User created successfully: {username}")
            return True

        except Exception as e:
            self.logging_service.log_error(f"Failed to create user: {str(e)}")
            return False

    def __del__(self):
        # Cleanup - but what if database connection fails?
        try:
            self.database.close()
        except:
            pass


class OrderService:
    def __init__(self):
        # PROBLEM: Multiple hard dependencies
        self.database = DatabaseConnection()  # Hard dependency
        self.payment_gateway = PaymentGateway()  # Hard dependency
        self.logging_service = LoggingService()  # Hard dependency
        self.user_service = UserService()  # Hard dependency (which has its own hard deps)
        self.notification_service = NotificationService()  # Hard dependency

    def process_order(self, user_id, items, payment_details):
        try:
            self.logging_service.log_info(f"Processing order for user {user_id}")

            # Calculate total
            total = sum(item['price'] * item['quantity'] for item in items)

            # Process payment
            payment_result = self.payment_gateway.process_payment(total, payment_details)

            if payment_result['status'] != 'success':
                self.logging_service.log_error("Payment failed")
                return False

            # Save order to database
            order_query = """
                INSERT INTO orders (user_id, total, transaction_id, created_at) 
                VALUES (?, ?, ?, ?)
            """
            self.database.execute(order_query, (
                user_id, total, payment_result['transaction_id'], datetime.now()
            ))

            # Get user email for notification
            user_query = "SELECT email FROM users WHERE id = ?"
            user_result = self.database.execute(user_query, (user_id,))

            if user_result:
                user_email = user_result[0][0]
                self.notification_service.send_notification(
                    user_email,
                    f"Order confirmed! Total: ${total}"
                )

            self.logging_service.log_info("Order processed successfully")
            return True

        except Exception as e:
            self.logging_service.log_error(f"Order processing failed: {str(e)}")
            return False

# PROBLEMS WITH THIS APPROACH:
# 1. Cannot unit test without real database, SMTP server, file system
# 2. Hard to test error scenarios (network failures, database errors)
# 3. Cannot easily switch implementations (e.g., test vs production database)
# 4. Configuration is scattered and hard-coded
# 5. Services are tightly coupled to specific implementations
# 6. Impossible to test individual components in isolation
# 7. Setup and teardown for tests is complex and fragile
# 8. Cannot easily mock external services for testing
# 9. Difficult to test different configurations
# 10. Violates Single Responsibility Principle (classes manage dependencies + business logic)
