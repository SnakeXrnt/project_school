
import os
import smtplib
from email.message import EmailMessage
from datetime import*

EMAIL_ADDRESS = 'tokoterangjaya2@gmail.com'
EMAIL_PASSWORD = 'Ethanbas17'
now = str(datetime.now())

msg = EmailMessage()
msg['Subject'] ='Struk pembelanjaanmu'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'ethanbastian11@gmail.com'
msg.set_content(now)

files = ['C:\github\Tkinter\KasirToko(GUI)\Report\LOGIN SAVE INFO.pdf']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)


    smtp.send_message(msg)
