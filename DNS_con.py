import paramiko

def DNS_con(host, command):
    hostname = host
    username = 'ubuntu'
    password = 'ubuntu'

    try:
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


        print(f'Connecting to {hostname}...')
        ssh.connect(hostname = hostname, username = username, password = password)

        stdin, stdout, stderr = ssh.exec_command(command)

        print('\n--- Command Output ---')
        print(stdout.read().decode())

        error_output = stderr.read().decode()
        if error_output:
            print(f'Error: {error_output}')

    finally:
        ssh.close()
        print('connection closed')
