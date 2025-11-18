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


# TODO: Zdefiniuj interfejs Database (ABC)
# Metody: connect() i save(user_id, name)

class Database(ABC):
    @abstractmethod
    def connect(self) -> str:
        """Nawiązuje połączenie z bazą danych"""
        pass

    @abstractmethod
    def save(self, user_id: str, name: str) -> str:
        """Zapisuje użytkownika do bazy danych"""
        pass


# TODO: Zaimplementuj MySQLDatabase
# Dziedziczy po Database
# Formaty: "Connected to MySQL", "Saved {user_id}: {name} to MySQL"

class MySQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to MySQL"

    def save(self, user_id: str, name: str) -> str:
        return f"Saved {user_id}: {name} to MySQL"


# TODO: Zaimplementuj PostgreSQLDatabase
# Dziedziczy po Database
# Formaty: "Connected to PostgreSQL", "Saved {user_id}: {name} to PostgreSQL"

class PostgreSQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to PostgreSQL"

    def save(self, user_id: str, name: str) -> str:
        return f"Saved {user_id}: {name} to PostgreSQL"


# TODO: Zaimplementuj UserService
# Konstruktor przyjmuje database: Database (dependency injection)
# Metoda save_user(user_id, name) używa database.connect() i database.save()

class UserService:
    def __init__(self, database: Database):
        """Dependency Injection - UserService zależy od abstrakcji"""
        self.database = database

    def save_user(self, user_id: str, name: str) -> str:
        """Używa abstrakcji Database - działa z dowolną implementacją"""
        result = self.database.connect()
        result += "\n" + self.database.save(user_id, name)
        return result


# DIP: High-level (UserService) zależy od abstrakcji (Database)
# Low-level (MySQLDatabase, PostgreSQL) też zależą od abstrakcji
# Możemy dodać MongoDB bez zmiany UserService!


# Przykład użycia
if __name__ == "__main__":
    mysql = MySQLDatabase()
    service = UserService(mysql)
    print(service.save_user("user1", "Alice"))

    postgres = PostgreSQLDatabase()
    service2 = UserService(postgres)
    print(service2.save_user("user2", "Bob"))
