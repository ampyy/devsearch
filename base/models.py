from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
        user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE, )
        uuid = models.UUIDField(default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=30, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    thumbnail = models.ImageField(upload_to='uploads/project_thumbnails', default='uploads/profile_pictures/default.png',
                                blank=True)
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=500)
    description = RichTextField()


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    brief = models.TextField(max_length=500)