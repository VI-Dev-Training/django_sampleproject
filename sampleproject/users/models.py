from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True,null=True)
    bio  = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'messages')
    sender_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created_date']