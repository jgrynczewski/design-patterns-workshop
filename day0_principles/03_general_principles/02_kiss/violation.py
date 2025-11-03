"""
KISS Violation - Keep It Simple, Stupid
Over-engineered solutions gdy proste wystarczyłyby
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, Any
from enum import Enum


class CalculationStrategy(ABC):
    """PROBLEM: Over-engineering dla prostego obliczenia"""

    @abstractmethod
    def execute(self, data: Dict[str, Any]) -> float:
        pass


class TotalCalculationStrategyFactory:
    """PROBLEM: Factory pattern dla... dodawania liczb"""

    def create_strategy(self, calculation_type: str) -> CalculationStrategy:
        if calculation_type == "simple_sum":
            return SimpleAdditionStrategy()
        elif calculation_type == "weighted_sum":
            return WeightedSumStrategy()
        else:
            raise ValueError("Unknown calculation strategy")


class SimpleAdditionStrategy(CalculationStrategy):
    def execute(self, data: Dict[str, Any]) -> float:
        return sum(data.get("items", []))


class WeightedSumStrategy(CalculationStrategy):
    def execute(self, data: Dict[str, Any]) -> float:
        items = data.get("items", [])
        weights = data.get("weights", [1] * len(items))
        return sum(item * weight for item, weight in zip(items, weights))


class ConfigurableCalculator:
    """PROBLEM: Klasa enterprise-level dla prostego dodawania"""

    def __init__(self, strategy_factory: TotalCalculationStrategyFactory):
        self.strategy_factory = strategy_factory
        self.configuration = {}
        self.metadata = {}

    def configure(self, config: Dict[str, Any]):
        self.configuration = config

    def calculate_with_complex_logic(self, items: List[float],
                                     calculation_type: str = "simple_sum",
                                     weights: Optional[List[float]] = None,
                                     precision: int = 2,
                                     validate_input: bool = True,
                                     store_metadata: bool = False) -> float:

        # PROBLEM: Niepotrzebna walidacja dla prostego przypadku
        if validate_input:
            if not items:
                raise ValueError("Items list cannot be empty")
            if any(not isinstance(item, (int, float)) for item in items):
                raise TypeError("All items must be numeric")
            if weights and len(weights) != len(items):
                raise ValueError("Weights must match items length")

        # PROBLEM: Skomplikowana logika dla prostego zadania
        strategy = self.strategy_factory.create_strategy(calculation_type)
        data = {"items": items}
        if weights:
            data["weights"] = weights

        result = strategy.execute(data)

        # PROBLEM: Niepotrzebne metadata tracking
        if store_metadata:
            self.metadata = {
                "last_calculation": calculation_type,
                "items_count": len(items),
                "result": result,
                "precision": precision
            }

        return round(result, precision)


class UserAuthenticationManager:
    """PROBLEM: Over-engineered authentication dla prostej aplikacji"""

    class AuthenticationResult(Enum):
        SUCCESS = "success"
        INVALID_CREDENTIALS = "invalid_credentials"
        USER_NOT_FOUND = "user_not_found"
        ACCOUNT_LOCKED = "account_locked"

    def __init__(self):
        self.users_database = {"admin": "password123", "user": "pass456"}
        self.failed_attempts = {}
        self.session_tokens = {}

    def authenticate_with_comprehensive_validation(
            self,
            username: str,
            password: str,
            track_attempts: bool = True,
            generate_session: bool = True,
            lockout_threshold: int = 3
    ) -> Dict[str, Union[str, bool, int]]:

        # PROBLEM: Skomplikowana logika tam gdzie wystarczy prosta
        if track_attempts:
            if username in self.failed_attempts:
                if self.failed_attempts[username] >= lockout_threshold:
                    return {
                        "status": self.AuthenticationResult.ACCOUNT_LOCKED.value,
                        "success": False,
                        "attempts_remaining": 0,
                        "session_token": None
                    }

        if username not in self.users_database:
            if track_attempts:
                self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            return {
                "status": self.AuthenticationResult.USER_NOT_FOUND.value,
                "success": False,
                "attempts_remaining": lockout_threshold - self.failed_attempts.get(username, 0),
                "session_token": None
            }

        if self.users_database[username] != password:
            if track_attempts:
                self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            return {
                "status": self.AuthenticationResult.INVALID_CREDENTIALS.value,
                "success": False,
                "attempts_remaining": lockout_threshold - self.failed_attempts.get(username, 0),
                "session_token": None
            }

        # Reset failed attempts on successful login
        if track_attempts and username in self.failed_attempts:
            del self.failed_attempts[username]

        session_token = None
        if generate_session:
            session_token = f"session_{username}_{hash(username + password)}"
            self.session_tokens[session_token] = username

        return {
            "status": self.AuthenticationResult.SUCCESS.value,
            "success": True,
            "attempts_remaining": lockout_threshold,
            "session_token": session_token
        }


if __name__ == "__main__":
    # Over-engineered calculator dla prostego dodawania
    factory = TotalCalculationStrategyFactory()
    calculator = ConfigurableCalculator(factory)

    # PROBLEM: 10 linii kodu żeby dodać [1, 2, 3, 4]
    result = calculator.calculate_with_complex_logic(
        items=[1, 2, 3, 4],
        calculation_type="simple_sum",
        validate_input=True,
        store_metadata=True
    )
    print(f"Sum of [1,2,3,4]: {result}")

    # Over-engineered authentication
    auth = UserAuthenticationManager()
    login_result = auth.authenticate_with_comprehensive_validation("admin", "password123")
    print(f"Login result: {login_result}")

    print("❌ Enterprise patterns dla prostych operacji")
    print("❌ 50 linii kodu tam gdzie wystarczy 5")
    print("❌ Abstrakcje które nie dodają wartości")
