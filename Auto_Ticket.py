import requests
import json
from network_devices_list import network_devices
from availability_test import bad_ips
i = 0

while i < len(bad_ips):
    device_name = ['PC3', 'SVR1', 'SVR2']
    token = 'vGkbXkGLqQSo7YLflp9DutuG8st4xdPPF7wnTcwB0FE'
    url = 'http://helpdesk.d522.wgu.internal:5000/api/tickets'
    headers = {'Authorization' : f'Bearer {token}',
               'Content-Type' : 'application/json'
               }
    payload = {
        "assigned_to": "John Pork",
        "description": "Host is down, get the host up and running at the earliest convenience",
        "priority": "high",
        "requester_email": "ITDesk@mailhog.com",
        "status": "open",
        "title": f"{device_name[i]} is down!"
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
