from django.conf import settings
from django.core.mail import EmailMessage

from celery import shared_task


@shared_task
def send_email(content, to):
    try:
        subject = 'Welcome to MyProject'
        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(subject, content, email_from, to,)
        email.content_subtype = "html"
        email.send()
        print("sended mail")
    except Exception as e:
        print(e)
