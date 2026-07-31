import paramiko
from DNS_con import DNS_con

host = ['10.10.10.10', '10.10.10.20']
command = 'sudo systemctl restart named'
i = 0

while i < len(host):
    DNS_con(host[i],command)
    print(f"DNS: {host[i]} has been restarted\n")
    i = i + 1
