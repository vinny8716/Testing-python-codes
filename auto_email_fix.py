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
Timestamp = datetime.datetime.now()
msg = EmailMessage()
msg['Subject'] = 'RESOLVED: DNS Service Issue and Device Compromise—All Issues Remediated'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('Dear Stakeholders,\n'
'\n'
'This is an automated notification to inform you that the DNS service issue and all related device compromises have been successfully resolved. The following devices were affected and have now been remediated:\n'
'\n'
'PC3\n'
'SVR1\n'
'SVR2\n'
'\n'
'No further action is required at this time. If you have any questions or concerns, please contact the IT support team.\n'
'\n'
'Thank you for your attention.\n'
'\n'
'Best regards,\n'
'Network Monitoring System\n')



#trying to send
    try:
        with smtplib.SMTP(stmp_s, port) as s:
            s.login(sender, password)
            s.send_message(msg)
        print("email sent!")
    except Exception as e:
            print(f'ERROR: {e}')
    i = i + 1
