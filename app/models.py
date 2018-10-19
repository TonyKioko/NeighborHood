from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    location=models.CharField(max_length=100, null=True, blank=True)
    description = HTMLField()
    photo = models.ImageField(upload_to='profpics/',default='NO IMAGE')
    user = models.ForeignKey(User, null=True)

    def save_hood(self):
        self.save()
    def __str__(self):
        return self.name
class Profile(models.Model):
    bio = HTMLField(default="Noisy Neigbhors")
    photo = models.ImageField(upload_to='profpics/',default='NO IMAGE')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True,blank=True)
    email = models.CharField(max_length=60,blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
class Business(models.Model):
    name=models.CharField(max_length=40, null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    @classmethod
    def search_by_name(cls,search_term):
    	businesses = cls.objects.filter(name__icontains=search_term)
    	return businesses

class Alert(models.Model):
	alert=HTMLField(default="")
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	neighbor_hood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True,blank=True)
	date_posted = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = HTMLField(default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    alert=models.ForeignKey(Alert, on_delete=models.CASCADE)
