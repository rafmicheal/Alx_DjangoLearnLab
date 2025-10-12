from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


@receiver(post_save, sender=Comment)
def notify_on_comment(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.author,
            verb='commented on your post',
            target_content_type=ContentType.objects.get_for_model(
                instance.post),
            target_object_id=str(instance.post.pk)
        )
