import cloudinary.uploader
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_to_new_user(email):
    subject = f"Welcome {email} to MyEventWorld"
    message = "Welcome to MyEventWorld. I`m delighted you`ve decided to register im my first web-site try. I hope you enjoy it and i`ll love to receive a feedback to improve my developer skills. Have Fun :)"

    send_mail(
        subject,
        message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(email,)
    )


@shared_task
def remove_entity_avatar_on_deletion_or_update(entity_avatar):
    cloudinary.uploader.destroy(entity_avatar)
