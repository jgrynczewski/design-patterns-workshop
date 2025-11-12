"""
Creator Violation
Klasa tworzy obiekty, z którymi nie ma bezpośredniej relacji
"""


class OrderItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class OrderManager:  # PROBLEM: Nie ma bezpośredniej relacji z OrderItem
    def add_item_to_order(self, order, product_id, quantity, price):
        item = OrderItem(product_id, quantity, price)  # Kto powinien tworzyć?
        order.add_item(item)


class ShoppingCart:  # PROBLEM: Tworzy Order, ale nie zarządza zamówieniami
    def __init__(self):
        self.items = []

    def checkout(self):
        order = Order()  # ShoppingCart tworzy Order — czy to właściwe?
        for item_data in self.items:
            item = OrderItem(item_data['id'], item_data['qty'], item_data['price'])
            order.add_item(item)
        return order


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.items.append({'id': 1, 'qty': 2, 'price': 50})

    manager = OrderManager()
    order = Order()
    manager.add_item_to_order(order, 2, 1, 100)

    print("❌ OrderManager tworzy OrderItem, ale Order zawiera items")
    print("❌ ShoppingCart tworzy Order, ale nie zarządza zamówieniami")
