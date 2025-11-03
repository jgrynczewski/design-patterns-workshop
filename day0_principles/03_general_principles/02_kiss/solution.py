"""
KISS Solution - Keep It Simple, Stupid
Proste rozwiązania dla prostych problemów
"""


def calculate_total(items):
    """KISS: Prosta funkcja do prostego zadania"""
    return sum(items)


def calculate_weighted_total(items, weights):
    """KISS: Dodaj złożoność tylko gdy potrzebna"""
    return sum(item * weight for item, weight in zip(items, weights))


def authenticate_user(username, password):
    """KISS: Prosta autentykacja dla prostej aplikacji"""
    users = {"admin": "password123", "user": "pass456"}
    return username in users and users[username] == password


class SimpleShoppingCart:
    """KISS: Prosta implementacja koszyka"""

    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

    def get_item_count(self):
        return len(self.items)


class UserManager:
    """KISS: Proste zarządzanie użytkownikami"""

    def __init__(self):
        self.users = {}
        self.logged_in_users = set()

    def register_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.logged_in_users.add(username)
            return True
        return False

    def logout(self, username):
        self.logged_in_users.discard(username)

    def is_logged_in(self, username):
        return username in self.logged_in_users


# Przykład: Kiedy można dodać złożoność (ale tylko gdy potrzebna)
class UserManagerWithSecurity:
    """
    KISS + Security: Dodajemy złożoność tylko tam gdzie jest potrzebna
    Większość firm potrzebuje basic security, więc to uzasadnione
    """

    def __init__(self):
        self.users = {}
        self.logged_in_users = set()
        self.failed_attempts = {}  # Dodane tylko dla security
        self.max_attempts = 3

    def register_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def login(self, username, password):
        # Prosta logika, ale z podstawowym security
        if self.failed_attempts.get(username, 0) >= self.max_attempts:
            return False  # Account locked

        if username in self.users and self.users[username] == password:
            self.logged_in_users.add(username)
            if username in self.failed_attempts:
                del self.failed_attempts[username]  # Reset on success
            return True

        # Track failed attempts
        self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
        return False

    def logout(self, username):
        self.logged_in_users.discard(username)

    def is_logged_in(self, username):
        return username in self.logged_in_users


# Przykład progresywnej złożoności - zaczynamy prosto, dodajemy gdy potrzeba
class FileProcessor:
    """KISS: Start simple, add complexity when needed"""

    def read_file(self, filename):
        # V1: Najprostsza implementacja
        with open(filename, 'r') as f:
            return f.read()

    def read_file_safe(self, filename):
        # V2: Dodajemy error handling tylko gdy mamy problemy
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def read_file_with_encoding(self, filename, encoding='utf-8'):
        # V3: Dodajemy encoding tylko gdy mamy problemy z różnymi plikami
        try:
            with open(filename, 'r', encoding=encoding) as f:
                return f.read()
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None


if __name__ == "__main__":
    # Proste rozwiązania dla prostych problemów
    print(f"Sum: {calculate_total([1, 2, 3, 4])}")
    print(f"Weighted sum: {calculate_weighted_total([1, 2, 3], [0.5, 1.0, 2.0])}")

    print(f"Auth admin: {authenticate_user('admin', 'password123')}")
    print(f"Auth wrong: {authenticate_user('admin', 'wrong')}")

    # Prosta klasa zamiast over-engineered patterns
    cart = SimpleShoppingCart()
    cart.add_item("Laptop", 1000)
    cart.add_item("Mouse", 50)
    print(f"Cart total: ${cart.get_total()}")

    # User management - prosty i czytelny
    user_mgr = UserManager()
    user_mgr.register_user("john", "secret123")
    print(f"Login successful: {user_mgr.login('john', 'secret123')}")
    print(f"Is logged in: {user_mgr.is_logged_in('john')}")

    # Security tylko tam gdzie potrzebne
    secure_mgr = UserManagerWithSecurity()
    secure_mgr.register_user("admin", "admin123")
    print(f"Login attempts: {secure_mgr.login('admin', 'wrong')}")
    print(f"Login attempts: {secure_mgr.login('admin', 'wrong')}")
    print(f"Login attempts: {secure_mgr.login('admin', 'wrong')}")
    print(f"Account locked: {secure_mgr.login('admin', 'admin123')}")  # Should fail - locked

    print("✅ Proste rozwiązania = łatwe do zrozumienia")
    print("✅ Dodajemy złożoność tylko gdy rzeczywiście potrzebna")
    print("✅ 5 linii zamiast 50 dla podstawowych operacji")
    print("✅ Kod robi dokładnie to co potrzebne, nic więcej")
