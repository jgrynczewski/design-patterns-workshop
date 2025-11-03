"""
Law of Demeter Solution - Delegacja i loose coupling
"""


class Address:
    def __init__(self, street, city, country, postal_code):
        self.street = street
        self.city = city
        self.country = country
        self.postal_code = postal_code

    def get_shipping_cost(self):
        """CLEAN: Address calculates its own shipping cost"""
        shipping_zone = self.city.get_shipping_zone()
        country_code = self.country.get_code()

        if country_code == "PL":
            if shipping_zone == "metro":
                return 5
            elif shipping_zone == "city":
                return 10
            else:
                return 15
        else:
            return 25

    def get_tax_rate(self):
        """CLEAN: Address delegates to country"""
        return self.country.get_tax_rate()

    def is_valid(self):
        """CLEAN: Address validates itself"""
        if not self.street or not self.city.get_name() or not self.country.get_name():
            return False

        return self.country.validate_postal_code(self.postal_code)

    def get_display_location(self):
        """CLEAN: Address formats its own display"""
        return f"{self.city.get_name()}, {self.country.get_name()}"


class City:
    def __init__(self, name, shipping_zone):
        self.name = name
        self.shipping_zone = shipping_zone

    def get_name(self):
        return self.name

    def get_shipping_zone(self):
        return self.shipping_zone


class Country:
    def __init__(self, name, code, tax_rate):
        self.name = name
        self.code = code
        self.tax_rate = tax_rate

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_tax_rate(self):
        return self.tax_rate

    def validate_postal_code(self, postal_code):
        """CLEAN: Country knows its own postal code rules"""
        if self.code == "PL":
            return len(postal_code) == 6 and postal_code.replace('-', '').isdigit()
        return len(postal_code) >= 3


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.loyalty_level = "standard"

    def get_shipping_cost(self):
        """CLEAN: Customer delegates to address"""
        return self.address.get_shipping_cost()

    def get_tax_rate(self):
        """CLEAN: Customer delegates to address"""
        return self.address.get_tax_rate()

    def get_email_domain(self):
        """CLEAN: Customer manages its own email logic"""
        domain = self.email.split('@')[1]

        if self.loyalty_level == "premium":
            return f"premium-{domain}"
        return domain

    def get_location(self):
        """CLEAN: Customer delegates to address"""
        return self.address.get_display_location()

    def has_valid_address(self):
        """CLEAN: Customer delegates to address"""
        return self.address.is_valid()


class OrderItems:
    def __init__(self):
        self.items = []
        self.subtotal = 0

    def get_subtotal(self):
        """CLEAN: Items manage their own total"""
        return self.subtotal

    def add_item(self, item):
        self.items.append(item)
        self.subtotal += item.price * item.quantity


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.status = "pending"

    def get_shipping_cost(self):
        """CLEAN: Order delegates to customer"""
        return self.customer.get_shipping_cost()

    def get_tax_amount(self):
        """CLEAN: Order calculates tax using delegated tax rate"""
        return self.items.get_subtotal() * self.customer.get_tax_rate()

    def get_total(self):
        """CLEAN: Order coordinates calculation without knowing details"""
        subtotal = self.items.get_subtotal()
        shipping = self.get_shipping_cost()
        tax = self.get_tax_amount()
        return subtotal + shipping + tax

    def is_valid(self):
        """CLEAN: Order delegates validation"""
        return self.customer.has_valid_address()


class OrderProcessor:
    """CLEAN: Simple coordination without violating Law of Demeter"""

    def process_order(self, order):
        if not order.is_valid():
            return False, "Invalid shipping address"

        total = order.get_total()
        return True, f"Order processed. Total: ${total}"


class ReportGenerator:
    """CLEAN: Uses delegated methods instead of deep property access"""

    def generate_customer_report(self, orders):
        for order in orders:
            customer_name = order.customer.name
            customer_location = order.customer.get_location()
            order_total = order.get_total()

            print(f"{customer_name} from {customer_location}: ${order_total}")

# BENEFITS:
# - Loose coupling - changes to internal structure don't break clients
# - Each object manages its own responsibilities
# - Easy to test individual components
# - Clear interfaces and delegation
# - Follows encapsulation principles
# - Code is maintainable and extensible
