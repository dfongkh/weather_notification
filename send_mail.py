import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#setting username and password for logging to account for sending email
username = 'example@gmail.com'
password = 'your_password'

def send_mail(text='Email Body', subject='Current Weather', from_email='Automatic Weather <example@gmail.com>', to_emails=None, html=None):
    #assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_emails
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(text, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()

    # login
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo() # config by default
    server.starttls() # secure connection
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)


    server.quit()
