from meeting_website.celery import app

from .utils import send_new_letter


@app.task
def send_new_email(email: str, theme: str, message: str):
    send_new_letter(email, theme, message)
