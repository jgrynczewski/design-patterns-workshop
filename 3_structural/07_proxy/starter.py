# %% About
# - Name: Proxy - Product Caching System
# - Difficulty: easy
# - Lines: 15
# - Minutes: 12
# - Focus: Proxy pattern - controlling access with caching

# %% Description
"""
Implementuj wzorzec Proxy do cache'owania kosztownych operacji
ładowania produktów bez zmiany kodu klienta.

Zadanie: Stwórz proxy z cache'owaniem dla ProductService
"""

# %% Hints
# - Proxy implementuje ten sam interface co RealService
# - Cache jako dict: {product_id: product_data}
# - Lazy initialization: stwórz real_service tylko gdy potrzeba
# - Loguj cache hits/misses dla monitoringu

# %% Doctests
"""
>>> # Test basic functionality
>>> proxy = ProductServiceProxy()
>>> product = proxy.get_product_details("PROD001")
>>> product["name"]
'Gaming Laptop'
>>> product["price"]
1500.0

>>> # Test cache hit (drugi raz ten sam produkt)
>>> product2 = proxy.get_product_details("PROD001")
>>> product2["name"]
'Gaming Laptop'

>>> # Test cache statistics
>>> stats = proxy.get_cache_stats()
>>> stats["hits"] >= 1
True
>>> stats["misses"] >= 1  
True
"""

# %% Imports
from abc import ABC, abstractmethod
import time
from typing import Dict, Any


# %% TODO: Implement ProductService Interface

class ProductService(ABC):
    """Interface dla serwisu produktów"""

    @abstractmethod
    def get_product_details(self, product_id: str) -> Dict[str, Any]:
        """Pobierz szczegóły produktu po ID"""
        pass


# %% TODO: Implement RealProductService (Subject)

class RealProductService:
    """Prawdziwy serwis produktów - symuluje wolne API/DB"""

    def __init__(self):
        """Inicjalizuj serwis z przykładowymi danymi"""
        # TODO: Stwórz słownik z przykładowymi produktami
        # self.products = {
        #     "PROD001": {"name": "Gaming Laptop", "price": 1500.0, "category": "Electronics"},
        #     "PROD002": {"name": "Wireless Mouse", "price": 25.0, "category": "Accessories"},
        #     "PROD003": {"name": "4K Monitor", "price": 400.0, "category": "Displays"},
        #     ...
        # }
        pass

    def get_product_details(self, product_id: str) -> Dict[str, Any]:
        """Pobierz szczegóły produktu (symuluje wolne API call)"""
        # TODO:
        # 1. Symuluj delay: time.sleep(0.5)  # 500ms delay
        # 2. Sprawdź czy product_id istnieje w self.products
        # 3. Jeśli tak, zwróć dane produktu
        # 4. Jeśli nie, zwróć None lub rzuć wyjątek
        pass


# %% TODO: Implement ProductServiceProxy

class ProductServiceProxy:
    """Proxy z cache'owaniem dla ProductService"""

    def __init__(self):
        """Inicjalizuj proxy"""
        # TODO:
        # self.real_service = None  # Lazy initialization
        # self.cache = {}  # Cache: {product_id: product_data}
        # self.cache_hits = 0
        # self.cache_misses = 0
        pass

    def get_product_details(self, product_id: str) -> Dict[str, Any]:
        """Pobierz szczegóły produktu z cache lub real service"""
        # TODO:
        # 1. Sprawdź czy produkt jest w cache
        # 2. Jeśli tak: increment cache_hits, zwróć z cache
        # 3. Jeśli nie:
        #    - Stwórz real_service jeśli nie istnieje (lazy init)
        #    - Pobierz dane z real_service
        #    - Zapisz w cache
        #    - Increment cache_misses
        #    - Zwróć dane
        pass

    def _get_real_service(self) -> RealProductService:
        """Lazy initialization prawdziwego serwisu"""
        # TODO:
        # if self.real_service is None:
        #     self.real_service = RealProductService()
        # return self.real_service
        pass

    def get_cache_stats(self) -> Dict[str, Any]:
        """Zwróć statystyki cache"""
        # TODO: Zwróć słownik z:
        # - "hits": liczba cache hits
        # - "misses": liczba cache misses
        # - "hit_rate": procent hits (hits / (hits + misses))
        # - "cached_items": liczba elementów w cache
        pass

    def clear_cache(self) -> None:
        """Wyczyść cache"""
        # TODO:
        # 1. Wyczyść self.cache
        # 2. Zresetuj cache_hits i cache_misses do 0
        pass

    def is_cached(self, product_id: str) -> bool:
        """Sprawdź czy produkt jest w cache"""
        # TODO: Zwróć czy product_id jest w self.cache
        pass


# %% Performance Testing Helper (Optional)

def measure_performance_improvement():
    """Zmierz poprawę wydajności z proxy vs bez proxy"""
    # TODO (Opcjonalne):
    # 1. Stwórz RealProductService i ProductServiceProxy
    # 2. Zmierz czas 10 wywołań tego samego produktu bez cache
    # 3. Zmierz czas 10 wywołań tego samego produktu z cache
    # 4. Zwróć dict z wynikami: {"without_cache": time1, "with_cache": time2, "improvement": "%"}
    pass


# %% Cache Statistics Helper (Optional)

class CacheLogger:
    """Logger do monitorowania cache performance"""

    def __init__(self):
        # TODO (Opcjonalne): Zaimplementuj jeśli masz czas
        pass

    def log_hit(self, product_id: str) -> None:
        """Zaloguj cache hit"""
        pass

    def log_miss(self, product_id: str) -> None:
        """Zaloguj cache miss"""
        pass

    def get_report(self) -> str:
        """Wygeneruj raport cache performance"""
        pass
