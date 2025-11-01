"""Interfejsy dla warstwy persistencji"""
from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def save_order(self, order_data): pass
