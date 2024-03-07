from project.celery import app
from .send_email import send_email


@app.task
def send_email_task(subject, user_email, secret_code):
    try:
        send_email(subject, user_email, secret_code)

    except Exception as _ex:
        return _ex
