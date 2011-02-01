from django.db import models

from django.contrib.auth.models import User
from basic.profiles.models import Profile

class LaunchReminder(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

# Top-level menu items
class MenuItem(models.Model):
    title = models.CharField(max_length=80)
    url = models.CharField(max_length=80)
    placement = models.IntegerField()
    
    def __str__(self):
        return self.title

# so that we don't have to continuously check to see if the profile has been created
User.get_profile = lambda self: Profile.objects.get_or_create(user=self)[0]
