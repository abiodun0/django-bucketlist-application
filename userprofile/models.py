from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User,related_name='profile')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    about = models.TextField(max_length=1200,blank=True)
    image = models.TextField(max_length=1200,blank=True)