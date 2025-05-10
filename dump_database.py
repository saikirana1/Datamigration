import subprocess
import os
from dotenv import load_dotenv

def dump_all_databases():
    load_dotenv()

    pg_dump_path = os.getenv("PG_DUMP_PATH")
    pg_user = os.getenv("PG_USERNAME")
    pg_password = os.getenv("PG_PASSWORD")
    db_list_raw = os.getenv("PG_DATABASES")
    pg_host = os.getenv("PG_HOST")

    if not all([pg_dump_path, pg_user, pg_password, db_list_raw]):
        raise ValueError("Missing required environment variables (PG_DUMP_PATH, PG_USERNAME, PG_PASSWORD, PG_DATABASES)")

    
    databases = [db.strip() for db in db_list_raw.split(",")]

    env = os.environ.copy()
    env["PGPASSWORD"] = pg_password

    for db in databases:
        output_file = f"{db}.sql"
        command = [pg_dump_path, "-U", pg_user, "-d", db, "-h", pg_host, "-f", output_file]

        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
            print(f"✅ Dumped '{db}' to '{output_file}'")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to dump '{db}':\n{e.stderr.decode()}")

if __name__ == "__main__":
    dump_all_databases()

