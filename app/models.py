from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class neighborhood(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    location=models.CharField(max_length=100, null=True, blank=True)
    description = HTMLField()
    user = models.ForeignKey(User, null=True)
