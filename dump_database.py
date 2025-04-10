import subprocess

def dump_database():
    # Full path to pg_dump
    pg_dump_path = r"D:\programs-16\bin\pg_dump"  # Change if your pg_dump is elsewhere

    # PostgreSQL credentials and target file
    user = "postgres"
    db_name = "hospitalmanagement"
    output_file = "hospital_dump.sql"

    # Build the command
    command = [pg_dump_path, "-U", user, "-d", db_name, "-f", output_file]

    try:
        # Run the command with environment variable for password prompt bypass (optional)
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Database '{db_name}' dumped successfully to '{output_file}'")

    except subprocess.CalledProcessError as e:
        print(f"Error during pg_dump:\n{e.stderr.decode()}")

if __name__ == "__main__":
    dump_database()
