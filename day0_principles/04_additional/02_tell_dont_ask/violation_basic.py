"""BASIC: Tell Don't Ask Violation - tylko istota problemu"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount


class PaymentService:
    def transfer_money(self, account, amount):
        # PROBLEM: ASK about state, then manipulate it
        if account.get_balance() >= amount:  # ← ASK
            current = account.get_balance()  # ← ASK
            account.set_balance(current - amount)  # ← MANIPULATE
            return True
        return False


# PROBLEM: Business logic scattered, no encapsulation
# Kluczowy problem: Kod "wypytuje" obiekt o stan, potem nim manipuluje, zamiast powiedzieć, co ma zrobić.
