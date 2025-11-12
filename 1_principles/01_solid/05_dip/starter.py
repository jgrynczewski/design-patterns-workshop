"""
Dependency Inversion Principle - Database Abstraction

>>> mysql = MySQLDatabase()
>>> mysql.connect()
'Connected to MySQL'
>>> mysql.save("user123", "Alice")
'Saved user123: Alice to MySQL'

>>> postgres = PostgreSQLDatabase()
>>> postgres.connect()
'Connected to PostgreSQL'

>>> # Test UserService with different databases
>>> service = UserService(mysql)
>>> service.save_user("user1", "Bob")
'Connected to MySQL\\nSaved user1: Bob to MySQL'

>>> service2 = UserService(postgres)
>>> service2.save_user("user2", "Charlie")
'Connected to PostgreSQL\\nSaved user2: Charlie to PostgreSQL'
"""

from abc import ABC, abstractmethod


class Database(ABC):
    """Interfejs bazy danych"""

    @abstractmethod
    def connect(self) -> str:
        """Łączy się z bazą danych"""
        pass

    @abstractmethod
    def save(self, user_id: str, name: str) -> str:
        """Zapisuje użytkownika"""
        pass


# TODO: Zaimplementuj MySQLDatabase
# Hint: connect() zwraca "Connected to MySQL"
# Hint: save() zwraca "Saved {user_id}: {name} to MySQL"

class MySQLDatabase:
    pass


# TODO: Zaimplementuj PostgreSQLDatabase
# Hint: connect() zwraca "Connected to PostgreSQL"
# Hint: save() zwraca "Saved {user_id}: {name} to PostgreSQL"

class PostgreSQLDatabase:
    pass


class UserService:
    """
    Serwis użytkowników - zależy od ABSTRAKCJI (Database)
    nie od konkretnej implementacji (MySQLDatabase)
    """

    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user_id: str, name: str) -> str:
        """
        Zapisuje użytkownika

        DIP: UserService nie wie, czy to MySQL, PostgreSQL czy MongoDB
        Zależy tylko od interfejsu Database
        """
        result = self.database.connect()
        result += "\n" + self.database.save(user_id, name)
        return result


# DIP: High-level (UserService) zależy od abstrakcji (Database)
# Low-level (MySQLDatabase, PostgreSQL) też zależą od abstrakcji
# Możemy dodać MongoDB bez zmiany UserService!
