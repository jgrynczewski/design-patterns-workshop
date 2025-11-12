"""
Testy dla Intro - Simple Calculator
"""

import pytest
from starter import add, multiply


class TestCalculator:
    """Testy prostego kalkulatora"""

    def test_add_positive_numbers(self):
        """Test dodawania liczb dodatnich"""
        assert add(2, 3) == 5
        assert add(10, 5) == 15

    def test_add_zero(self):
        """Test dodawania zera"""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_add_negative_numbers(self):
        """Test dodawania liczb ujemnych"""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2
        assert add(5, -3) == 2

    def test_multiply_positive_numbers(self):
        """Test mnożenia liczb dodatnich"""
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50

    def test_multiply_by_zero(self):
        """Test mnożenia przez zero"""
        assert multiply(0, 0) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_multiply_by_one(self):
        """Test mnożenia przez jeden"""
        assert multiply(1, 1) == 1
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5

    def test_multiply_negative_numbers(self):
        """Test mnożenia liczb ujemnych"""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6
        assert multiply(2, -3) == -6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
