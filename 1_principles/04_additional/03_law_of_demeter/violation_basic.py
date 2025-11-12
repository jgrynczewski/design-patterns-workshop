"""BASIC: Law of Demeter Violation - tylko istota problemu"""


class Order:
    def __init__(self, customer):
        self.customer = customer

    def get_shipping_cost(self):
        # PROBLEM: Chain of calls - violates Law of Demeter
        city = self.customer.address.city.name  # ← 3 dots!
        country = self.customer.address.country.code  # ← 3 dots!

        if country == "PL" and city == "Warsaw":
            return 10
        return 20


class OrderProcessor:
    def calculate_total(self, order):
        # PROBLEM: Knows too much about internal structure
        subtotal = order.items.total_price.amount  # ← 3 dots!
        shipping = order.customer.address.shipping_cost  # ← 3 dots!

        return subtotal + shipping

# PROBLEM: Tight coupling — any structure change breaks this code
# Kluczowy problem: Kod "przechodzi" przez strukturę obiektów (object.field.field.method)
# zamiast pytać o to, czego potrzebuje.
