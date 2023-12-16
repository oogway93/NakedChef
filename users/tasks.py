from celery import shared_task

from users.service import send_contact_email_message


@shared_task
def send_contact_email_message_task(subject, user_id):
    return send_contact_email_message(subject, user_id)
