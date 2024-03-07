import smtplib
from email.mime.text import MIMEText
import logging


logging.basicConfig(filename='app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


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

    except Exception as e:
        logger.error(f"Ошибка в получении доступа: {e}", exc_info=True)
