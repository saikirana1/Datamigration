import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Fetch credentials from .env
NEON_API_KEY = os.getenv("NEON_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
BRANCH_ID = os.getenv("BRANCH_ID")

print("NEON_API_KEY:", NEON_API_KEY)
print("PROJECT_ID:", PROJECT_ID)
print("BRANCH_ID:", BRANCH_ID)

# Headers
HEADERS = {
    "Authorization": f"Bearer {NEON_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Function to create database
def create_database(db_name, owner_name="neondb_owner"):
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
        print(response.json())
    else:
        print("❌ Failed to create database")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

# Example usage
if __name__ == "__main__":
    create_database("my_api_created_db")
