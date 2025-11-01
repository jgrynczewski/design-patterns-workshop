# %% About
# - Name: Facade - Order Processing System
# - Difficulty: easy
# - Lines: 12
# - Minutes: 10
# - Focus: Facade pattern - simplifying complex subsystems

# %% Description
"""
Implementuj wzorzec Facade do uproszczenia złożonego systemu
składania zamówień e-commerce.

Zadanie: Stwórz prosty interfejs dla skomplikowanego procesu zamówienia
"""

# %% Hints
# - Facade enkapsuluje wywołania do wielu podsystemów
# - Wywołuj podsystemy w kolejności: Inventory → Payment → Shipping → Notification
# - Obsłuż błędy i rollback dla failed operations
# - Zwróć strukturalny result dict

# %% Doctests
"""
>>> # Test pomyślnego zamówienia
>>> facade = OrderFacade()
>>> customer = {"name": "Jan Kowalski", "email": "jan@example.com"}
>>> items = [{"name": "Laptop", "price": 1000, "quantity": 1}]
>>> result = facade.place_order(customer, items)
>>> result["success"]
True
>>> len(result["order_id"]) > 0
True

>>> # Test zamówienia bez stock
>>> items_out_of_stock = [{"name": "Rare Item", "price": 2000, "quantity": 10}]
>>> result = facade.place_order(customer, items_out_of_stock)
>>> result["success"]
False
>>> "stock" in result["message"].lower()
True
"""

# %% Imports
import uuid
from typing import List, Dict, Any


# %% Complex Subsystems (już gotowe - nie modyfikuj)

class InventoryService:
    """Podsystem zarządzania magazynem"""

    def __init__(self):
        self.stock = {
            "Laptop": 5,
            "Phone": 10,
            "Tablet": 3,
            "Monitor": 7
        }

    def check_stock(self, items: List[Dict]) -> bool:
        """Sprawdź dostępność produktów"""
        for item in items:
            available = self.stock.get(item["name"], 0)
            if available < item["quantity"]:
                return False
        return True

    def reserve_items(self, items: List[Dict]) -> bool:
        """Zarezerwuj produkty (zmniejsz stock)"""
        if not self.check_stock(items):
            return False

        for item in items:
            self.stock[item["name"]] -= item["quantity"]
        return True


class PaymentService:
    """Podsystem przetwarzania płatności"""

    def process_payment(self, customer: Dict, amount: float) -> Dict:
        """Przetwórz płatność"""
        # Symulacja: płatność fails dla kwot > 5000
        if amount > 5000:
            return {"success": False, "transaction_id": None}

        transaction_id = f"TXN_{uuid.uuid4().hex[:8].upper()}"
        return {"success": True, "transaction_id": transaction_id}

    def refund_payment(self, transaction_id: str) -> bool:
        """Zwróć pieniądze (rollback)"""
        return transaction_id is not None


class ShippingService:
    """Podsystem organizacji dostaw"""

    def arrange_delivery(self, customer: Dict, items: List[Dict]) -> Dict:
        """Zorganizuj dostawę"""
        # Symulacja: shipping fails dla > 5 items
        total_quantity = sum(item["quantity"] for item in items)
        if total_quantity > 5:
            return {"success": False, "tracking_number": None}

        tracking_number = f"TRACK_{uuid.uuid4().hex[:8].upper()}"
        return {"success": True, "tracking_number": tracking_number}


class NotificationService:
    """Podsystem powiadomień"""

    def send_confirmation(self, customer: Dict, order_details: Dict) -> bool:
        """Wyślij potwierdzenie zamówienia"""
        # Symulacja: zawsze sukces
        return True


# %% TODO: Implement OrderFacade

class OrderFacade:
    """Facade upraszczający proces składania zamówień"""

    def __init__(self):
        """Inicjalizuj facade z wszystkimi podsystemami"""
        # TODO: Stwórz instancje wszystkich podsystemów
        # self.inventory = ...
        # self.payment = ...
        # self.shipping = ...
        # self.notifications = ...
        pass

    def place_order(self, customer: Dict, items: List[Dict]) -> Dict[str, Any]:
        """
        Złóż zamówienie - główny interfejs Facade

        Args:
            customer: {"name": str, "email": str}
            items: [{"name": str, "price": float, "quantity": int}]

        Returns:
            {"success": bool, "order_id": str, "message": str}
        """
        order_id = f"ORDER_{uuid.uuid4().hex[:8].upper()}"

        try:
            # TODO: Krok 1 - Sprawdź dostępność w magazynie
            # if not self.inventory.check_stock(items):
            #     return {"success": False, "order_id": "", "message": "Items out of stock"}

            # TODO: Krok 2 - Zarezerwuj produkty
            # if not self.inventory.reserve_items(items):
            #     return {"success": False, "order_id": "", "message": "Could not reserve items"}

            # TODO: Krok 3 - Przetwórz płatność
            # total_amount = sum(item["price"] * item["quantity"] for item in items)
            # payment_result = self.payment.process_payment(customer, total_amount)
            # if not payment_result["success"]:
            #     # Rollback: zwróć items do stock (opcjonalne)
            #     return {"success": False, "order_id": "", "message": "Payment failed"}

            # TODO: Krok 4 - Zorganizuj dostawę
            # shipping_result = self.shipping.arrange_delivery(customer, items)
            # if not shipping_result["success"]:
            #     # Rollback: zwróć pieniądze
            #     self.payment.refund_payment(payment_result["transaction_id"])
            #     return {"success": False, "order_id": "", "message": "Shipping unavailable"}

            # TODO: Krok 5 - Wyślij potwierdzenie
            # order_details = {
            #     "order_id": order_id,
            #     "items": items,
            #     "total": total_amount,
            #     "tracking": shipping_result["tracking_number"]
            # }
            # self.notifications.send_confirmation(customer, order_details)

            # TODO: Zwróć sukces
            # return {
            #     "success": True,
            #     "order_id": order_id,
            #     "message": f"Order placed successfully. Tracking: {shipping_result['tracking_number']}"
            # }

            pass  # Usuń to gdy zaimplementujesz

        except Exception as e:
            # Obsługa nieoczekiwanych błędów
            return {
                "success": False,
                "order_id": "",
                "message": f"Order processing failed: {str(e)}"
            }

    def get_order_status(self, order_id: str) -> Dict[str, Any]:
        """Pobierz status zamówienia (opcjonalne rozszerzenie)"""
        # TODO (Opcjonalne): Zaimplementuj jeśli masz czas
        pass


# %% Helper Functions (Optional)

def calculate_total(items: List[Dict]) -> float:
    """Oblicz łączną wartość zamówienia"""
    # TODO (Opcjonalne): Zaimplementuj helper function
    pass
