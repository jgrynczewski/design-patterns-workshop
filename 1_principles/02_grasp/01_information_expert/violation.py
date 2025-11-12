"""
Information Expert Violation
Klasa, która nie ma informacji potrzebnych do wykonania operacji
"""


class Order:
    def __init__(self):
        self.items = []


class OrderItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class OrderService:  # PROBLEM: Nie ma bezpośredniego dostępu do items
    def calculate_total(self, order):
        total = 0
        for item in order.items:  # Musi "zagłębiać się" w Order
            total += item.price * item.quantity
        return total

    def get_item_count(self, order):
        return len(order.items)  # Znów musi znać wewnętrzną strukturę


if __name__ == "__main__":
    order = Order()
    order.items.append(OrderItem("Laptop", 1000, 1))
    order.items.append(OrderItem("Mouse", 50, 2))

    service = OrderService()
    print(f"Total: ${service.calculate_total(order)}")
    print("❌ OrderService musi znać wewnętrzną strukturę Order")
