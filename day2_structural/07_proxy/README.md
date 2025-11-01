# 🛡️ Proxy - Product Caching System

**Difficulty**: easy \
**Time**: 12 minutes \
**Focus**: Proxy pattern - controlling access with caching

## 🎯 Zadanie
Implementuj system cache'owania dla kosztownych operacji ładowania produktów używając wzorca Proxy, który kontroluje dostęp do prawdziwego obiektu.

## 📋 Wymagania
- [ ] `ProductService` interface z metodą `get_product_details(product_id)`
- [ ] `RealProductService` - prawdziwy serwis (symuluje wolne API/DB)
- [ ] `ProductServiceProxy` - proxy z cache'owaniem wyników
- [ ] Cache przechowuje wyniki wcześniejszych zapytań
- [ ] Proxy loguje hits/misses dla monitoringu
- [ ] Lazy initialization - proxy tworzy real service dopiero gdy potrzeba

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj ProductService interface
4. Zaimplementuj RealProductService i ProductServiceProxy
5. Uruchom testy: `python -m pytest test_proxy.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Proxy implementuje ten sam interface co RealService
- Cache jako słownik: {product_id: product_data}
- Lazy initialization: stwórz real_service dopiero przy pierwszym użyciu
- Loguj cache hits/misses dla analytics

## 🚀 Use Cases
- **API Caching**: Cache odpowiedzi z zewnętrznych API
- **Database Proxy**: Cache wyników zapytań DB
- **Image Loading**: Cache załadowanych obrazów w aplikacji

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Każde wywołanie = kosztowne API call ❌
service = RealProductService()
product1 = service.get_product_details("PROD001")  # API call - 500ms
product2 = service.get_product_details("PROD001")  # API call - 500ms again! ❌  
product3 = service.get_product_details("PROD001")  # API call - 500ms again! ❌

# Brak cache = 1500ms total ❌
```

### ✅ Z wzorcem:

```python
# Proxy z cache'owaniem ✅
proxy = ProductServiceProxy()
product1 = proxy.get_product_details("PROD001")  # API call - 500ms
product2 = proxy.get_product_details("PROD001")  # Cache hit - 1ms ✅
product3 = proxy.get_product_details("PROD001")  # Cache hit - 1ms ✅

# Z cache = 502ms total ✅ (66% oszczędności!)
```

Korzyść: Transparentne cache'owanie bez zmiany kodu klienta
