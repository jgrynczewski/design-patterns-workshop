"""
Separation of Concerns Solution - Oddzielenie aspektów
Każdy concern ma własną warstwę/klasę odpowiedzialności
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import json


# ============================================================================
# LAYER 1: DOMAIN (Business Logic) - Czysty model domenowy
# ============================================================================

class User:
    """CLEAN: User zawiera tylko business logic, żadnych infrastructure concerns"""

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True

    def change_password(self, new_password: str) -> None:
        """Business rule: password validation"""
        if len(new_password) < 8:
            raise ValueError("Password too short")
        self.password = new_password

    def deactivate_account(self) -> None:
        """Business operation"""
        self.is_active = False

    def should_auto_activate(self) -> bool:
        """Business rule: company emails auto-activate"""
        return self.email.endswith('@company.com')


# ============================================================================
# LAYER 2: INFRASTRUCTURE - External concerns
# ============================================================================

class UserRepository(ABC):
    """Data persistence abstraction"""

    @abstractmethod
    def save(self, user: User) -> None: pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]: pass


class DatabaseUserRepository(UserRepository):
    """CLEAN: Persistence concern oddzielony od domain"""

    def save(self, user: User) -> None:
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password, is_active) 
            VALUES (?, ?, ?, ?)
        """, (user.username, user.email, user.password, user.is_active))
        conn.commit()
        conn.close()

    def find_by_id(self, user_id: int) -> Optional[User]:
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return User(username=row[1], email=row[2], password=row[3])
        return None


class EmailService(ABC):
    """Email communication abstraction"""

    @abstractmethod
    def send_welcome_email(self, user: User) -> None: pass


class SMTPEmailService(EmailService):
    """CLEAN: Email concern oddzielony"""

    def send_welcome_email(self, user: User) -> None:
        import smtplib
        from email.mime.text import MIMEText

        msg = MIMEText(f"Welcome {user.username}!")
        msg['Subject'] = 'Welcome to our platform'
        msg['From'] = 'noreply@example.com'
        msg['To'] = user.email

        server = smtplib.SMTP('localhost', 587)
        server.send_message(msg)
        server.quit()


class Logger(ABC):
    """Logging abstraction"""

    @abstractmethod
    def log_user_activity(self, username: str, action: str) -> None: pass


class FileLogger(Logger):
    """CLEAN: Logging concern oddzielony"""

    def log_user_activity(self, username: str, action: str) -> None:
        import logging
        import datetime

        logging.basicConfig(filename='user_activity.log', level=logging.INFO)
        timestamp = datetime.datetime.now().isoformat()
        logging.info(f"{timestamp} - User {username}: {action}")


# ============================================================================
# LAYER 3: APPLICATION SERVICES - Use cases
# ============================================================================

class UserService:
    """CLEAN: Application service koordynuje use case, nie zawiera business logic"""

    def __init__(self,
                 user_repo: UserRepository,
                 email_service: EmailService,
                 logger: Logger):
        self.user_repo = user_repo
        self.email_service = email_service
        self.logger = logger

    def create_user(self, username: str, email: str, password: str) -> User:
        """Use case: tworzenie użytkownika z pełnym workflow"""

        # Domain logic
        user = User(username, email, password)

        # Business rule applied
        if user.should_auto_activate():
            user.is_active = True

        # Infrastructure orchestration
        self.user_repo.save(user)
        self.email_service.send_welcome_email(user)
        self.logger.log_user_activity(user.username, 'User created')

        return user


# ============================================================================
# LAYER 4: PRESENTATION - Input validation, serialization
# ============================================================================

class UserValidator:
    """CLEAN: Input validation oddzielony od domain"""

    @staticmethod
    def validate_user_input(data: Dict) -> List[str]:
        errors = []

        if 'username' not in data or len(data['username']) < 3:
            errors.append("Username must be at least 3 characters")

        if 'email' not in data or '@' not in data['email']:
            errors.append("Valid email required")

        if 'password' not in data or len(data['password']) < 8:
            errors.append("Password must be at least 8 characters")

        return errors


class UserSerializer:
    """CLEAN: Serialization concern oddzielony"""

    @staticmethod
    def to_json(user: User) -> str:
        return json.dumps({
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active
            # Password celowo pominięte
        })


# ============================================================================
# LAYER 5: INTERFACE - HTTP/API layer
# ============================================================================

class UserController:
    """CLEAN: Controller tylko konwertuje HTTP -> Application Service"""

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, request_data: Dict) -> Dict:
        # Validation concern
        validation_errors = UserValidator.validate_user_input(request_data)
        if validation_errors:
            return {'errors': validation_errors}

        try:
            # Delegation to application service
            user = self.user_service.create_user(
                request_data['username'],
                request_data['email'],
                request_data['password']
            )

            # Presentation concern
            return {
                'status': 'success',
                'user': UserSerializer.to_json(user),
                'message': f'User {user.username} created successfully'
            }

        except Exception as e:
            return {'status': 'error', 'message': str(e)}


# ============================================================================
# COMPOSITION ROOT - Dependency injection setup
# ============================================================================

def create_user_controller() -> UserController:
    """Factory method - wiring dependencies"""

    # Infrastructure layer
    user_repo = DatabaseUserRepository()
    email_service = SMTPEmailService()
    logger = FileLogger()

    # Application layer
    user_service = UserService(user_repo, email_service, logger)

    # Presentation layer
    return UserController(user_service)

# RESULT: Każdy concern ma swoją odpowiedzialność:
# - Domain: User (business logic)
# - Infrastructure: Repository, EmailService, Logger (external)
# - Application: UserService (use case orchestration)
# - Presentation: Validator, Serializer (input/output)
# - Interface: Controller (HTTP handling)
