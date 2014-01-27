import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save    
from pybb.profiles import PybbProfile

# Create your models here.

class Profile(PybbProfile):
    user = models.ForeignKey(User, related_name='profile_users')
    bio = models.CharField(max_length=6000, blank=True, help_text="Say something about yourself which will be publically visible.")
    conversion_password = models.CharField(max_length=40, unique=True, blank=True, help_text="The password I use to convert others.")
    converted_by = models.ForeignKey(User, blank=True, null = True, related_name='profile_converted_bys')
    
# Automatically create profile if it doesn't exist    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        passwd = instance.username + "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(4))
        profile, created = Profile.objects.get_or_create(user=instance, conversion_password=passwd)  

post_save.connect(create_user_profile, sender=User) 

User.profile = property(lambda u: u.get_profile() )