from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #id the user account is deleted then it also deletes the profile
    location =models.CharField(max_length=100)

#when we try to acces any object from this model we should get the username

def _str_(self):
    return self.user.username
