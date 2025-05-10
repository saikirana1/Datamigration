import subprocess
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs


load_dotenv()

def restore_roles_to_multiple_databases():
    psql_path = os.getenv("PSQL_PATH")
    base_url = os.getenv("dest_DATABASE_URL")
    db_list_raw = os.getenv("PG_DATABASES")

    if not psql_path or not base_url or not db_list_raw:
        raise ValueError("One or more required environment variables are missing.")

    database_names = [db.strip() for db in db_list_raw.split(",") if db.strip()]
    parsed = urlparse(base_url)
    ssl_mode = parse_qs(parsed.query).get("sslmode", ["require"])[0]

   
    port = parsed.port if parsed.port else 5432

    for db_name in database_names:
        print(f"\n🔄 Restoring roles into database: {db_name}")

        updated_url = f"{parsed.scheme}://{parsed.username}:{parsed.password}@{parsed.hostname}:{port}/{db_name}?sslmode={ssl_mode}"

        command = [psql_path, "-d", updated_url, "-f", "roles.sql"]

        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"✅ Successfully restored roles to '{db_name}'")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to restore roles to '{db_name}'")
            print(f"Error: {e.stderr.decode()}")

if __name__ == "__main__":
    restore_roles_to_multiple_databases()



