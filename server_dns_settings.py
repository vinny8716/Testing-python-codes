import paramiko

# Connection details
HOSTNAME = '192.168.1.50'
PORT = 22
USERNAME = 'your_username'
PASSWORD = 'your_password'

# File paths and edit details
REMOTE_FILE_PATH = '/etc/your_config_file.conf'
SEARCH_PATTERN = 'max_connections = 100'
REPLACE_PATTERN = 'max_connections = 500'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote server
    ssh.connect(HOSTNAME, port=PORT, username=USERNAME, password=PASSWORD)

    # 1. Read the remote file
    stdin, stdout, stderr = ssh.exec_command(f'cat {REMOTE_FILE_PATH}')
    file_content = stdout.read().decode('utf-8')

    if stderr.read():
        print(f"Error reading file. Check permissions. {stderr.read().decode('utf-8')}")
    else:
        # 2. Modify the target configuration
        if SEARCH_PATTERN in file_content:
            updated_content = file_content.replace(SEARCH_PATTERN, REPLACE_PATTERN)

            # 3. Overwrite the remote file with the new configuration
            # Use 'sudo bash -c' if the config file requires root privileges
            command = f"echo '{updated_content}' > {REMOTE_FILE_PATH}"
            stdin, stdout, stderr = ssh.exec_command(command)

            if stderr.read():
                print(f"Failed to write file: {stderr.read().decode('utf-8')}")
            else:
                print("Configuration successfully updated remotely.")
        else:
            print("Search pattern not found in the remote file.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    ssh.close()
