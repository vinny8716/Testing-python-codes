import subprocess
from subprocess import DEVNULL
from network_devices_list import network_devices
import paramiko
i = 0
#ip ping config
ip_list = ['10.10.10.200', '10.10.10.210', '10.10.10.10', '10.10.10.20' '192.168.10.102', '192.168.20.102', '192.168.30.101', '192.168.10.101', '10.10.10.1', '10.10.10.100', '192.168.20.210', '192.168.30.210']
bad_DNS = []
device_name = network_devices[i]['Device Name']
cmd = ['ping', '-c', '1', ip_list[i]]

#DNS settings check config
username = 'ubuntu'
password = 'ubuntu'
command = 'cat /etc/resolv.conf'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
temp_readout = ''

#ip ping
while i < len(ip_list):
    try:
        subprocess.run(cmd, stdout=DEVNULL, stderr=DEVNULL, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f'{ip_list[i]} is down!')
    try:
        client.connect(host = ip_list[i], username = username, password = password, timeout = 5)
        stdin, stdout, stderr = client.exec_command(command)
        temp_readout = stdout.read().decode()
        if '10.10.10.10' or '10.10.10.20' in temp_readout:
            print(f'{ip_list[i]} is pingable, and DNS settings are right!')
        else:
            ip_list.append(ip_list[i])
            print(f'{ip_list[i]} is pingable, but DNS settings are wrong!')
    except Exception as e:
        print(f'{ip_list[i]} Connection failed!')
    finally:
        client.close()
        i = i + 1