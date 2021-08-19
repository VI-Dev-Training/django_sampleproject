from django.db import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'first_name': 'Name'
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'username',
            'bio',
            'profile_image'
        ]

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'email','subject', 'body']