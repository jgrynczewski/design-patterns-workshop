"""Hierarchia klientów (LSP)"""
from abc import ABC, abstractmethod


class Customer(ABC):
    @abstractmethod
    def get_discount_strategy(self): pass

    @abstractmethod
    def can_receive_discount(self): pass


class ActiveCustomer(Customer):
    def can_receive_discount(self):
        return True


class RegularCustomer(ActiveCustomer):
    def get_discount_strategy(self):
        from domain.discount import RegularCustomerDiscount
        return RegularCustomerDiscount()


class PremiumCustomer(ActiveCustomer):
    def get_discount_strategy(self):
        from domain.discount import PremiumCustomerDiscount
        return PremiumCustomerDiscount()


class VIPCustomer(ActiveCustomer):
    def get_discount_strategy(self):
        from domain.discount import VIPCustomerDiscount
        return VIPCustomerDiscount()


class BlockedCustomer(Customer):
    def get_discount_strategy(self):
        from domain.discount import RegularCustomerDiscount
        return RegularCustomerDiscount()

    def can_receive_discount(self):
        return False
