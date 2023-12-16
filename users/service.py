from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from main import settings

User = get_user_model()


def send_contact_email_message(subject, user_id):
    """
    Функция отправки письма из формы обратной связи
    """
    user = User.objects.get(id=user_id) if user_id else None
    email = EmailMessage(subject,
                         render_to_string("celery/email.html", {"name": user.first_name}),
                         settings.EMAIL_HOST_USER,
                         [user.email])
    email.content_subtype = 'html'
    email.send()
