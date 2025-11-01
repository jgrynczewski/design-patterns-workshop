"""Konkretne implementacje baz danych"""
from interfaces.database import DatabaseInterface


class MySQLDatabase(DatabaseInterface):
    def save_order(self, order_data):
        print(f"MySQL: Saving order to database")


class PostgreSQLDatabase(DatabaseInterface):
    def save_order(self, order_data):
        print(f"PostgreSQL: Saving order to database")
