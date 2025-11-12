"""
Law of Demeter Violation - Łańcuchy wywołań i tight coupling
"""


class Address:
    def __init__(self, street, city, country, postal_code):
        self.street = street
        self.city = city
        self.country = country
        self.postal_code = postal_code


class City:
    def __init__(self, name, shipping_zone):
        self.name = name
        self.shipping_zone = shipping_zone


class Country:
    def __init__(self, name, code, tax_rate):
        self.name = name
        self.code = code
        self.tax_rate = tax_rate


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.loyalty_level = "standard"


class OrderItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price


class OrderItems:
    def __init__(self):
        self.items = []
        self.subtotal = 0


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.status = "pending"


class OrderProcessor:
    """PROBLEM: Violates Law of Demeter throughout"""

    def calculate_shipping(self, order):
        # PROBLEM: Deep chain of calls - knows too much about structure
        city_name = order.customer.address.city.name
        shipping_zone = order.customer.address.city.shipping_zone
        country_code = order.customer.address.country.code

        # PROBLEM: Accessing nested properties
        if country_code == "PL":
            if shipping_zone == "metro":
                return 5
            elif shipping_zone == "city":
                return 10
            else:
                return 15
        else:
            return 25

    def calculate_tax(self, order):
        # PROBLEM: Multiple dot accesses
        tax_rate = order.customer.address.country.tax_rate
        subtotal = order.items.subtotal

        return subtotal * tax_rate

    def get_customer_email_domain(self, order):
        # PROBLEM: Chain of property access
        email = order.customer.email
        domain = email.split('@')[1]

        # PROBLEM: Accessing nested customer properties for business logic
        if order.customer.loyalty_level == "premium":
            return f"premium-{domain}"
        return domain

    def validate_shipping_address(self, order):
        # PROBLEM: Knowledge of deep object structure
        street = order.customer.address.street
        city = order.customer.address.city.name
        country = order.customer.address.country.name
        postal = order.customer.address.postal_code

        # Complex validation logic based on nested properties
        if not street or not city or not country:
            return False

        # PROBLEM: Business logic scattered, depends on internal structure
        if order.customer.address.country.code == "PL":
            return len(postal) == 6 and postal.replace('-', '').isdigit()

        return len(postal) >= 3


class ReportGenerator:
    """PROBLEM: Another class violating Law of Demeter"""

    def generate_customer_report(self, orders):
        # PROBLEM: Multiple classes accessing deep object structures
        for order in orders:
            customer_name = order.customer.name
            customer_city = order.customer.address.city.name
            customer_country = order.customer.address.country.name
            order_total = order.items.subtotal

            # PROBLEM: If any part of the object structure changes,
            # this code breaks
            print(f"{customer_name} from {customer_city}, {customer_country}: ${order_total}")

# PROBLEMS:
# - Changes to Address, City, or Country structure break multiple classes
# - OrderProcessor knows too much about Customer internal structure
# - Tight coupling between classes
# - Difficult to test individual components
# - Violates encapsulation - exposes implementation details
# - Code is fragile and hard to maintain
