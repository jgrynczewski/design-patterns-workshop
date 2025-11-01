"""Demonstracja modularnej architektury SOLID"""
from config.dependency_injection import create_mysql_smtp_processor, create_postgres_sendgrid_processor
from domain.customer import RegularCustomer, PremiumCustomer, BlockedCustomer
from core.order_processor import calculate_total_discount

if __name__ == "__main__":
    # Wybór konfiguracji
    processor = create_mysql_smtp_processor()
    # processor = create_postgres_sendgrid_processor()  # alternatywa

    # Wszystkie zasady SOLID w akcji
    premium_customer = PremiumCustomer()
    success, message = processor.process_order(
        premium_customer,
        [{"price": 100}],
        "test@example.com"
    )
    print(f"Result: {success}, {message}")

    # LSP compliance — wszystkie typy Customer działają
    customers_list = [RegularCustomer(), PremiumCustomer(), BlockedCustomer()]
    total_discount = calculate_total_discount(customers_list)
    print(f"Total available discount: ${total_discount}")

    print("\n=== WSZYSTKIE ZASADY SOLID ZASTOSOWANE ===")
    print("✅ SRP: Każda klasa ma jedną, jasną odpowiedzialność")
    print("✅ OCP: Nowe typy klientów przez strategy pattern")
    print("✅ LSP: Wszystkie typy Customer działają jednakowo")
    print("✅ ISP: Małe, wyspecjalizowane interfejsy")
    print("✅ DIP: Zależności od abstrakcji, nie konkretnych klas")
    print("\n🎉 Kod jest łatwy w utrzymaniu, rozszerzaniu i testowaniu!")
