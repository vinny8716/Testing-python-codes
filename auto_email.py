import smtplib
from email.message import EmailMessage
from IP_CHECK import bad_DNS
from network_devices_list import network_devices
import datetime

#email config
stmp_s = 'smtp.d522.wgu.internal'
port = 1025
sender = 'ITDesk@mailhog.com'
password = ''
receiver = 'Stakeholders@mailhog.com'
Device_name = ['PC3', 'SVR1', 'SVR2']
#email massage
i = 0
while  i < len(bad_DNS):
    Device_temp = Device_name[i]
    IP_Address = bad_DNS[i]
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
