import subprocess
import os
import psycopg2

# --- Local PostgreSQL configuration ---
local_db_user = "postgres"
local_db_name = "college2"
local_db_password = "root"

# --- Neon (Cloud) PostgreSQL configuration ---
neon_connection_uri = "postgresql://neondb_owner:npg_aLH2eYsu1mkM@ep-frosty-base-a5ijuw75-pooler.us-east-2.aws.neon.tech/myproj2-college?sslmode=require"

# --- Dump file path ---
dump_file = "college2.sql"

# --- Step 1: Create a pg_dump from local database ---
print("Creating dump from local database...")
os.environ["PGPASSWORD"] = local_db_password
dump_command = [
    r"D:\programs-16\bin\pg_dump.exe",
    "--no-owner",  # Avoid ownership issues
    "-U", local_db_user,
    "-d", local_db_name,
    "-f", dump_file
]

try:
    subprocess.run(dump_command, check=True)
    print(f"✅ Dump created successfully as '{dump_file}'")
except subprocess.CalledProcessError as e:
    print("❌ Failed to create dump:", e)
    exit()

# --- Step 2: Get roles from local database ---
print("Fetching roles from local database...")

try:
    conn = psycopg2.connect(
        dbname=local_db_name,
        user=local_db_user,
        password=local_db_password,
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT rolname FROM pg_roles WHERE rolname NOT IN ('postgres');")
    roles = cursor.fetchall()
    cursor.close()
    conn.close()

    # Build dynamic SQL for creating roles in Neon
    role_sql_commands = "DO $$ BEGIN\n"
    for role in roles:
        role_name = role[0]
        role_sql_commands += f"   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '{role_name}') THEN\n"
        role_sql_commands += f"      CREATE ROLE {role_name};\n"
        role_sql_commands += f"   END IF;\n"
    role_sql_commands += "END $$;"

    print("✅ Roles fetched successfully from local DB.")

except Exception as e:
    print("❌ Error fetching roles:", e)
    exit()

# --- Step 3: Create roles in Neon ---
print("Creating roles in Neon...")

try:
    subprocess.run(
        [r"D:\programs-16\bin\psql.exe", neon_connection_uri, "-c", role_sql_commands],
        check=True
    )
    print("✅ Roles created successfully in Neon.")
except subprocess.CalledProcessError as e:
    print("❌ Failed to create roles in Neon:", e)

# --- Step 4: Restore into Neon ---
print("Restoring dump into Neon database...")
restore_command = [
    r"D:\programs-16\bin\psql.exe",
    neon_connection_uri,
    "-f", dump_file
]

try:
    subprocess.run(restore_command, check=True)
    print("✅ Restore into Neon database completed successfully.")
except subprocess.CalledProcessError as e:
    print("❌ Failed to restore into Neon database:", e)


