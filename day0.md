# Day 0: Programming Principles - Complete Specification

## 📁 Folder Structure
```
day0_principles/
├── README.md                    # Ogólny przegląd wszystkich zasad
├── 01_solid/
│   ├── README.md               # Teoria SOLID + linki
│   ├── violations.py           # Wszystkie 5 zasad - złe przykłady
│   ├── solutions.py            # Wszystkie 5 zasad - dobre przykłady
│   └── exercise.md             # Zadania do wykonania
├── 02_grasp/
│   ├── README.md               # Teoria GRASP + kontekst
│   ├── violations.py           # Wszystkie 9 zasad - złe przykłady
│   ├── solutions.py            # Wszystkie 9 zasad - dobre przykłady
│   └── exercise.md             # Zadania code review
├── 03_general_principles/
│   ├── README.md               # DRY, KISS, YAGNI, SoC
│   ├── violations.py           # Złe przykłady
│   ├── solutions.py            # Dobre przykłady
│   └── exercise.md             # Zadania refactoring
├── 04_dependency_injection/
│   ├── README.md               # DI teoria + kiedy używać
│   ├── anti_patterns.py        # Service Locator, itp.
│   ├── patterns.py             # Constructor, Setter, Interface injection
│   └── exercise.md             # Zadania DI
└── 05_additional/
    ├── README.md               # Tell Don't Ask, Law of Demeter, itp.
    ├── violations.py           # Złe przykłady
    ├── solutions.py            # Dobre przykłady
    └── exercise.md             # Zadania
```

## 🎯 Flow pracy z kursantami

### Wariant A: Facilitated Code Review (ZALECANY)
```
15 min teoria (README.md) → 
20 min code review violations.py (wspólnie) →
15 min zadania w parach → 
10 min dyskusja solutions.py
```

### Wariant B: Individual Challenge
```
10 min teoria → 
30 min samodzielne zadania exercise.md →
20 min code review solutions + Q&A
```

### Wariant C: Workshop Style
```
5 min intro zasady →
10 min "code smells hunt" w violations.py →
15 min grupowe refactoring →
10 min prezentacja rozwiązań grup →
5 min pokazanie "official" solutions.py
```

## 📋 Complete Content Specifications

### SOLID PRINCIPLES

#### S - Single Responsibility Principle

**❌ Violation:**
```python
class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def save_to_database(self):
        # database saving logic
        pass
    
    def send_welcome_email(self):
        # email sending logic  
        pass
    
    def validate_email_format(self):
        # email validation logic
        pass
```

**✅ Solution:**
```python
class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def save(self, user): pass

class EmailService:  
    def send_welcome(self, user): pass

class EmailValidator:
    def is_valid(self, email): pass
```

#### O - Open/Closed Principle

**❌ Violation:**
```python
class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.95
        elif customer_type == "premium":
            return amount * 0.90
        elif customer_type == "vip":
            return amount * 0.85
        # Jak dodać "student" bez modyfikacji tej klasy?
```

**✅ Solution:**
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount): pass

class RegularDiscount(DiscountStrategy):
    def calculate(self, amount): return amount * 0.95

class StudentDiscount(DiscountStrategy):  # Nowy typ - zero zmian w istniejącym kodzie
    def calculate(self, amount): return amount * 0.80

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
    
    def calculate(self, amount):
        return self.strategy.calculate(amount)
```

#### L - Liskov Substitution Principle

**❌ Violation:**
```python
class Bird:
    def fly(self): pass

class Sparrow(Bird):
    def fly(self): return "Flying high"

class Penguin(Bird):
    def fly(self): raise Exception("Cannot fly!")  # Narusza kontrakt Bird

def make_bird_fly(bird: Bird):
    return bird.fly()  # Crash dla Penguin!
```

**✅ Solution:**
```python
class Bird:
    def move(self): pass

class FlyingBird(Bird):
    def fly(self): pass
    def move(self): return self.fly()

class Sparrow(FlyingBird):
    def fly(self): return "Flying high"

class Penguin(Bird):  # Nie dziedziczy po FlyingBird
    def move(self): return "Swimming fast"
```

#### I - Interface Segregation Principle

**❌ Violation:**
```python
class Printer(ABC):
    @abstractmethod
    def print_document(self): pass
    @abstractmethod
    def scan_document(self): pass
    @abstractmethod
    def fax_document(self): pass

class SimplePrinter(Printer):  # Ma tylko funkcję druku
    def print_document(self): return "Printing"
    def scan_document(self): raise NotImplementedError  # Zmuszony do implementacji
    def fax_document(self): raise NotImplementedError   # Zmuszony do implementacji
```

**✅ Solution:**
```python
class Printable(ABC):
    @abstractmethod
    def print_document(self): pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self): pass

class SimplePrinter(Printable):  # Implementuje tylko to czego potrzebuje
    def print_document(self): return "Printing"

class MultiFunctionPrinter(Printable, Scannable):
    def print_document(self): return "Printing"
    def scan_document(self): return "Scanning"
```

#### D - Dependency Inversion Principle

**❌ Violation:**
```python
class EmailSender:
    def send(self, message): pass

class NotificationService:
    def __init__(self):
        self.sender = EmailSender()  # Hardcoded dependency
    
    def notify(self, message):
        self.sender.send(message)  # Nie można użyć SMS, Push, etc.
```

**✅ Solution:**
```python
class MessageSender(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailSender(MessageSender):
    def send(self, message): return f"Email: {message}"

class SMSSender(MessageSender):
    def send(self, message): return f"SMS: {message}"

class NotificationService:
    def __init__(self, sender: MessageSender):  # Dependency injection
        self.sender = sender
    
    def notify(self, message):
        return self.sender.send(message)
```

### GRASP PRINCIPLES (All 9)

#### 1. Information Expert
**❌ Violation:**
```python
class Order:
    def __init__(self):
        self.items = []

class OrderService:  # Ma informacje o Order, ale nie ma dostępu do items
    def calculate_total(self, order):
        total = 0
        for item in order.items:  # Musi "zagłębiać się" w Order
            total += item.price * item.quantity
        return total
```

**✅ Solution:**
```python
class Order:
    def __init__(self):
        self.items = []
    
    def calculate_total(self):  # Order ma items, więc Order oblicza total
        return sum(item.price * item.quantity for item in self.items)
```

#### 2. Creator
**❌ Violation:**
```python
class OrderManager:
    def add_item_to_order(self, order, product_id, quantity):
        item = OrderItem(product_id, quantity)  # OrderManager tworzy OrderItem?
        order.add_item(item)
```

**✅ Solution:**
```python
class Order:
    def add_item(self, product_id, quantity):
        item = OrderItem(product_id, quantity)  # Order tworzy OrderItem (zawiera items)
        self.items.append(item)
```

#### 3. Controller
**❌ Violation:**
```python
# HTTP handler bezpośrednio manipuluje domain objects
class UserHTTPHandler:
    def create_user(self, request):
        user = User(request.data["name"])  # HTTP layer zna domain
        user.save_to_db()                  # HTTP layer zna persistence
        user.send_welcome_email()          # HTTP layer zna email logic
        return "OK"
```

**✅ Solution:**
```python
class UserController:  # Controller koordynuje use case
    def __init__(self, user_repo, email_service):
        self.user_repo = user_repo
        self.email_service = email_service
    
    def create_user(self, user_data):
        user = User(user_data["name"])
        self.user_repo.save(user)
        self.email_service.send_welcome(user)
        return user

class UserHTTPHandler:  # HTTP layer tylko konwertuje format
    def __init__(self, controller):
        self.controller = controller
    
    def create_user(self, request):
        user = self.controller.create_user(request.data)
        return {"id": user.id}
```

#### 4. Low Coupling
**❌ Violation:**
```python
class OrderProcessor:
    def __init__(self):
        self.db = Database()           # Zna konkretną implementację DB
        self.email = SMTPEmailer()     # Zna konkretną implementację email
        self.logger = FileLogger()     # Zna konkretną implementację logger
        self.payment = PayPalGateway() # Zna konkretną implementację payment
        # 4 konkretne dependencies = high coupling
```

**✅ Solution:**
```python
class OrderProcessor:
    def __init__(self, repo, notifier):  # Tylko 2 abstrakcje
        self.repo = repo                 # Repository abstraction
        self.notifier = notifier         # Notification abstraction
    
    def process(self, order):
        self.repo.save(order)
        self.notifier.notify(f"Order {order.id} processed")
```

#### 5. High Cohesion
**❌ Violation:**
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def change_password(self, new_password): pass  # OK - user operation
    def get_full_name(self): pass                 # OK - user data
    def send_marketing_email(self): pass          # NIE - marketing operation
    def generate_report(self): pass               # NIE - reporting operation
    def backup_to_s3(self): pass                  # NIE - infrastructure operation
```

**✅ Solution:**
```python
class User:  # Tylko user-related operations
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def change_password(self, new_password): pass
    def get_full_name(self): pass

class MarketingService:  # Marketing operations
    def send_marketing_email(self, user): pass

class ReportGenerator:  # Reporting operations  
    def generate_user_report(self, user): pass
```

#### 6. Polymorphism
**❌ Violation:**
```python
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            return self._process_credit_card(amount)
        elif payment_type == "paypal":
            return self._process_paypal(amount)
        elif payment_type == "bank_transfer":
            return self._process_bank_transfer(amount)
        # Każdy nowy typ = modyfikacja tej metody
```

**✅ Solution:**
```python
class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount): pass

class CreditCard(PaymentMethod):
    def process(self, amount): return f"Credit card: {amount}"

class PayPal(PaymentMethod):
    def process(self, amount): return f"PayPal: {amount}"

class PaymentProcessor:
    def process_payment(self, method: PaymentMethod, amount):
        return method.process(amount)  # Polimorfizm zamiast if/else
```

#### 7. Pure Fabrication
**❌ Violation:**
```python
class User:
    def save_to_database(self): pass     # User nie powinien znać DB
    def send_email(self): pass           # User nie powinien znać email
    def log_activity(self): pass         # User nie powinien znać logging

class Order:  
    def persist_to_file(self): pass      # Order nie powinien znać file system
    def encrypt_data(self): pass         # Order nie powinien znać crypto
```

**✅ Solution:**
```python
# Pure Fabrications - klasy które nie reprezentują domain concepts
class UserRepository:      # Fabrication dla persistence
    def save(self, user): pass

class EmailService:        # Fabrication dla email
    def send(self, user, message): pass

class ActivityLogger:      # Fabrication dla logging
    def log_user_action(self, user, action): pass

class User:               # Czyste domain object
    def __init__(self, name):
        self.name = name
```

#### 8. Indirection
**❌ Violation:**
```python
class OrderService:
    def __init__(self):
        self.payment = PayPalAPI()  # Bezpośrednia dependency na PayPal

    def process_order(self, order):
        result = self.payment.charge_credit_card(  # Zna PayPal API
            order.total, 
            order.card_number
        )
        return result
```

**✅ Solution:**
```python
class PaymentGateway(ABC):  # Indirection layer
    @abstractmethod
    def process_payment(self, amount, card): pass

class PayPalAdapter(PaymentGateway):  # Adapter dla PayPal
    def __init__(self):
        self.paypal = PayPalAPI()
    
    def process_payment(self, amount, card):
        return self.paypal.charge_credit_card(amount, card)

class OrderService:
    def __init__(self, gateway: PaymentGateway):  # Zależność od abstrakcji
        self.gateway = gateway

    def process_order(self, order):
        return self.gateway.process_payment(order.total, order.card)
```

#### 9. Protected Variations
**❌ Violation:**
```python
class WeatherService:
    def get_temperature(self, city):
        # Bezpośrednie wywołanie external API
        response = requests.get(f"http://api.weather.com/v1/current?city={city}")
        return response.json()["current"]["temperature"]  # Łamie się gdy API się zmieni
        
class ReportGenerator:
    def generate_weather_report(self, city):
        weather = WeatherService()
        temp = weather.get_temperature(city)
        return f"Temperature in {city}: {temp}°C"  # Zależy od konkretnej struktury API
```

**✅ Solution:**
```python
class WeatherData:  # Stable internal model
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

class WeatherAdapter(ABC):  # Interface chroni przed zmianami
    @abstractmethod
    def get_weather(self, city) -> WeatherData: pass

class OpenWeatherAdapter(WeatherAdapter):  # Konkretny adapter
    def get_weather(self, city) -> WeatherData:
        response = requests.get(f"http://api.openweather.com?city={city}")
        data = response.json()
        return WeatherData(
            temperature=data["main"]["temp"],  # Mapowanie external -> internal
            humidity=data["main"]["humidity"]
        )

class ReportGenerator:
    def __init__(self, weather: WeatherAdapter):
        self.weather = weather
    
    def generate_weather_report(self, city):
        data = self.weather.get_weather(city)  # Chronione od zmian API
        return f"Temperature in {city}: {data.temperature}°C"
```

### GENERAL PRINCIPLES

#### DRY - Don't Repeat Yourself
**❌ Violation:**
```python
class UserValidator:
    def validate_email(self, email):
        if "@" not in email or "." not in email:
            return False
        return True
    
    def validate_admin_email(self, email):
        if "@" not in email or "." not in email:  # Duplikacja!
            return False
        if not email.endswith("@company.com"):
            return False
        return True
```

**✅ Solution:**
```python
class UserValidator:
    def _is_valid_email_format(self, email):  # Jedna implementacja
        return "@" in email and "." in email
    
    def validate_email(self, email):
        return self._is_valid_email_format(email)
    
    def validate_admin_email(self, email):
        return (self._is_valid_email_format(email) and 
                email.endswith("@company.com"))
```

#### KISS - Keep It Simple, Stupid
**❌ Violation:**
```python
def calculate_total_with_complex_logic(items):
    result = 0
    for item in items:
        if hasattr(item, 'price') and item.price is not None:
            if hasattr(item, 'quantity') and item.quantity is not None:
                if item.quantity > 0 and item.price >= 0:
                    result += item.price * item.quantity
    return result
```

**✅ Solution:**
```python
def calculate_total(items):
    return sum(item.price * item.quantity for item in items)
```

#### YAGNI - You Ain't Gonna Need It
**❌ Violation:**
```python
class User:
    def __init__(self, name):
        self.name = name
        self.future_feature_data = {}     # YAGNI violation
        self.cache_layer = CacheLayer()   # YAGNI violation  
        self.metrics_tracker = Metrics()  # YAGNI violation
        # Wszędzie kod "na przyszłość" którego nie ma w requirements
```

**✅ Solution:**
```python
class User:
    def __init__(self, name):
        self.name = name
    # Tylko to co potrzebne TERAZ
```

### DEPENDENCY INJECTION

#### 1. Constructor Injection
**❌ Violation:**
```python
class OrderService:
    def __init__(self):
        self.repo = DatabaseOrderRepository()  # Hard dependency
        self.logger = FileLogger()             # Hard dependency
```

**✅ Solution:**
```python
class OrderService:
    def __init__(self, repo: OrderRepository, logger: Logger):  # Injected
        self.repo = repo
        self.logger = logger
```

#### 2. Setter Injection
**❌ Violation:**
```python
class EmailService:
    def __init__(self, required_config):
        self.config = required_config
        # Ale co z optional dependencies?
```

**✅ Solution:**
```python
class EmailService:
    def __init__(self, config):
        self.config = config
        self.template_engine = None  # Optional dependency
    
    def set_template_engine(self, engine):  # Setter injection dla optional
        self.template_engine = engine
```

#### 3. Interface Injection
**❌ Violation:**
```python
class CacheService:
    def __init__(self):
        # Potrzebuje config, ale skąd go wziąć?
        pass
```

**✅ Solution:**
```python
class ConfigurableService(ABC):
    @abstractmethod
    def configure(self, config): pass

class CacheService(ConfigurableService):
    def configure(self, config):  # Interface injection
        self.max_size = config.cache_max_size
        self.ttl = config.cache_ttl
```

#### 4. Service Locator (anti-pattern)
**❌ Violation:**
```python
class ServiceLocator:
    services = {}
    
    @classmethod
    def get(cls, service_name):
        return cls.services[service_name]

class OrderService:
    def __init__(self):
        self.repo = ServiceLocator.get("order_repo")      # Hidden dependency
        self.logger = ServiceLocator.get("logger")        # Hidden dependency
        # Nie widać zależności w interface!
```

**✅ Solution:**
```python
class OrderService:
    def __init__(self, repo: OrderRepository, logger: Logger):  # Explicit dependencies
        self.repo = repo
        self.logger = logger
# Wszystkie dependencies widoczne w konstruktorze
```

### ADDITIONAL PRINCIPLES

#### Tell, Don't Ask
**❌ Violation:**
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self): return self.balance
    def set_balance(self, amount): self.balance = amount

class PaymentService:
    def transfer_money(self, from_account, to_account, amount):
        if from_account.get_balance() >= amount:  # ASK
            from_account.set_balance(from_account.get_balance() - amount)  # ASK + manipulation
            to_account.set_balance(to_account.get_balance() + amount)      # ASK + manipulation
```

**✅ Solution:**
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):  # TELL it what to do
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def deposit(self, amount):   # TELL it what to do
        self.balance += amount

class PaymentService:
    def transfer_money(self, from_account, to_account, amount):
        if from_account.withdraw(amount):  # TELL, don't ask
            to_account.deposit(amount)     # TELL, don't ask
```

#### Law of Demeter (Principle of Least Knowledge)
**❌ Violation:**
```python
class Order:
    def get_customer_city(self):
        return self.customer.address.city.name  # Violates LoD - knows too much

class OrderProcessor:
    def calculate_shipping(self, order):
        city = order.customer.address.city.name      # Chain of calls
        country = order.customer.address.country.code # Chain of calls
        # OrderProcessor knows internal structure of Customer
```

**✅ Solution:**
```python
class Order:
    def get_shipping_destination(self):  # Delegate to customer
        return self.customer.get_shipping_destination()

class Customer:
    def get_shipping_destination(self):  # Delegate to address
        return self.address.get_shipping_destination()

class Address:
    def get_shipping_destination(self):  # Encapsulate the details
        return {
            'city': self.city.name,
            'country': self.country.code
        }

class OrderProcessor:
    def calculate_shipping(self, order):
        destination = order.get_shipping_destination()  # Single call
        # Uses destination dict without knowing internal structure
```

#### Composition over Inheritance
**❌ Violation:**
```python
class Vehicle:
    def start_engine(self): pass

class Car(Vehicle):
    def start_engine(self): return "Car engine started"

class ElectricCar(Car):
    def start_engine(self): raise Exception("No engine!")  # Problem!

class FlyingCar(Car):
    def fly(self): pass  # Jak dodać flying do Electric?

class ElectricFlyingCar(ElectricCar, FlyingCar):  # Multiple inheritance mess
    pass
```

**✅ Solution:**
```python
class Engine:
    def start(self): return "Engine started"

class ElectricMotor:
    def start(self): return "Motor started"

class FlightSystem:
    def fly(self): return "Flying"

class Vehicle:
    def __init__(self, propulsion):
        self.propulsion = propulsion  # Composition
    
    def start(self):
        return self.propulsion.start()

class Car(Vehicle):
    def __init__(self, propulsion, flight_system=None):
        super().__init__(propulsion)
        self.flight_system = flight_system  # Optional composition

# Easy combinations:
regular_car = Car(Engine())
electric_car = Car(ElectricMotor())  
flying_car = Car(Engine(), FlightSystem())
electric_flying_car = Car(ElectricMotor(), FlightSystem())
```

## 📋 File Format Templates

### README.md Template
```markdown
# [PRINCIPLE NAME] 

## [Principle 1]
**Definicja:** [One sentence definition]

**Dlaczego:** [Benefits]

**Kiedy łamiesz:** [When you violate it]

**Sprawdź w kodzie:** `violations.py` linia XX-XX
```

### violations.py Template
```python
"""
[SECTION NAME] - Code Violations
Znajdź problemy i zastanów się nad rozwiązaniami przed sprawdzeniem solutions.py
"""

# ============================================================================
# [PRINCIPLE NAME] VIOLATION
# ============================================================================
class ExampleClass:  # Line XX-XX: [Principle] violation
    # Code with clear violation
    # PROBLEM: [Explanation why this is bad]
```

### solutions.py Template
```python
"""
[SECTION NAME] - Clean Solutions
Porównaj z violations.py
"""

# ============================================================================
# [PRINCIPLE NAME] SOLUTION
# ============================================================================
class CleanExampleClass:  # Clean implementation
    # Solution code
```

### exercise.md Template
```markdown
# [SECTION] - Ćwiczenia Code Review

## Zadanie 1: [Principle] Violations (5 min)
1. Otwórz `violations.py` linie XX-XX
2. Zidentyfikuj [specific problems]
3. Zaproponuj [specific solution approach]
4. Sprawdź rozwiązanie w `solutions.py` linie XX-XX

## Zadanie 2: Refactoring Challenge (10 min)
Otrzymujesz ten kod:
```python
[Code to refactor]
```

**Zadanie:** [Specific refactoring instruction]
```