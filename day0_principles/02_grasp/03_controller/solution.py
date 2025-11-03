"""
Controller Solution
Controller koordynuje use case, HTTP handler tylko konwertuje format
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = None


class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")
        user.id = 123
        return user


class EmailService:
    def send_welcome(self, user):
        print(f"Sending welcome email to {user.email}")


class UserController:  # Controller koordynuje use case
    def __init__(self, user_repo, email_service):
        self.user_repo = user_repo
        self.email_service = email_service

    def create_user(self, user_data):
        # Koordynuje cały use case
        user = User(user_data["name"], user_data["email"])
        saved_user = self.user_repo.save(user)
        self.email_service.send_welcome(saved_user)
        return saved_user


class UserHTTPHandler:  # HTTP layer tylko konwertuje format
    def __init__(self, controller):
        self.controller = controller

    def create_user(self, request):
        # Tylko konwersja HTTP -> domain i domain -> HTTP
        user = self.controller.create_user(request.data)
        return {"id": user.id, "name": user.name, "status": "created"}


class ProductController:  # Reużywalny pattern
    def __init__(self, product_repo, notification_service):
        self.product_repo = product_repo
        self.notification_service = notification_service

    def create_product(self, product_data):
        # Koordynuje use case dla produktów
        print("Creating product...")
        print("Saving to repository...")
        print("Sending notification...")
        return {"id": 456, "status": "created"}


if __name__ == "__main__":
    class MockRequest:
        def __init__(self, data):
            self.data = data


    # Dependency injection
    user_repo = UserRepository()
    email_service = EmailService()
    controller = UserController(user_repo, email_service)
    handler = UserHTTPHandler(controller)

    request = MockRequest({"name": "John", "email": "john@example.com"})
    result = handler.create_user(request)
    print(f"HTTP Response: {result}")

    print("✅ Controller koordynuje use case")
    print("✅ HTTP handler tylko konwertuje format")
    print("✅ Clear separation of concerns")
