"""Interfejsy dla warstwy komunikacji"""
from abc import ABC, abstractmethod


class EmailInterface(ABC):
    @abstractmethod
    def send_email(self, email, message): pass
