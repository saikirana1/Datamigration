import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Neon credentials
NEON_API_KEY = os.getenv("NEON_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
BRANCH_ID = os.getenv("BRANCH_ID")

# Neon API headers
HEADERS = {
    "Authorization": f"Bearer {NEON_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Wait for any ongoing operations to finish
def wait_for_no_conflict():
    check_url = f"https://console.neon.tech/api/v2/projects/{PROJECT_ID}/operations"
    while True:
        res = requests.get(check_url, headers=HEADERS)
        data = res.json()
        active_ops = [op for op in data.get("operations", []) if op.get("status") in ["running", "pending"]]
        if not active_ops:
            break
        print("⏳ Waiting for ongoing operations to complete...")
        time.sleep(2)

# Create a Neon database
def create_database(db_name, owner_name):
    wait_for_no_conflict()
    url = f"https://console.neon.tech/api/v2/projects/{PROJECT_ID}/branches/{BRANCH_ID}/databases"
    payload = {
        "database": {
            "name": db_name,
            "owner_name": owner_name
        }
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 201:
        print(f"✅ Database '{db_name}' created successfully!")
    else:
        print(f"❌ Failed to create database '{db_name}'")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

# Get databases and users from .env
db_names = [x.strip() for x in os.getenv("PG_DATABASES", "").split(",")]
db_users = [x.strip() for x in os.getenv("PG_DB_USERS", "").split(",")]

# Check if lengths match
if len(db_names) != len(db_users):
    raise ValueError("Mismatch: PG_DATABASES and PG_DB_USERS must have the same number of entries.")

# Main runner
if __name__ == "__main__":
    for db_name, user_name in zip(db_names, db_users):
        create_database(db_name, user_name)
