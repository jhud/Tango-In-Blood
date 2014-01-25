from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save    

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile_users')
    avatar = models.URLField(blank=True, help_text="A URL link to your profile picture online. It should be 200x250 pixels.")
    bio = models.CharField(max_length=6000, blank=True, help_text="Say something about yourself which will be publically visible.")
    conversion_password = models.CharField(max_length=40, unique=True, blank=True, help_text="The password I use to convert others.")
    converted_by = models.ForeignKey(User, blank=True, null = True, related_name='profile_converted_bys')
    
# Automatically create profile if it doesn't exist    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Profile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

User.profile = property(lambda u: u.get_profile() )