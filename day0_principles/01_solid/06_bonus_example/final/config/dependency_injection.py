"""Konfiguracja dependency injection"""
from implementations.database import MySQLDatabase, PostgreSQLDatabase
from implementations.email import SMTPEmailer, SendGridEmailer
from implementations.order_processing import OrderValidator, DiscountCalculator, OrderPersistence, EmailNotifier, \
    PaymentProcessor
from domain.discount import RegularCustomerDiscount
from core.order_processor import OrderProcessor


def create_mysql_smtp_processor():
    """Konfiguracja: MySQL + SMTP"""
    database = MySQLDatabase()
    emailer = SMTPEmailer()

    validator = OrderValidator()
    discount_calc = DiscountCalculator(RegularCustomerDiscount())
    persistence = OrderPersistence(database)
    notifier = EmailNotifier(emailer)
    payment = PaymentProcessor()

    return OrderProcessor(
        validator=validator,
        discount_calculator=discount_calc,
        persistence=persistence,
        notifier=notifier,
        payment_processor=payment
    )


def create_postgres_sendgrid_processor():
    """Konfiguracja: PostgreSQL + SendGrid"""
    database = PostgreSQLDatabase()
    emailer = SendGridEmailer()

    validator = OrderValidator()
    discount_calc = DiscountCalculator(RegularCustomerDiscount())
    persistence = OrderPersistence(database)
    notifier = EmailNotifier(emailer)
    payment = PaymentProcessor()

    return OrderProcessor(
        validator=validator,
        discount_calculator=discount_calc,
        persistence=persistence,
        notifier=notifier,
        payment_processor=payment
    )
