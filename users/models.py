from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.text import slugify


class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)
    avatar = models.ImageField(upload_to="images/avatar/%Y/%m/%d/", default="images/avatar/default.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url (self):
        return reverse("profile", kwargs={"slug": self.slug})


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.username, slug=slugify(instance.username))


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()

