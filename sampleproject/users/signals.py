
from users.views import userAccount
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from django.contrib.auth.models import User
from .models import Profile

def createProfile(sender, instance, created, **kwargs):
    print("profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

def updateProfile(sender, instance, created, **kwargs):
    print("profile updated")
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        


def deleteUser(sender, instance, **kwargs):
    user = instance.User
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender = Profile)
post_delete.connect(deleteUser, sender=Profile)