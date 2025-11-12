"""
Controller Violation
HTTP handler bezpośrednio manipuluje domain objects i zna business logic
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = None

    def save_to_db(self):
        print(f"Saving {self.name} to database")
        self.id = 123

    def send_welcome_email(self):
        print(f"Sending welcome email to {self.email}")


class UserHTTPHandler:  # PROBLEM: HTTP layer wie za dużo
    def create_user(self, request):
        # PROBLEM: HTTP handler zna domain logic
        user = User(request.data["name"], request.data["email"])

        # PROBLEM: HTTP handler zna persistence
        user.save_to_db()

        # PROBLEM: HTTP handler zna email logic
        user.send_welcome_email()

        # PROBLEM: HTTP handler formatuje response
        return f"User {user.name} created with ID {user.id}"


class ProductHTTPHandler:  # PROBLEM: Duplikacja logiki
    def create_product(self, request):
        # Podobna logika jak w UserHTTPHandler
        print("Creating product...")
        print("Saving to database...")
        print("Sending notification...")
        return "Product created"


if __name__ == "__main__":
    class MockRequest:
        def __init__(self, data):
            self.data = data


    handler = UserHTTPHandler()
    request = MockRequest({"name": "John", "email": "john@example.com"})
    result = handler.create_user(request)
    print(result)

    print("❌ HTTP handler wie za dużo o domain logic")
    print("❌ Brak separation of concerns")
