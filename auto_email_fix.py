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
fix1 = [network_devices[10]['Device Name'], network_devices[10]['Device Address']]
fix1_hostname = ''
fix2 = [network_devices[11]['Device Name'], network_devices[11]['Device Address']]
fix2_hostname = ''
#email massage
Timestamp = datetime.datetime.now()
msg = EmailMessage()
msg['Subject'] = 'URGENT: Device Compromise Detected—Immediate Attention Required'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('Dear Stakeholders,\n'
'\n'
'This is an automated notification to inform you that the DNS service issue and all related device compromises have been successfully resolved. The following devices were affected and have now been remediated:\n'
'\n'
f'{fix1[0]}, {fix1_hostname}, {fix1[1]}\n'
f'{fix2[0]}, {fix2_hostname}, {fix2[1]}\n'
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
