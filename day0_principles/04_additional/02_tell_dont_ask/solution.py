"""
Tell Don't Ask Solution - Enkapsulacja stanu i zachowania
"""


class BankAccount:
    """CLEAN: Object manages its own state and business rules"""

    def __init__(self, balance, account_type="standard"):
        self.balance = balance
        self.account_type = account_type
        self.is_frozen = False
        self.daily_withdrawal_limit = 1000 if account_type == "standard" else 2000
        self.daily_withdrawn = 0

    def withdraw(self, amount):
        """TELL: Single method for all withdrawal logic"""
        if self._cannot_withdraw(amount):
            return False, self._get_withdrawal_error(amount)

        self.balance -= amount
        self.daily_withdrawn += amount
        return True, "Withdrawal successful"

    def deposit(self, amount):
        """TELL: Simple deposit operation"""
        if amount <= 0:
            return False, "Invalid amount"

        self.balance += amount
        return True, "Deposit successful"

    def can_get_loan(self, loan_amount):
        """TELL: Loan eligibility encapsulated"""
        if self.is_frozen:
            return False

        required_down_payment = 0.05 if self.account_type == "premium" else 0.1
        return self.balance >= loan_amount * required_down_payment

    def freeze_account(self):
        """TELL: Account management"""
        self.is_frozen = True

    def unfreeze_account(self):
        """TELL: Account management"""
        self.is_frozen = False

    def reset_daily_limit(self):
        """TELL: Daily operations"""
        self.daily_withdrawn = 0

    # Private methods - encapsulation helpers
    def _cannot_withdraw(self, amount):
        return (self.is_frozen or
                self.balance < amount or
                self._exceeds_daily_limit(amount))

    def _exceeds_daily_limit(self, amount):
        return self.daily_withdrawn + amount > self.daily_withdrawal_limit

    def _get_withdrawal_error(self, amount):
        if self.is_frozen:
            return "Account is frozen"
        if self.balance < amount:
            return "Insufficient funds"
        if self._exceeds_daily_limit(amount):
            return "Daily limit exceeded"
        return "Unknown error"


class PaymentService:
    """CLEAN: Service just tells objects what to do"""

    def transfer_money(self, from_account, to_account, amount):
        # TELL: Just instruct objects what to do
        withdrawal_success, withdrawal_message = from_account.withdraw(amount)

        if not withdrawal_success:
            return False, withdrawal_message

        deposit_success, deposit_message = to_account.deposit(amount)

        if not deposit_success:
            # Rollback withdrawal if deposit fails
            from_account.deposit(amount)
            return False, f"Transfer failed: {deposit_message}"

        return True, "Transfer successful"


class LoanService:
    """CLEAN: Simple delegation to account logic"""

    def approve_loan(self, account, loan_amount):
        # TELL: Ask account if it can handle the loan
        if account.can_get_loan(loan_amount):
            return True, "Loan approved"
        else:
            return False, "Loan denied"


class AccountManager:
    """CLEAN: High-level account operations"""

    def daily_reset(self, accounts):
        # TELL: Reset daily limits for all accounts
        for account in accounts:
            account.reset_daily_limit()

    def freeze_suspicious_accounts(self, accounts, suspicious_ids):
        # TELL: Freeze accounts by ID
        for account in accounts:
            if id(account) in suspicious_ids:
                account.freeze_account()

# BENEFITS:
# - Business logic encapsulated in domain objects
# - No duplicate validation logic
# - Clear interfaces and responsibilities
# - Easy to test individual business rules
# - Objects protect their own invariants
# - Services just coordinate, don't manipulate state
