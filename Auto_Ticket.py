import requests
import json
from network_devices_list import network_devices
from dns_ip_check import bad_dns
i = 0

while i < len(bad_dns):
    devie_name = ''
    token = 'vGkbXkGLqQSo7YLflp9DutuG8st4xdPPF7wnTcwB0FE'
    for device in network_devices:
        if bad_dns[i] in device['Device Address']:
              device_name = device['Device Name']
        else:
             pass
    url = 'http://helpdesk.d522.wgu.internal:5000/api/tickets'
    headers = {'Authorization' : f'Bearer {token}',
               'Content-Type' : 'application/json'
               }
    payload = {
        "assigned_to": "John Smith",
        "description": "DNS settings are poisoned!",
        "priority": "high",
        "requester_email": "ITDesk@mailhog.com",
        "status": "open",
        f"title": "{device_name} is compromised"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Ticket created")
        print(response.json)
        print(f'Status Code: {response.status_code}')
    else:
        print('something went wrong')
        print(f'Status Code: {response.status_code}')
    i = i + 1