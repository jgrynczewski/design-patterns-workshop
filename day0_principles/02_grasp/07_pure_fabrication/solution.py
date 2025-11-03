"""
Pure Fabrication Solution - GRASP
Separacja domain objects od technical concerns
"""


class User:  # Pure domain object
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def change_password(self, new_password):
        self.password = new_password

    def get_full_name(self):
        return self.name


# Pure Fabrications - nie reprezentują domain concepts
class UserRepository:  # Fabrication dla persistence
    def save(self, user):
        print(f"INSERT INTO users VALUES('{user.name}', '{user.email}')")

    def find_by_email(self, email):
        print(f"SELECT * FROM users WHERE email='{email}'")


class EmailService:  # Fabrication dla email
    def send_welcome(self, user):
        print(f"Sending welcome email to {user.email}")

    def send_notification(self, user, message):
        print(f"Sending '{message}' to {user.email}")


class ActivityLogger:  # Fabrication dla logging
    def log_user_action(self, user, action):
        print(f"LOG: User {user.name} performed {action}")


class BackupService:  # Fabrication dla infrastructure
    def backup_user(self, user):
        print(f"Backing up user {user.name} to S3")


class UserService:  # Orchestrator - coordinates fabrications
    def __init__(self, repo, email_service, logger, backup_service):
        self.repo = repo
        self.email_service = email_service
        self.logger = logger
        self.backup_service = backup_service

    def register_user(self, user):
        self.repo.save(user)
        self.email_service.send_welcome(user)
        self.logger.log_user_action(user, "registered")
        self.backup_service.backup_user(user)


if __name__ == "__main__":
    user = User("John", "john@example.com")

    # Pure Fabrications handle technical concerns
    repo = UserRepository()
    email_service = EmailService()
    logger = ActivityLogger()
    backup_service = BackupService()

    user_service = UserService(repo, email_service, logger, backup_service)
    user_service.register_user(user)

    print("✅ Domain object czysty, technical concerns w fabrications")
