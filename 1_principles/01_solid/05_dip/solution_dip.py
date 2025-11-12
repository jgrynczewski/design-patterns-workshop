"""
Dependency Inversion Principle - Database Abstraction - SOLUTION

>>> mysql = MySQLDatabase()
>>> mysql.connect()
'Connected to MySQL'

>>> service = UserService(mysql)
>>> result = service.save_user("user1", "Bob")
>>> "MySQL" in result
True
"""

from abc import ABC, abstractmethod


class Database(ABC):
    """Interfejs bazy danych"""

    @abstractmethod
    def connect(self) -> str:
        pass

    @abstractmethod
    def save(self, user_id: str, name: str) -> str:
        pass


class MySQLDatabase(Database):
    """Implementacja MySQL"""

    def connect(self) -> str:
        return "Connected to MySQL"

    def save(self, user_id: str, name: str) -> str:
        return f"Saved {user_id}: {name} to MySQL"


class PostgreSQLDatabase(Database):
    """Implementacja PostgreSQL"""

    def connect(self) -> str:
        return "Connected to PostgreSQL"

    def save(self, user_id: str, name: str) -> str:
        return f"Saved {user_id}: {name} to PostgreSQL"


class UserService:
    """Serwis użytkowników - zależy od abstrakcji"""

    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user_id: str, name: str) -> str:
        result = self.database.connect()
        result += "\n" + self.database.save(user_id, name)
        return result


if __name__ == "__main__":
    # Demo DIP
    print("=== DIP: UserService with different databases ===\n")

    mysql_db = MySQLDatabase()
    service1 = UserService(mysql_db)
    print(service1.save_user("user1", "Alice"))
    print()

    postgres_db = PostgreSQLDatabase()
    service2 = UserService(postgres_db)
    print(service2.save_user("user2", "Bob"))
    print()

    print("DIP: Można dodać MongoDB bez zmiany UserService:")

    class MongoDB(Database):
        def connect(self):
            return "Connected to MongoDB"

        def save(self, user_id, name):
            return f"Saved {user_id}: {name} to MongoDB"

    mongo_db = MongoDB()
    service3 = UserService(mongo_db)
    print(service3.save_user("user3", "Charlie"))
