"""
❌ VIOLATION of Dependency Inversion Principle

Problem: UserService zależy od KONKRETNEJ implementacji (MySQLDatabase)
- Nie można łatwo zmienić na PostgreSQL lub MongoDB
- Naruszenie DIP: zależności powinny wskazywać na abstrakcje, nie konkretne klasy
"""


class MySQLDatabase:
    """Konkretna implementacja bazy MySQL"""

    def connect(self) -> str:
        return "Connected to MySQL"

    def save(self, user_id: str, name: str) -> str:
        return f"Saved {user_id}: {name} to MySQL"


class PostgreSQLDatabase:
    """Konkretna implementacja bazy PostgreSQL"""

    def connect(self) -> str:
        return "Connected to PostgreSQL"

    def save(self, user_id: str, name: str) -> str:
        return f"Saved {user_id}: {name} to PostgreSQL"


class UserService:
    """
    ❌ PROBLEM: Bezpośrednia zależność od MySQLDatabase

    Konsekwencje:
    1. Nie można zmienić bazy danych bez edycji tej klasy
    2. Wysokopoziomowy moduł zależy od niskopoziomowego
    3. Trudne testowanie (musimy użyć prawdziwego MySQL)
    4. Zmiana DB wymaga modyfikacji kodu klasy
    """

    def __init__(self):
        # ❌ PROBLEM: Tworzymy MySQLDatabase bezpośrednio
        # Silne sprzężenie z konkretną implementacją
        self.database = MySQLDatabase()

    def save_user(self, user_id: str, name: str) -> str:
        """
        ❌ Zawsze używa MySQL, nie można zmienić
        """
        result = self.database.connect()
        result += "\n" + self.database.save(user_id, name)
        return result


# ❌ Przykład użycia - działa, ale narusza DIP
if __name__ == "__main__":
    # ❌ UserService zawsze używa MySQL
    service = UserService()
    print(service.save_user("user1", "Alice"))

    # ❌ Chcę użyć PostgreSQL?
    # Muszę:
    # 1. EDYTOWAĆ UserService.__init__()
    # 2. Zmienić MySQLDatabase() na PostgreSQLDatabase()
    # 3. Przekompilować/wdrożyć kod
    #
    # To naruszenie DIP!

    # ❌ Nie mogę zrobić:
    # service_postgres = UserService(PostgreSQLDatabase())  # Nie ma takiej opcji!


"""
Dlaczego to jest ZŁE?

1. ❌ High-level zależy od low-level
   - UserService (wysoki poziom) → MySQLDatabase (niski poziom) (wysokość poziomu mierzymy poziomem abstrakcji)
   - Powinno być: oba zależą od abstrakcji (Database)

2. ❌ Niemożliwa zmiana implementacji
   - Nie można użyć PostgreSQL bez edycji UserService
   - Zmiana bazy = zmiana kodu wysokopoziomowego

3. ❌ Trudne testowanie
   - Nie można wstrzyknąć mock database
   - Testy wymagają prawdziwego MySQL

4. ❌ Naruszenie Open/Closed
   - Dodanie MongoDB wymaga edycji UserService
   - Klasa nie jest zamknięta na modyfikacje

5. ❌ Silne sprzężenie
   - UserService "wie" o MySQLDatabase
   - Zmiana w MySQL może wpłynąć na UserService

Jak to naprawić?
1. Stwórz interfejs Database (ABC)
2. MySQLDatabase i PostgreSQLDatabase dziedziczą po Database
3. UserService przyjmuje Database w konstruktorze (dependency injection)
"""
