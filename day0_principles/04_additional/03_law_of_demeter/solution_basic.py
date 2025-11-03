"""BASIC: Law of Demeter Solution - clean approach"""


class Order:
    def __init__(self, customer):
        self.customer = customer

    def get_shipping_cost(self):
        # CLEAN: Ask customer for what you need (delegation)
        return self.customer.get_shipping_cost()  # ← 1 dot!

    def get_total_price(self):
        # CLEAN: Ask items for their total
        return self.items.get_total()  # ← 1 dot!


class Customer:
    def get_shipping_cost(self):
        # CLEAN: Customer delegates to address
        return self.address.calculate_shipping()  # ← 1 dot!


class OrderProcessor:
    def calculate_total(self, order):
        # CLEAN: Simple delegation, no knowledge of internal structure
        subtotal = order.get_total_price()  # ← 1 dot!
        shipping = order.get_shipping_cost()  # ← 1 dot!

        return subtotal + shipping

# RESULT: Loose coupling, easy to change internal structure
# Kluczowa korzyść: Każdy obiekt deleguje odpowiedzialność zamiast ekspozować wewnętrzną strukturę.
# Jedna kropka wszędzie!
