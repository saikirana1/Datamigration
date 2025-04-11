import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch Neon and PostgreSQL configuration from .env
neon_user = os.getenv("NEON_USER")
neon_host = os.getenv("NEON_HOST")
neon_password = os.getenv("NEON_PASSWORD")
db_names = [db.strip() for db in os.getenv("PG_DATABASES", "").split(",")]
psql_path = os.getenv("PSQL_PATH")  # ✅ Now coming from .env

if not psql_path or not os.path.exists(psql_path):
    raise ValueError("❌ PSQL_PATH is not set correctly or psql not found.")

def restore_to_neon(db_name):
    # Construct Neon DB connection string
    conn_str = (
        f"postgresql://{neon_user}:{neon_password}@{neon_host}/{db_name}?sslmode=require"
    )

    # Expected SQL file name
    sql_file = f"{db_name}.sql"

    if not os.path.exists(sql_file):
        print(f"⚠️  SQL file '{sql_file}' not found. Skipping...")
        return

    command = [psql_path, conn_str, "-f", sql_file]

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"✅ Restored '{sql_file}' into '{db_name}' on Neon.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to restore '{db_name}':")
        print(e.stderr.decode())

if __name__ == "__main__":
    for db in db_names:
        restore_to_neon(db)
