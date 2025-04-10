import subprocess

# --- Path to psql executable ---
PSQL_PATH = r"D:\programs-16\bin\psql.exe"  # adjust if needed

# --- Dump file created from Part 1 ---
dump_file = "full_pg_dumpall.sql"

# --- Neon PostgreSQL Connection URI ---
neon_uri = "postgresql://neondb_owner:npg_aLH2eYsu1mkM@ep-frosty-base-a5ijuw75-pooler.us-east-2.aws.neon.tech/myproj3-college?sslmode=require"

# --- Restore the dump ---
print("🔁 Restoring full dump (including roles and databases) to Neon Cloud...")

restore_command = [
    PSQL_PATH,
    neon_uri,
    "-f", dump_file
]

try:
    subprocess.run(restore_command, check=True)
    print("✅ Full restore to Neon completed.")
except subprocess.CalledProcessError as e:
    print("❌ Restore failed:", e)


