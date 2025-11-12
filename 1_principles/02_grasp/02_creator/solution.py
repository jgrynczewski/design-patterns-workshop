"""
Creator Solution
Klasa która, zawiera, agreguje lub używa innych obiektów powinna je tworzyć
"""


class OrderItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price


class Order:  # Order zawiera items, więc Order tworzy OrderItem
    def __init__(self):
        self.items = []

    def add_item(self, product_id, quantity, price):  # Creator pattern
        item = OrderItem(product_id, quantity, price)  # Order tworzy OrderItem
        self.items.append(item)

    def get_total(self):
        return sum(item.price * item.quantity for item in self.items)


class OrderFactory:  # Factory ma za zadanie tworzyć Orders
    @staticmethod
    def create_order():
        return Order()  # Factory tworzy Order - to jego rola


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product_id, quantity, price):
        self.items.append({
            'product_id': product_id,
            'quantity': quantity,
            'price': price
        })

    def checkout(self):
        order = OrderFactory.create_order()  # Używa factory
        for item_data in self.items:
            order.add_item(  # Order sam tworzy swoje items
                item_data['product_id'],
                item_data['quantity'],
                item_data['price']
            )
        return order


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(1, 2, 50)
    cart.add_product(2, 1, 100)

    order = cart.checkout()
    print(f"Order total: ${order.get_total()}")
    print("✅ Order tworzy OrderItem (zawiera items)")
    print("✅ OrderFactory tworzy Order (to jego zadanie)")
