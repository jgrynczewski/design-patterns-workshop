"""
YAGNI Solution - You Ain't Gonna Need It
Implementuj tylko to czego rzeczywiście potrzebujesz TERAZ
"""

import json
from datetime import datetime


class User:
    """YAGNI: Tylko to co potrzebne w aktualnych wymaganiach"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # I to wszystko! Nie dodajemy nic więcej dopóki nie będzie potrzebne


class DataProcessor:
    """YAGNI: Obsługujemy tylko JSON - jedyny format którego używamy"""

    def process_json(self, data):
        """Prosta implementacja dla aktualnych potrzeb"""
        return json.loads(data)

    # Nie implementujemy XML/CSV/YAML dopóki ich nie potrzebujemy
    # Gdy będziemy potrzebować XML - dodamy process_xml()
    # Gdy będziemy potrzebować CSV - dodamy process_csv()


class EmailService:
    """YAGNI: Prosty email service dla aktualnych potrzeb"""

    def send_email(self, to, subject, body):
        """Podstawowa funkcjonalność email - to wszystko czego teraz potrzebujemy"""
        print(f"Sending email to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # Używamy prostego SMTP - jedynego providera którego faktycznie używamy
        return True

    # Nie dodajemy SendGrid/Mailgun/SES dopóki nie migrujemy
    # Nie dodajemy template engine dopóki nie mamy complex templates
    # Nie dodajemy A/B testing dopóki nie jest to requirement


# Przykład ewolucji: jak dodawać funkcjonalność gdy jest rzeczywiście potrzebna
class UserV1:
    """Wersja 1: Minimum Viable Product"""

    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserV2:
    """Wersja 2: Dodajemy preferences gdy okazało się że są potrzebne"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.preferences = {}  # Dodane tylko gdy users zaczęli pytać o preferences

    def set_preference(self, key, value):
        self.preferences[key] = value


class UserV3:
    """Wersja 3: Dodajemy timestamps gdy potrzebujemy auditingu"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.preferences = {}
        self.created_at = datetime.now()  # Dodane gdy biznes zapytał "kiedy user się zarejestrował?"

    def set_preference(self, key, value):
        self.preferences[key] = value


# Przykład: Incremental Development zamiast Speculative Development
class ShoppingCart:
    """Start simple - dodaj funkcjonalność gdy jest potrzebna"""

    def __init__(self):
        self.items = []  # Start z prostą listą

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

    # Nie dodajemy:
    # - Quantity tracking (dopóki ktoś nie powie "chcę 2 laptopy")
    # - Discount codes (dopóki marketing nie powie "chcemy promocje")
    # - Tax calculation (dopóki nie sprzedajemy w różnych stanach)
    # - Shipping costs (dopóki nie mamy fizycznych produktów)
    # - Inventory checking (dopóki nie mamy problemów z stock)


class ShoppingCartV2:
    """Dodajemy quantity gdy okazało się że jest potrzebne"""

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):  # Dodane gdy users chcieli quantity
        existing_item = self._find_item(name)
        if existing_item:
            existing_item["quantity"] += quantity
        else:
            self.items.append({"name": name, "price": price, "quantity": quantity})

    def _find_item(self, name):
        for item in self.items:
            if item["name"] == name:
                return item
        return None

    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)


class ConfigurationManager:
    """YAGNI: Prosta konfiguracja zamiast complex config system"""

    def __init__(self):
        # Start z prostym dictionary - upgrade gdy będzie potrzeba
        self.config = {
            "app_name": "MyApp",
            "debug": True,
            "database_url": "sqlite:///app.db"
        }

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    # Nie implementujemy:
    # - Environment-specific configs (dopóki nie mamy staging/prod)
    # - Config validation (dopóki nie mamy błędów z config)
    # - Config hot-reloading (dopóki nie jest to problem)
    # - Encrypted configs (dopóki nie przechowujemy secrets)
    # - Config versioning (dopóki nie ma konfliktów deployment)


# Anti-example: Co NIE robić
class OverEngineeredConfigManager:
    """To jest przykład czego NIE robić - over-engineering na start"""

    def __init__(self):
        self.environments = ["dev", "staging", "prod"]
        self.config_sources = ["file", "env", "consul", "vault"]
        self.validation_schemas = {}
        self.config_history = []
        self.hot_reload_enabled = False
        self.encryption_enabled = False
        # 100 linii kodu dla... przechowywania 3 wartości konfiguracji


if __name__ == "__main__":
    # YAGNI: Start simple
    user = User("John Doe", "john@example.com")
    print(f"User: {user.name} ({user.email})")

    # Process only what we need
    processor = DataProcessor()
    data = '{"message": "hello", "count": 42}'
    result = processor.process_json(data)
    print(f"Processed: {result}")

    # Simple email
    email = EmailService()
    email.send_email("user@example.com", "Welcome", "Hello and welcome!")

    # Shopping cart evolution
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000)
    cart.add_item("Mouse", 50)
    print(f"Cart V1 total: ${cart.get_total()}")

    cart_v2 = ShoppingCartV2()
    cart_v2.add_item("Laptop", 1000, 2)  # Now supports quantity
    cart_v2.add_item("Mouse", 50, 1)
    print(f"Cart V2 total: ${cart_v2.get_total()}")

    # Simple config
    config = ConfigurationManager()
    print(f"App name: {config.get('app_name')}")
    print(f"Debug mode: {config.get('debug')}")

    print("✅ Implementujemy tylko to czego rzeczywiście używamy")
    print("✅ Dodajemy funkcjonalność gdy staje się potrzebna")
    print("✅ Nie ma martwego kodu ani spekulacyjnych features")
    print("✅ Kod jest prosty i łatwy do zrozumienia")
    print("✅ Incremental development > Big Design Up Front")
