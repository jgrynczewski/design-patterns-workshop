"""
Pure Fabrication Violation - GRASP
Domain objects z odpowiedzialnością techniczną
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def change_password(self, new_password):
        # OK - user operation
        self.password = new_password

    def get_full_name(self):
        # OK - user data
        return self.name

    # PROBLEM: Technical responsibilities in domain object
    def save_to_database(self):
        # User nie powinien znać DB
        print(f"INSERT INTO users VALUES('{self.name}', '{self.email}')")

    def send_welcome_email(self):
        # User nie powinien znać email logic
        print(f"Sending welcome email to {self.email}")

    def log_activity(self, action):
        # User nie powinien znać logging
        print(f"LOG: User {self.name} performed {action}")

    def backup_to_s3(self):
        # User nie powinien znać infrastructure
        print(f"Backing up user {self.name} to S3")


if __name__ == "__main__":
    user = User("John", "john@example.com")
    user.save_to_database()
    user.send_welcome_email()
    user.log_activity("login")
    user.backup_to_s3()
    print("❌ User klasa ma zbyt wiele technicznych odpowiedzialności")
