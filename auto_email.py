import smtplib
from email.message import EmailMessage
from dns_ip_check import bad_dns
from network_devices_list import network_devices
import datetime

#email config
stmp_s = 'smtp.d522.wgu.internal'
port = 1025
sender = 'ITDesk@mailhog.com'
password = ''
receiver = 'Stakeholders@mailhog.com'
#email massage
i = 0
while i < len(bad_dns):
    Device_name = ''
    for device in network_devices:
        if bad_dns[i] in device['Device Address']:
              Device_name = device['Device Name']
        else:
             pass
    IP_Address = bad_dns[i]
    Timestamp = datetime.datetime.now()
    msg = EmailMessage()
    msg['Subject'] = 'URGENT: Device Compromise Detected—Immediate Attention Required'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content('Dear Stakeholders,\n'
    '\n'
    'This is an automated alert to inform you that the following device(s) have been identified as compromised during the recent network scan:\n'
    '\n'
    f'Device Name: {Device_name}\n'
    f'IP Address: {IP_Address}\n'
    f'Last Checked: {Timestamp}\n'
    '\n'
    'Immediate investigation and remediation are recommended to prevent further impact.\n'
    '\n'
    'If you have any questions or require additional information, please contact the IT support team.\n'
    '\n'
    'Best regards,\n'
    'Network Monitoring System')



#trying to send
    try:
        with smtplib.SMTP(stmp_s, port) as s:
            s.login(sender, password)
            s.send_message(msg)
        print("email sent!")
    except Exception as e:
            print(f'ERROR: {e}')
    i = i + 1