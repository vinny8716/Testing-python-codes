import paramiko
from dns_ip_check import bad_dns
username = 'ubuntu'
password = 'ubuntu'
i = 0

while i < len(bad_dns):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=bad_dns[i], username=username, password=password)


    command = (
        "sudo sed -i 's/^#\\?DNS=.*/DNS=10.10.10.10 10.10.10.20/' /etc/systemd/resolved.conf && "
        "sudo systemctl restart systemd-resolved"
    )

    stdin, stdout, stderr = ssh.exec_command(command)


    print(stdout.read().decode())
    print(stderr.read().decode())

    ssh.close()
