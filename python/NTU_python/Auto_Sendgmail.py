#! /usr/bin/python3.5
import requests
import smtplib
from email.mime.text import MIMEText

#Gmail
sender = 'crayflames@gmail.com'
receiver = 'crayflames@gmail.com'
content = 'everything \n second line'
msg =MIMEText(content.encode('utf-8'),_charset='utf-8')
msg['Subject'] = 'Subject'
msg['From'] = sender
msg['receiver'] = receiver

conn = smtplib.SMTP('smtp.gmail.com:587')
conn.ehlo()
conn.starttls()
conn.login(sender,'mydnsaqwkqepojso')
conn.sendmail(sender,
			  receiver,
			  msg.as_string())
conn.quit()

# LINE
content = "你好,我是來自 Python 的訊息，啾咪！"

## Line Notify
lineUrl = "https://notify-api.line.me/api/notify"
token = "RNeFGMxis9g8JTmOQHDBovWR87elsHCzm8Udb2Kvhtr"
headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

payload = {'message': content}
r = requests.post(lineUrl, headers = headers, params = payload)