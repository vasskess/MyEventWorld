from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from MyEventWorld.accounts.models import EventProfile
from MyEventWorld.events.models import Event
from MyEventWorld.accounts.tasks import send_email_to_new_user, remove_entity_avatar_on_deletion_or_update

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    """
    This will automatically creat a Profile, when a User is created
    """
    if created:
        user = instance
        profile = EventProfile.objects.create(
            user=user,
        )
        send_email_to_new_user.delay(instance.email)


@receiver(post_delete, sender=EventProfile)
def delete_user(sender, instance, **kwargs):
    """
    This will automatically delete a User, when a Profile is deleted and removes his avatar from Cloudinary
    """
    if instance.profile_avatar:
        remove_entity_avatar_on_deletion_or_update.delay(instance.profile_avatar.public_id)
    user = instance.user
    user.delete()


@receiver(pre_save, sender=EventProfile)
def delete_old_profile_avatar_on_update(sender, instance, **kwargs):
    """
    This will replace old Profile avatar with the new one in Cloudinary
    """
    if instance.profile_avatar:
        profile_avatar_to_remove = EventProfile.objects.get(pk=instance.pk).profile_avatar
        if profile_avatar_to_remove:
            remove_entity_avatar_on_deletion_or_update.delay(profile_avatar_to_remove.public_id)


@receiver(post_delete, sender=Event)
def delete_event_picture(sender, instance, **kwargs):
    """
        This will remove Event picture from Cloudinary when Event is deleted
    """
    if instance.event_picture:
        remove_entity_avatar_on_deletion_or_update.delay(instance.event_picture.public_id)


@receiver(pre_save, sender=Event)
def delete_old_event_picture_on_update(sender, instance, **kwargs):
    """
    This will replace old event picture with the new one in Cloudinary
    """
    if instance.event_picture:
        event_picture_to_remove = Event.objects.get(pk=instance.pk).event_picture
        if event_picture_to_remove:
            remove_entity_avatar_on_deletion_or_update.delay(event_picture_to_remove.public_id)
