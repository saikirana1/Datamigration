import subprocess
import os
from dotenv import load_dotenv

def dump_roles_to_sql():
    load_dotenv()

    pg_dumpall_path = os.getenv("PG_DUMPALL_PATH")
    pg_user = os.getenv("PG_USERNAME")
    pg_password = os.getenv("PG_PASSWORD")  # ✅ New line
    pg_host = os.getenv("PG_HOST")  # ✅ New line

    if not pg_user:
        raise ValueError("Environment variable PG_USERNAME is not set.")
    if not pg_dumpall_path:
        raise ValueError("Environment variable PG_DUMPALL_PATH is not set.")
    if not pg_password:
        raise ValueError("Environment variable PG_PASSWORD is not set.")

    # ✅ Set the environment variable for subprocess
    env = os.environ.copy()
    env["PGPASSWORD"] = pg_password

    command = [pg_dumpall_path, '-U', pg_user, '--roles-only', '--no-role-passwords', '-f', 'roles.sql', '-h', pg_host]
    
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
        print("✅ Roles dumped successfully to roles.sql")
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr.decode()}")
        print("Roles dump failed.")

if __name__ == "__main__":
    dump_roles_to_sql()
    



