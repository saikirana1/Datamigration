import subprocess

def dump_roles_to_sql():
    # Define the full path to pg_dumpall (adjust if needed)
    command = ['D:\\programs-16\\bin\\pg_dumpall', '-U', 'postgres', '--roles-only', '-f', 'roles.sql']
    
    try:
        # Run the command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Output success message
        print("Roles dumped successfully to roles.sql")
    
    except subprocess.CalledProcessError as e:
        # If an error occurs, print the error message
        print(f"Error executing command: {e.stderr.decode()}")
        print("Roles dump failed.")

if __name__ == "__main__":
    dump_roles_to_sql()
