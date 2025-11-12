"""
Testy dla DIP - Database Abstraction
"""

import pytest
from starter import Database, MySQLDatabase, PostgreSQLDatabase, UserService


class TestDIP:
    """Testy Dependency Inversion Principle"""

    def test_mysql_connect(self):
        db = MySQLDatabase()
        assert db.connect() == "Connected to MySQL"

    def test_mysql_save(self):
        db = MySQLDatabase()
        result = db.save("user1", "Alice")
        assert "user1" in result
        assert "Alice" in result
        assert "MySQL" in result

    def test_postgres_connect(self):
        db = PostgreSQLDatabase()
        assert db.connect() == "Connected to PostgreSQL"

    def test_postgres_save(self):
        db = PostgreSQLDatabase()
        result = db.save("user2", "Bob")
        assert "user2" in result
        assert "Bob" in result
        assert "PostgreSQL" in result

    def test_databases_implement_interface(self):
        mysql = MySQLDatabase()
        postgres = PostgreSQLDatabase()

        assert isinstance(mysql, Database)
        assert isinstance(postgres, Database)

    def test_user_service_with_mysql(self):
        mysql = MySQLDatabase()
        service = UserService(mysql)
        result = service.save_user("user1", "Alice")

        assert "MySQL" in result
        assert "Alice" in result

    def test_user_service_with_postgres(self):
        postgres = PostgreSQLDatabase()
        service = UserService(postgres)
        result = service.save_user("user2", "Bob")

        assert "PostgreSQL" in result
        assert "Bob" in result

    def test_dip_extensibility(self):
        """Test DIP: można dodać nową bazę bez zmiany UserService"""

        class MongoDB(Database):
            def connect(self):
                return "Connected to MongoDB"

            def save(self, user_id, name):
                return f"Saved {user_id}: {name} to MongoDB"

        mongo = MongoDB()
        service = UserService(mongo)
        result = service.save_user("user3", "Charlie")

        assert "MongoDB" in result
        assert "Charlie" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
