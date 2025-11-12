"""Strategie rabatów (OCP)"""
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, total): pass


class RegularCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        return total * 0.05


class PremiumCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        return total * 0.10


class VIPCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        return total * 0.15


class StudentCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        return total * 0.20
