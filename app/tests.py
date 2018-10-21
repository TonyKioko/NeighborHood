from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# Create your tests here.
class NeighborhoodTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='tony')
        self.user.save()
        self.hood = Neighborhood(name='Karen',location='Nairobi',description="hood of hoods",photo='photo.url',user=self.user)
        self.hood.create_neighborhood()


    def tearDown(self):
        Neighborhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Neighborhood))

    def test_save_method(self):
        self.hood.create_neighborhood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_method(self):
        self.hood.create_neighborhood()
        self.hood.delete_neighborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood) == 0)

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.hood = Neighborhood(name='karen')
        self.hood.save()
        self.user = User(username='tony')
        self.user.save()
        self.profile = Profile(photo='black and white',bio='test bio',email="abc@xyz.com",user=self.user,neighborhood=self.hood)
        self.profile.save_profile()


    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)
