"""
Low Coupling Solution
Klasa zależy od abstrakcji i ma minimalne dependencies
"""

from abc import ABC, abstractmethod


class Repository(ABC):  # Abstrakcja zamiast konkretnej klasy
    @abstractmethod
    def save(self, data): pass


class NotificationService(ABC):  # Jedna abstrakcja dla powiadomień
    @abstractmethod
    def notify(self, recipient, message): pass


class OrderProcessor:  # Low coupling — tylko 2 abstrakcje
    def __init__(self, repo: Repository, notifier: NotificationService):
        self.repo = repo  # Abstrakcja
        self.notifier = notifier  # Abstrakcja
        # Tylko 2 dependencies zamiast 5

    def process(self, order):
        # Używa abstrakcji
        self.repo.save(order)
        self.notifier.notify(order['contact'], f"Order {order['id']} confirmed")
        return True


# Konkretne implementacje (mogą być w innych modułach)
class DatabaseRepository(Repository):
    def save(self, data):
        print("Saving to database")


class EmailNotifier(NotificationService):
    def notify(self, recipient, message):
        print(f"Email to {recipient}: {message}")


class CompositeNotifier(NotificationService):  # Composite pattern
    def __init__(self, notifiers):
        self.notifiers = notifiers

    def notify(self, recipient, message):
        for notifier in self.notifiers:
            notifier.notify(recipient, message)


class SMSNotifier(NotificationService):
    def notify(self, recipient, message):
        print(f"SMS to {recipient}: {message}")


class LoggingRepository(Repository):  # Decorator pattern
    def __init__(self, repo, logger):
        self.repo = repo
        self.logger = logger

    def save(self, data):
        self.logger.log(f"Saving order {data.get('id')}")
        self.repo.save(data)


class SimpleLogger:
    def log(self, message):
        print(f"Log: {message}")


if __name__ == "__main__":
    # Łatwa konfiguracja różnych implementacji

    # Konfiguracja 1: Prosta
    repo = DatabaseRepository()
    notifier = EmailNotifier()
    processor = OrderProcessor(repo, notifier)

    # Konfiguracja 2: Z loggingiem i wieloma notifierami
    logger = SimpleLogger()
    logged_repo = LoggingRepository(DatabaseRepository(), logger)
    multi_notifier = CompositeNotifier([EmailNotifier(), SMSNotifier()])
    advanced_processor = OrderProcessor(logged_repo, multi_notifier)

    order = {
        'id': 123,
        'total': 100,
        'contact': 'test@example.com'
    }

    print("=== Simple processor ===")
    processor.process(order)

    print("\n=== Advanced processor ===")
    advanced_processor.process(order)

    print("✅ OrderProcessor ma tylko 2 abstrakcje")
    print("✅ Łatwe testowanie - można mock abstrakcje")
    print("✅ Łatwe rozszerzanie - kompozycja bez modyfikacji")
