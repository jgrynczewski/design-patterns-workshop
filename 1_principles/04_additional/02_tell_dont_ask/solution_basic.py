"""BASIC: Tell Don't Ask Solution - clean approach"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        # TELL: Object manages its own state and validation
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class PaymentService:
    def transfer_money(self, account, amount):
        # TELL: Just tell the object what to do
        return account.withdraw(amount)

# RESULT: Encapsulation, validation in one place, clear intent
# Kluczowa korzyść: Obiekt BankAccount sam zarządza swoim stanem i walidacją. PaymentService tylko mówi, co ma się stać.
