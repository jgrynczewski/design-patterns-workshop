# %% About
# - Name: Chain of Responsibility - Approval Chain
# - Difficulty: medium
# - Lines: 20
# - Minutes: 15
# - Focus: Chain of Responsibility pattern - passing requests through handler chain

# %% Description
"""
Implementuj wzorzec Chain of Responsibility do systemu akceptacji
wydatków w workflow system.

Zadanie: Stwórz łańcuch handlers z różnymi limitami autoryzacji
"""

# %% Hints
# - ApprovalHandler ma abstract method handle_request()
# - Każdy handler sprawdza czy może obsłużyć request
# - Jeśli nie może - przekazuje do next_handler
# - ExpenseRequest zawiera kwotę, opis i priorytet

# %% Doctests
"""
>>> # Test podstawowego approval chain
>>> team_lead = TeamLeadApprover()
>>> manager = ManagerApprover()
>>> team_lead.set_next(manager)
<class 'starter.ManagerApprover'>

>>> # Test małej kwoty (team lead approval)
>>> small_expense = ExpenseRequest(500, "Office supplies", Priority.LOW)
>>> result = team_lead.handle_request(small_expense)
>>> result.approved
True
>>> result.approved_by
'Team Lead'

>>> # Test większej kwoty (manager approval)
>>> big_expense = ExpenseRequest(3000, "New laptop", Priority.MEDIUM)
>>> result = team_lead.handle_request(big_expense)
>>> result.approved
True
>>> result.approved_by
'Manager'

>>> # Test rejection
>>> huge_expense = ExpenseRequest(100000, "Company jet", Priority.LOW)
>>> manager_only = ManagerApprover()  # Bez CEO w łańcuchu
>>> result = manager_only.handle_request(huge_expense)
>>> result.approved
False
"""

# %% Imports
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List
from datetime import datetime


# %% Priority Enum (już gotowe)

class Priority(Enum):
    """Priorytety requests"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


# %% ExpenseRequest Class (już gotowe)

class ExpenseRequest:
    """Request wydatku do zatwierdzenia"""

    def __init__(self, amount: float, description: str, priority: Priority):
        """Inicjalizuj request wydatku"""
        self.amount = amount
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.request_id = f"EXP_{int(self.created_at.timestamp())}"

    def __str__(self):
        return f"Expense {self.request_id}: {self.amount} PLN - {self.description}"


# %% ApprovalResult Class (już gotowe)

class ApprovalResult:
    """Wynik procesu zatwierdzania"""

    def __init__(self, approved: bool, approved_by: str = "", reason: str = ""):
        """Inicjalizuj wynik zatwierdzania"""
        self.approved = approved
        self.approved_by = approved_by
        self.reason = reason
        self.processed_at = datetime.now()
        self.approval_chain = []  # Lista wszystkich handlers, które przetworzyły request


# %% TODO: Implement ApprovalHandler Abstract Class

class ApprovalHandler(ABC):
    """Abstract base class dla handlers zatwierdzania"""

    def __init__(self, name: str, approval_limit: float):
        """Inicjalizuj handler z nazwą i limitem"""
        # TODO:
        # self.name = name
        # self.approval_limit = approval_limit
        # self._next_handler = None
        # self.processed_requests = []  # Historia przetworzonych requests
        pass

    def set_next(self, handler: 'ApprovalHandler') -> 'ApprovalHandler':
        """Ustaw następny handler w łańcuchu"""
        # TODO:
        # self._next_handler = handler
        # return handler  # Pozwala na fluent interface
        pass

    def handle_request(self, request: ExpenseRequest) -> ApprovalResult:
        """Template method dla obsługi request"""
        # TODO:
        # 1. Dodaj request do processed_requests
        # 2. Sprawdź czy może obsłużyć (can_handle)
        # 3. Jeśli tak - wywołaj process_request
        # 4. Jeśli nie i jest next_handler - przekaż dalej
        # 5. Jeśli nie ma next_handler - zwróć rejection
        pass

    @abstractmethod
    def can_handle(self, request: ExpenseRequest) -> bool:
        """Sprawdź czy handler może obsłużyć request"""
        pass

    @abstractmethod
    def process_request(self, request: ExpenseRequest) -> ApprovalResult:
        """Przetworz request (primitive operation)"""
        pass

    def get_processing_stats(self) -> dict:
        """Zwróć statystyki przetwarzania"""
        # TODO: Zwróć dict z:
        # - "total_processed": liczba przetworzonych requests
        # - "approved_count": liczba zatwierdzonych
        # - "handler_name": nazwa handler'a
        # - "approval_limit": limit zatwierdzania
        pass


# %% TODO: Implement Concrete Handlers

class TeamLeadApprover:
    """Handler dla Team Lead - limit 1000 PLN"""

    def __init__(self):
        """Inicjalizuj Team Lead approver"""
        # TODO: super().__init__("Team Lead", 1000.0)
        pass

    def can_handle(self, request: ExpenseRequest) -> bool:
        """Team Lead może zatwierdzić do 1000 PLN"""
        # TODO: Sprawdź czy amount <= approval_limit
        pass

    def process_request(self, request: ExpenseRequest) -> ApprovalResult:
        """Przetworz request przez Team Lead"""
        # TODO:
        # 1. Sprawdź dodatkowe warunki (np. priorytet LOW/MEDIUM)
        # 2. Zatwierdź jeśli warunki spełnione
        # 3. Zwróć ApprovalResult z approved=True/False, approved_by=self.name, reason
        pass


class ManagerApprover:
    """Handler dla Manager - limit 5000 PLN"""

    def __init__(self):
        """Inicjalizuj Manager approver"""
        # TODO: super().__init__("Manager", 5000.0)
        pass

    def can_handle(self, request: ExpenseRequest) -> bool:
        """Manager może zatwierdzić do 5000 PLN"""
        # TODO: Sprawdź czy amount <= approval_limit
        pass

    def process_request(self, request: ExpenseRequest) -> ApprovalResult:
        """Przetworz request przez Manager"""
        # TODO:
        # 1. Manager zatwierdza wszystkie priorytety
        # 2. Zatwierdź jeśli kwota w limicie
        # 3. Zwróć ApprovalResult
        pass


class DirectorApprover:
    """Handler dla Director - limit 25000 PLN"""

    def __init__(self):
        """Inicjalizuj Director approver"""
        # TODO: super().__init__("Director", 25000.0)
        pass

    def can_handle(self, request: ExpenseRequest) -> bool:
        """Director może zatwierdzić do 25000 PLN"""
        # TODO: Sprawdź czy amount <= approval_limit
        pass

    def process_request(self, request: ExpenseRequest) -> ApprovalResult:
        """Przetworz request przez Director"""
        # TODO:
        # 1. Director wymaga HIGH lub URGENT priority dla kwot > 10000
        # 2. Zatwierdź jeśli warunki spełnione
        # 3. Zwróć ApprovalResult
        pass


class CEOApprover:
    """Handler dla CEO - bez limitu"""

    def __init__(self):
        """Inicjalizuj CEO approver"""
        # TODO: super().__init__("CEO", float('inf'))
        pass

    def can_handle(self, request: ExpenseRequest) -> bool:
        """CEO może zatwierdzić wszystko"""
        # TODO: return True (CEO nie ma limitów)
        pass

    def process_request(self, request: ExpenseRequest) -> ApprovalResult:
        """Przetworz request przez CEO"""
        # TODO:
        # 1. CEO zatwierdza wszystko z priorytetem URGENT
        # 2. Dla innych priorytetów może odrzucić jeśli kwota > 50000
        # 3. Zwróć ApprovalResult
        pass


# %% TODO: Implement Chain Builder

class ApprovalChainBuilder:
    """Builder dla łańcucha zatwierdzania"""

    def __init__(self):
        """Inicjalizuj builder"""
        # TODO: self.handlers = []
        pass

    def add_team_lead(self) -> 'ApprovalChainBuilder':
        """Dodaj team lead do łańcucha"""
        # TODO:
        # self.handlers.append(TeamLeadApprover())
        # return self
        pass

    def add_manager(self) -> 'ApprovalChainBuilder':
        """Dodaj manager do łańcucha"""
        # TODO:
        # self.handlers.append(ManagerApprover())
        # return self
        pass

    def add_director(self) -> 'ApprovalChainBuilder':
        """Dodaj director do łańcucha"""
        # TODO:
        # self.handlers.append(DirectorApprover())
        # return self
        pass

    def add_ceo(self) -> 'ApprovalChainBuilder':
        """Dodaj CEO do łańcucha"""
        # TODO:
        # self.handlers.append(CEOApprover())
        # return self
        pass

    def build(self) -> Optional[ApprovalHandler]:
        """Zbuduj łańcuch handlers"""
        # TODO:
        # 1. Jeśli brak handlers - zwróć None
        # 2. Połącz handlers w łańcuch (set_next)
        # 3. Zwróć pierwszy handler
        pass


# %% Example Usage (Optional)

def demonstrate_approval_chain():
    """Demonstracja łańcucha zatwierdzania"""
    # TODO (Opcjonalne):
    # 1. Stwórz różne requests o różnych kwotach
    # 2. Zbuduj pełny łańcuch approval
    # 3. Przetestuj różne scenariusze
    # 4. Pokaż statystyki każdego handler'a
    # 5. Zwróć wyniki
    pass
