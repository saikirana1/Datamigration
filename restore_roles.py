import subprocess
import os
from dotenv import load_dotenv


load_dotenv()

def restore_roles_from_sql():
    #load_dotenv()  # Load environment variables from .env

    # Get path to psql and Neon DB connection URL from .env
    psql_path = os.getenv("PSQL_PATH")
    neon_url = os.getenv("NEON_DATABASE_URL")

    if not psql_path:
        raise ValueError("Environment variable PSQL_PATH is not set.")
    if not neon_url:
        raise ValueError("Environment variable NEON_DATABASE_URL is not set.")

    command = [psql_path, "-d", neon_url, "-f", "roles.sql"]

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Roles restored successfully from roles.sql")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr.decode()}")
        print("Roles restoration failed.")

if __name__ == "__main__":
    restore_roles_from_sql()
