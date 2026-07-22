import subprocess
from network_devices_list import network_devices
dns_list = ['ns1.d522.wgu.internal', 'ns2.d522.wgu.internal', 'db.d522.wgu.internal', 'api.d522.wgu.internal', 'svr1.d522.wgu.internal', 'svr2.d522.wgu.internal']
good_ips = [network_devices[2]['Device Address'], network_devices[3]['Device Address'], network_devices[1]['Device Address'], network_devices[0]['Device Address'], network_devices[10]['Device Address'], network_devices[11]['Device Address']]
i = 0
bad_dns = []
dns_temp = ''
while i < len(dns_list):
    host = dns_list[i]
    output = subprocess.check_output(['ping', '-c', '1', host])
    output = output.decode('utf-8')
    dns_temp = good_ips[i]
    if dns_temp in output:
        print(dns_list[i], 'DNS settings are good')
    else:
        print(dns_list[i], 'DNS settings are not working!')
        bad_dns.append(good_ips[i])
    i = i + 1
