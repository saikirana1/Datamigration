import subprocess
import os

# --- Local PostgreSQL configuration ---
local_user = "postgres"
local_password = "root"
dump_file = "full_pg_dumpall.sql"

# --- Path to pg_dumpall ---
PG_DUMPALL_PATH = r"D:\programs-16\bin\pg_dumpall.exe"  # adjust if needed

# --- Set environment password ---
os.environ["PGPASSWORD"] = local_password

# --- Create full dump ---
print("📦 Exporting all PostgreSQL data (roles + databases)...")

dump_command = [
    PG_DUMPALL_PATH,
    "-U", local_user,
    "-f", dump_file
]

try:
    subprocess.run(dump_command, check=True)
    print(f"✅ Full dump completed. File saved as: {dump_file}")
except subprocess.CalledProcessError as e:
    print("❌ Error during pg_dumpall:", e)
