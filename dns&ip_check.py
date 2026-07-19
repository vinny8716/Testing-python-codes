import subprocess
from network_devices_list import network_devices
bad_ips = []
for device in network_devices:
    if subprocess.call(['ping', '-c', '1', device['Device Address']]) == 0:
        print('SUCCESS: {device} is reachable'.format(device=device['Device Address']))
    else:
        print('FAILURE: {device} is not reachable'.format(device=device['Device Address']))
        bad_ips.append(device)