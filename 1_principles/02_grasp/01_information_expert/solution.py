"""
Information Expert Solution
Klasa, która ma informacje wykonuje operacje
"""


class OrderItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):  # Item ma informacje o sobie
        return self.price * self.quantity


class Order:  # Order ma items, więc Order oblicza total
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):  # Expert - Order ma items
        return sum(item.get_total_price() for item in self.items)

    def get_item_count(self):  # Expert - Order zna swoje items
        return len(self.items)

    def get_most_expensive_item(self):  # Expert - Order może analizować items
        if not self.items:
            return None
        return max(self.items, key=lambda item: item.price)


if __name__ == "__main__":
    order = Order()
    order.add_item(OrderItem("Laptop", 1000, 1))
    order.add_item(OrderItem("Mouse", 50, 2))

    print(f"Total: ${order.calculate_total()}")
    print(f"Items: {order.get_item_count()}")
    print("✅ Order ma informacje, więc Order wykonuje operacje")
