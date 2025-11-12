"""
Separation of Concerns Violation - Mieszanie różnych aspektów
Jeden moduł/klasa odpowiada za więcej niż jeden concern
"""


class User:
    """PROBLEM: User class miesza 4 różne concerns w jednej klasie"""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True

    # CONCERN 1: Business Logic (Domain)
    def change_password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password too short")
        self.password = new_password

    def deactivate_account(self):
        self.is_active = False

    # CONCERN 2: Data Persistence (Infrastructure)
    def save_to_database(self):
        # PROBLEM: Domain object zna szczegóły bazy danych
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password, is_active) 
            VALUES (?, ?, ?, ?)
        """, (self.username, self.email, self.password, self.is_active))
        conn.commit()
        conn.close()

    def load_from_database(self, user_id):
        # PROBLEM: Business logic miesza się z SQL
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            self.username, self.email, self.password = row[1], row[2], row[3]
        conn.close()

    # CONCERN 3: External Communication (Infrastructure)
    def send_welcome_email(self):
        # PROBLEM: User odpowiada za wysyłanie emaili
        import smtplib
        from email.mime.text import MIMEText

        msg = MIMEText(f"Welcome {self.username}!")
        msg['Subject'] = 'Welcome to our platform'
        msg['From'] = 'noreply@example.com'
        msg['To'] = self.email

        server = smtplib.SMTP('localhost', 587)
        server.send_message(msg)
        server.quit()

    def log_activity(self, action):
        # PROBLEM: Domain object odpowiada za logging
        import logging
        import datetime

        logging.basicConfig(filename='user_activity.log', level=logging.INFO)
        timestamp = datetime.datetime.now().isoformat()
        logging.info(f"{timestamp} - User {self.username}: {action}")

    # CONCERN 4: Presentation/Validation (UI layer)
    def to_json(self):
        # PROBLEM: Domain object wie jak się serializować do JSON
        import json
        return json.dumps({
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active
            # Password celowo pominięte w JSON
        })

    def validate_input(self, data):
        # PROBLEM: Domain object validuje input z UI
        errors = []

        if 'username' not in data or len(data['username']) < 3:
            errors.append("Username must be at least 3 characters")

        if 'email' not in data or '@' not in data['email']:
            errors.append("Valid email required")

        if 'password' not in data or len(data['password']) < 8:
            errors.append("Password must be at least 8 characters")

        return errors


class UserController:
    """PROBLEM: Controller też miesza concerns"""

    def create_user(self, request_data):
        # PROBLEM: Controller zawiera business logic
        user = User(
            request_data['username'],
            request_data['email'],
            request_data['password']
        )

        # PROBLEM: Controller wykonuje validation
        validation_errors = user.validate_input(request_data)
        if validation_errors:
            return {'errors': validation_errors}

        # PROBLEM: Controller bezpośrednio zarządza persistence
        user.save_to_database()

        # PROBLEM: Controller zawiera business rules
        if user.email.endswith('@company.com'):
            user.is_active = True  # Auto-activate company emails

        # PROBLEM: Controller odpowiada za external communication
        user.send_welcome_email()
        user.log_activity('User created')

        # PROBLEM: Controller wie o formacie response
        return {
            'status': 'success',
            'user': user.to_json(),
            'message': f'User {user.username} created successfully'
        }

# PROBLEM: Wszystko w jednym miejscu - brak separation
# - Business logic (validation, rules)
# - Data access (SQL, database)
# - Infrastructure (email, logging)
# - Presentation (JSON, HTTP responses)
