"""
Tell Don't Ask Violation - Manipulacja stanu obiektów z zewnątrz
"""


class BankAccount:
    def __init__(self, balance, account_type="standard"):
        self.balance = balance
        self.account_type = account_type
        self.is_frozen = False
        self.daily_withdrawal_limit = 1000
        self.daily_withdrawn = 0

    # PROBLEM: Exposing internal state through getters/setters
    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount

    def get_account_type(self):
        return self.account_type

    def is_account_frozen(self):
        return self.is_frozen

    def get_daily_withdrawn(self):
        return self.daily_withdrawn

    def set_daily_withdrawn(self, amount):
        self.daily_withdrawn = amount

    def get_daily_limit(self):
        return self.daily_withdrawal_limit


class PaymentService:
    """PROBLEM: Business logic scattered across multiple classes"""

    def transfer_money(self, from_account, to_account, amount):
        # PROBLEM: ASK about state, then manipulate it

        # Check if account is frozen
        if from_account.is_account_frozen():
            return False, "Account is frozen"

        # Check balance
        if from_account.get_balance() < amount:
            return False, "Insufficient funds"

        # Check daily limit
        current_withdrawn = from_account.get_daily_withdrawn()
        daily_limit = from_account.get_daily_limit()
        if current_withdrawn + amount > daily_limit:
            return False, "Daily limit exceeded"

        # Premium accounts have higher limits
        if from_account.get_account_type() == "premium":
            if current_withdrawn + amount > daily_limit * 2:
                return False, "Premium daily limit exceeded"

        # Perform transfer - manipulating state directly
        new_balance = from_account.get_balance() - amount
        from_account.set_balance(new_balance)

        new_withdrawn = from_account.get_daily_withdrawn() + amount
        from_account.set_daily_withdrawn(new_withdrawn)

        # Update recipient
        to_balance = to_account.get_balance() + amount
        to_account.set_balance(to_balance)

        return True, "Transfer successful"


class LoanService:
    """PROBLEM: Duplicate validation logic"""

    def approve_loan(self, account, loan_amount):
        # PROBLEM: Same validation logic as PaymentService
        if account.is_account_frozen():
            return False

        if account.get_balance() < loan_amount * 0.1:  # 10% down payment
            return False

        if account.get_account_type() == "premium":
            # Different business rules, but same state access pattern
            return account.get_balance() >= loan_amount * 0.05

        return True

# PROBLEMS:
# - Business logic scattered across multiple classes
# - Account validation duplicated everywhere
# - Account state can be manipulated incorrectly
# - No single source of truth for business rules
# - Hard to maintain and test individual rules
