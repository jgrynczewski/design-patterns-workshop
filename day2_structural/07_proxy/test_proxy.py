"""
Testy dla Proxy Pattern - Product Caching System
"""

import pytest
import time
from starter import (
    ProductService, RealProductService, ProductServiceProxy,
    measure_performance_improvement, CacheLogger
)


class TestRealProductService:
    """Testy prawdziwego serwisu produktów"""

    def test_real_service_creation(self):
        """Test tworzenia prawdziwego serwisu"""
        service = RealProductService()
        assert hasattr(service, 'products')

    def test_real_service_implements_interface(self):
        """Test że RealProductService implementuje interface"""
        service = RealProductService()
        assert isinstance(service, ProductService)

    def test_real_service_get_existing_product(self):
        """Test pobierania istniejącego produktu"""
        service = RealProductService()

        product = service.get_product_details("PROD001")

        assert isinstance(product, dict)
        assert "name" in product
        assert "price" in product
        assert product["name"] == "Gaming Laptop"
        assert product["price"] == 1500.0

    def test_real_service_get_nonexistent_product(self):
        """Test pobierania nieistniejącego produktu"""
        service = RealProductService()

        product = service.get_product_details("NONEXISTENT")

        # Powinien zwrócić None lub rzucić wyjątek
        assert product is None or isinstance(product, Exception)

    def test_real_service_has_delay(self):
        """Test że prawdziwy serwis ma delay (symuluje wolne API)"""
        service = RealProductService()

        start_time = time.time()
        service.get_product_details("PROD001")
        end_time = time.time()

        # Powinno zająć co najmniej 500ms
        assert (end_time - start_time) >= 0.4  # Trochę luzu dla timing


class TestProductServiceProxy:
    """Testy proxy z cache'owaniem"""

    def test_proxy_creation(self):
        """Test tworzenia proxy"""
        proxy = ProductServiceProxy()

        assert hasattr(proxy, 'cache')
        assert hasattr(proxy, 'cache_hits')
        assert hasattr(proxy, 'cache_misses')
        assert proxy.real_service is None  # Lazy initialization

    def test_proxy_implements_interface(self):
        """Test że proxy implementuje interface"""
        proxy = ProductServiceProxy()
        assert isinstance(proxy, ProductService)

    def test_proxy_lazy_initialization(self):
        """Test lazy initialization prawdziwego serwisu"""
        proxy = ProductServiceProxy()

        # Real service nie powinien być utworzony na początku
        assert proxy.real_service is None

        # Po pierwszym wywołaniu powinien być utworzony
        proxy.get_product_details("PROD001")
        assert proxy.real_service is not None
        assert isinstance(proxy.real_service, RealProductService)

    def test_proxy_first_call_cache_miss(self):
        """Test że pierwsze wywołanie to cache miss"""
        proxy = ProductServiceProxy()

        product = proxy.get_product_details("PROD002")

        stats = proxy.get_cache_stats()
        assert stats["misses"] == 1
        assert stats["hits"] == 0
        assert stats["cached_items"] == 1

    def test_proxy_second_call_cache_hit(self):
        """Test że drugie wywołanie to cache hit"""
        proxy = ProductServiceProxy()

        # Pierwsze wywołanie - cache miss
        product1 = proxy.get_product_details("PROD001")

        # Drugie wywołanie - cache hit
        product2 = proxy.get_product_details("PROD001")

        # Produkty powinny być identyczne
        assert product1 == product2

        stats = proxy.get_cache_stats()
        assert stats["hits"] == 1
        assert stats["misses"] == 1
        assert stats["hit_rate"] == 0.5  # 50%

    def test_proxy_multiple_products_caching(self):
        """Test cache'owania wielu różnych produktów"""
        proxy = ProductServiceProxy()

        # Pobierz różne produkty
        proxy.get_product_details("PROD001")  # Miss
        proxy.get_product_details("PROD002")  # Miss
        proxy.get_product_details("PROD001")  # Hit
        proxy.get_product_details("PROD003")  # Miss
        proxy.get_product_details("PROD002")  # Hit

        stats = proxy.get_cache_stats()
        assert stats["hits"] == 2
        assert stats["misses"] == 3
        assert stats["cached_items"] == 3
        assert stats["hit_rate"] == 0.4  # 40%

    def test_proxy_cache_persistence(self):
        """Test że cache jest trwały między wywołaniami"""
        proxy = ProductServiceProxy()

        # Pierwsze wywołanie
        product1 = proxy.get_product_details("PROD001")

        # Sprawdź że jest w cache
        assert proxy.is_cached("PROD001") is True
        assert proxy.is_cached("PROD999") is False

        # Drugie wywołanie powinno być z cache
        product2 = proxy.get_product_details("PROD001")
        assert product1 == product2

    def test_proxy_clear_cache(self):
        """Test czyszczenia cache"""
        proxy = ProductServiceProxy()

        # Dodaj coś do cache
        proxy.get_product_details("PROD001")
        assert proxy.get_cache_stats()["cached_items"] == 1

        # Wyczyść cache
        proxy.clear_cache()

        stats = proxy.get_cache_stats()
        assert stats["cached_items"] == 0
        assert stats["hits"] == 0
        assert stats["misses"] == 0
        assert not proxy.is_cached("PROD001")


class TestProxyPattern:
    """Testy wzorca Proxy"""

    def test_proxy_transparent_interface(self):
        """Test że proxy ma transparentny interfejs"""
        real_service = RealProductService()
        proxy = ProductServiceProxy()

        # Oba powinny zwracać te same dane
        real_product = real_service.get_product_details("PROD001")
        proxy_product = proxy.get_product_details("PROD001")

        assert real_product == proxy_product

    def test_proxy_controls_access(self):
        """Test że proxy kontroluje dostęp do real service"""
        proxy = ProductServiceProxy()

        # Proxy powinien kontrolować kiedy real service jest tworzony
        assert proxy.real_service is None

        # Po pierwszym dostępie
        proxy.get_product_details("PROD001")
        assert proxy.real_service is not None

    def test_proxy_adds_caching_behavior(self):
        """Test że proxy dodaje behavior cache'owania"""
        proxy = ProductServiceProxy()

        # Zmierz czas pierwszego wywołania (cache miss)
        start_time = time.time()
        proxy.get_product_details("PROD001")
        first_call_time = time.time() - start_time

        # Zmierz czas drugiego wywołania (cache hit)
        start_time = time.time()
        proxy.get_product_details("PROD001")
        second_call_time = time.time() - start_time

        # Drugie wywołanie powinno być znacznie szybsze
        assert second_call_time < first_call_time / 10  # Co najmniej 10x szybsze


class TestCachePerformance:
    """Testy wydajności cache"""

    def test_cache_improves_performance(self):
        """Test że cache poprawia wydajność"""
        proxy = ProductServiceProxy()

        # 5 wywołań tego samego produktu
        product_id = "PROD001"

        start_time = time.time()
        for _ in range(5):
            proxy.get_product_details(product_id)
        total_time = time.time() - start_time

        # Z cache powinno zająć mniej niż 2 sekundy
        # (1 real call ~500ms + 4 cache hits ~1ms each)
        assert total_time < 1.0

        stats = proxy.get_cache_stats()
        assert stats["hits"] == 4
        assert stats["misses"] == 1

    def test_cache_hit_rate_calculation(self):
        """Test kalkulacji hit rate"""
        proxy = ProductServiceProxy()

        # Scenariusz z różnymi produktami
        calls = ["PROD001", "PROD002", "PROD001", "PROD003", "PROD001", "PROD002"]

        for product_id in calls:
            proxy.get_product_details(product_id)

        stats = proxy.get_cache_stats()
        expected_hits = 3  # PROD001 (2x), PROD002 (1x)
        expected_misses = 3  # PROD001, PROD002, PROD003 (first time each)

        assert stats["hits"] == expected_hits
        assert stats["misses"] == expected_misses
        assert stats["hit_rate"] == 0.5  # 50%

    def test_cache_memory_usage(self):
        """Test zużycia pamięci przez cache"""
        proxy = ProductServiceProxy()

        # Dodaj wiele produktów do cache
        for i in range(10):
            proxy.get_product_details(f"PROD{i:03d}")

        stats = proxy.get_cache_stats()
        assert stats["cached_items"] <= 10  # Nie więcej niż dodanych

        # Cache nie powinien być pusty
        assert len(proxy.cache) > 0


class TestErrorHandling:
    """Testy obsługi błędów"""

    def test_proxy_handles_nonexistent_product(self):
        """Test obsługi nieistniejących produktów"""
        proxy = ProductServiceProxy()

        # Nieistniejący produkt nie powinien być cache'owany
        result = proxy.get_product_details("NONEXISTENT")

        # Nieistniejące produkty nie powinny być w cache
        assert not proxy.is_cached("NONEXISTENT")

    def test_proxy_handles_real_service_errors(self):
        """Test obsługi błędów z real service"""
        proxy = ProductServiceProxy()

        # Test z różnymi edge cases
        test_cases = ["", None, "INVALID"]

        for case in test_cases:
            try:
                result = proxy.get_product_details(case)
                # Jeśli nie ma wyjątku, sprawdź że wynik jest sensowny
                if result is not None:
                    assert isinstance(result, dict)
            except (ValueError, TypeError):
                # Oczekiwane dla invalid input
                pass


class TestHelperFunctions:
    """Testy helper functions (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_performance_measurement(self):
        """Test pomiaru poprawy wydajności"""
        results = measure_performance_improvement()

        assert isinstance(results, dict)
        assert "without_cache" in results
        assert "with_cache" in results
        assert "improvement" in results

        # Cache powinien być szybszy
        assert results["with_cache"] < results["without_cache"]

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_cache_logger(self):
        """Test loggera cache"""
        logger = CacheLogger()

        logger.log_hit("PROD001")
        logger.log_miss("PROD002")

        report = logger.get_report()
        assert isinstance(report, str)
        assert len(report) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
