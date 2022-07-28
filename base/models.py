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
    profile_picture = models.ImageField(upload_to='uploads/profile_pictures',
                                        default='uploads/profile_pictures/default.png',
                                        blank=True, null=True)
    location = models.CharField(max_length=500)
    about_yourself = models.TextField(max_length=1000, blank=True, null=True)
    profession = models.CharField(max_length=500, blank=True, null=True)
    instagram_link = models.CharField(max_length=500, blank=True, null=True)
    linkedin_link = models.CharField(max_length=500, blank=True, null=True)
    github_link = models.CharField(max_length=500, blank=True, null=True)
    portfolio_link = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Projects(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    thumbnail = models.ImageField(upload_to='uploads/project_thumbnails',
                                  default='uploads/profile_pictures/default.png',
                                  blank=True)
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=80)
    description = RichTextField()
    live_link = models.CharField(max_length=1000, blank=True, null=True)
    github_link = models.CharField(max_length=1000, blank=True, null=True)
    techstack = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Skill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    brief = models.TextField(max_length=500, blank=True, null=True)
