"""
High Cohesion Violation
Klasa robi za dużo różnych rzeczy (low cohesion)
"""

import json
import hashlib
from datetime import datetime


class User:  # PROBLEM: Low cohesion — robi wszystko
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    # User operations (OK)
    def change_password(self, new_password):
        self.password_hash = hashlib.md5(new_password.encode()).hexdigest()

    def get_full_name(self):
        return self.name

    # PROBLEM: Marketing operations (nie user responsibility)
    def send_marketing_email(self):
        print(f"Sending marketing email to {self.email}")

    def calculate_marketing_score(self):
        # Skomplikowana logika marketingowa
        score = len(self.name) * 10
        if "@gmail.com" in self.email:
            score += 50
        return score

    # PROBLEM: Reporting operations (nie user responsibility)
    def generate_user_report(self):
        report = {
            'name': self.name,
            'email': self.email,
            'marketing_score': self.calculate_marketing_score(),
            'report_date': datetime.now().isoformat()
        }
        return json.dumps(report, indent=2)

    # PROBLEM: Infrastructure operations (nie user responsibility)
    def backup_to_s3(self):
        print(f"Backing up user {self.name} to S3")

    def sync_with_external_api(self):
        print(f"Syncing user {self.name} with external CRM")

    # PROBLEM: Database operations (nie user responsibility)
    def save_to_db(self):
        print(f"Saving user {self.name} to database")

    def delete_from_db(self):
        print(f"Deleting user {self.name} from database")


if __name__ == "__main__":
    user = User("John Doe", "john@gmail.com")

    # User ma za dużo odpowiedzialności
    user.change_password("secret123")
    user.send_marketing_email()
    user.generate_user_report()
    user.backup_to_s3()
    user.save_to_db()

    print("❌ User klasa robi wszystko - low cohesion")
    print("❌ Trudna do testowania i utrzymania")
    print("❌ Każda zmiana w różnych obszarach wymaga modyfikacji User")
