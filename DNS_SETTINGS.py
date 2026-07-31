import paramiko
username = 'ubuntu'
password = 'ubuntu'
bad_DNS = ['192.168.30.101', '192.168.20.210', '192.168.30.210']
i = 0

while i < len(bad_DNS):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=bad_DNS[i], username=username, password=password)


    command = (
        "sudo sed -i 's/^#\\?DNS=.*/DNS=10.10.10.10 10.10.10.20/' /etc/systemd/resolved.conf && "
        "cat /etc/systemd/resolved.conf"
        "sudo systemctl restart systemd-resolved"
    )

    stdin, stdout, stderr = ssh.exec_command(command)


    print(stdout.read().decode())
    print(stderr.read().decode())

    ssh.close()
