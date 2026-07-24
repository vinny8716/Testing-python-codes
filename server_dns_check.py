import paramiko
from DNS_con import DNS_con
from dns_ip_check import bad_dns


command = 'sudo resolvectl status'
i = 0

while i < len(bad_dns):
    DNS_con(bad_dns[i],command)
    i = i + 1