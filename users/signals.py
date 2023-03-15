from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver #recieve the send signal and perform the action thtis to create the profile for tht user
from.models import Profile

@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):#sender,the userbeen saved as instance,boolean value,keywords arguments-if having any additional
     if created:
          Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
     instance.profile.save()
