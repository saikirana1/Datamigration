import subprocess

def restore_to_neon():
    # Full path to the psql executable
    psql_path = r"D:\programs-16\bin\psql"  # Make sure this is correct

    # ✅ Updated Neon Cloud connection string
    neon_conn_string = (
        "postgresql://neondb_owner:npg_D1Tywt5zEYUW@"
        "ep-square-sea-a5693zzq-pooler.us-east-2.aws.neon.tech/"
        "neondb?sslmode=require"
    )

    # SQL file you want to restore
    sql_file = "hospital_dump.sql"

    # Construct the command
    command = [psql_path, neon_conn_string, "-f", sql_file]

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ Database restored successfully to Neon Cloud.")
    except subprocess.CalledProcessError as e:
        print("❌ Error during restore:")
        print(e.stderr.decode())

if __name__ == "__main__":
    restore_to_neon()
