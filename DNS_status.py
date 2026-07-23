import paramiko
from DNS_con import DNS_con

host = ['10.10.10.10', '10.10.10.20']
command = 'systemctl status named'
i = 0

while i < len(host):
    DNS_con(host[i],command)
    i = i + 1