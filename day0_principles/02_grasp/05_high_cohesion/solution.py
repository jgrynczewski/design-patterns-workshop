"""
High Cohesion Solution
Każda klasa ma jedną, spójną odpowiedzialność
"""

import json
import hashlib
from datetime import datetime


class User:  # High cohesion - tylko user-related operations
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()
        self.password_hash = None

    def change_password(self, new_password):
        self.password_hash = hashlib.md5(new_password.encode()).hexdigest()

    def get_full_name(self):
        return self.name

    def get_user_data(self):
        return {
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }


class MarketingService:  # High cohesion - tylko marketing operations
    def send_marketing_email(self, user):
        print(f"Sending marketing email to {user.email}")

    def calculate_marketing_score(self, user):
        score = len(user.name) * 10
        if "@gmail.com" in user.email:
            score += 50
        return score

    def create_marketing_campaign(self, users):
        qualified_users = [u for u in users if self.calculate_marketing_score(u) > 60]
        print(f"Created campaign for {len(qualified_users)} qualified users")


class ReportGenerator:  # High cohesion - tylko reporting operations
    def generate_user_report(self, user):
        marketing_service = MarketingService()
        report = {
            'name': user.name,
            'email': user.email,
            'marketing_score': marketing_service.calculate_marketing_score(user),
            'report_date': datetime.now().isoformat()
        }
        return json.dumps(report, indent=2)

    def generate_bulk_report(self, users):
        reports = [self.generate_user_report(user) for user in users]
        return "\n".join(reports)


class BackupService:  # High cohesion - tylko infrastructure operations
    def backup_to_s3(self, user):
        print(f"Backing up user {user.name} to S3")

    def sync_with_external_api(self, user):
        print(f"Syncing user {user.name} with external CRM")

    def bulk_backup(self, users):
        for user in users:
            self.backup_to_s3(user)


class UserRepository:  # High cohesion - tylko database operations
    def save(self, user):
        print(f"Saving user {user.name} to database")

    def delete(self, user):
        print(f"Deleting user {user.name} from database")

    def find_by_email(self, email):
        print(f"Finding user by email: {email}")
        return None


if __name__ == "__main__":
    # Każda klasa ma jedną odpowiedzialność
    user = User("John Doe", "john@gmail.com")

    # Specialized services
    marketing = MarketingService()
    reports = ReportGenerator()
    backup = BackupService()
    repo = UserRepository()

    # Clear separation of concerns
    user.change_password("secret123")
    marketing.send_marketing_email(user)
    report = reports.generate_user_report(user)
    backup.backup_to_s3(user)
    repo.save(user)

    print("✅ Każda klasa ma jedną, spójną odpowiedzialność")
    print("✅ Łatwe testowanie - małe, fokusowane klasy")
    print("✅ Łatwe utrzymanie - zmiany w jednym obszarze")
