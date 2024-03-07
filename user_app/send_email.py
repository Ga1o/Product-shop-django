import smtplib
from email.mime.text import MIMEText


def send_email(subject, email, message):
    sender = 'email-name@gmail.com'
    password = 'password'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(str(message))
        msg['Subject'] = subject
        msg['To'] = email
        server.sendmail(sender, email, msg.as_string())
        server.quit()

    except Exception as _ex:
        # TODO заменить принт на логирование
        print(f'{_ex}\nПроверьте email и пароль для подключения.')