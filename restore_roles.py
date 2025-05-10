import subprocess
import os
from dotenv import load_dotenv


load_dotenv()

def restore_roles_from_sql():
    

    
    psql_path = os.getenv("PSQL_PATH")
    dest_url = os.getenv("dest_DATABASE_URL")

    if not psql_path:
        raise ValueError("Environment variable PSQL_PATH is not set.")
    if not dest_url:
        raise ValueError("Environment variable dest_DATABASE_URL is not set.")

    command = [psql_path, "-d", dest_url, "-f", "roles.sql"]

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Roles restored successfully from roles.sql")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr.decode()}")
        print("Roles restoration failed.")

if __name__ == "__main__":
    restore_roles_from_sql()
