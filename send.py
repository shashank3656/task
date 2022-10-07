import email.mime.text
import smtplib

username = 'nookala3656@gmail.com'
password = 'pjuyhgioilukcyjq'
hostname = 'smtp.gmail.com'

msg = email.mime.text.MIMEText('Your Website Server is down')
msg['Subject'] = 'Server Down'
msg['From'] = 'nookala3656@gmail.com'
msg['To'] = 'shashankgowtham12@gmail.com'

server = smtplib.SMTP(hostname, 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(
        'abc@gmail.com',
        ['shashankgowtham12@gmail.com'],
        msg.as_string(),
        )
server.close()
