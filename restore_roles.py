import subprocess

def restore_roles_from_sql():
    # Define the full path to psql
    psql_path = r"D:\programs-16\bin\psql"
    
    # Define the command to execute with the full path to psql
    command = [psql_path, "-d", "postgresql://neondb_owner:npg_D1Tywt5zEYUW@ep-square-sea-a5693zzq-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require", "-f", "roles.sql"]
    
    try:
        # Run the command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Output success message
        print("Roles restored successfully from roles.sql")
    
    except subprocess.CalledProcessError as e:
        # If an error occurs, print the error message
        print(f"Error executing command: {e.stderr.decode()}")
        print("Roles restoration failed.")

if __name__ == "__main__":
    restore_roles_from_sql()
