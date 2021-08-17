from django import contrib, forms
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .utils import searchProfiles
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
# Create your views here.


def loginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'Username not found')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('user-account')

        else:

            messages.error(request, "username or password is not correct")

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, "logout success")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Creation Successfull")

            login(request, user)
            return redirect('profiles')

        else:
            messages.success(request, "something went wrong please try again")

    context = {
        'page': page,
        'form': form
    }

    return render(request, 'users/login.html', context)


def profiles(request):
    profiles, search_query  = searchProfiles(request)
    context = {
        'profiles': profiles,
        'search_query': search_query
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profiles = Profile.objects.get(id=pk)
    context = {
        'profile': profiles
    }
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context  ={
        'profile' : profile
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form  = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-account')
    context = {
       'form': form
    }
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def addSkills(request):
    profile = request.user.profile
    form  = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'skill was added successfully')
            return redirect('user-account')
    context = {
        'form': form
    }
    return render(request, 'users/skill-form.html', context)


@login_required(login_url='login')
def updateSkills(request, pk):
    profile = request.user.profile
    skill  = profile.skill_set.get(id=pk)
    form  = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'update was successfull')
            return redirect('user-account')
    context = {
        'form': form
    }
    return render(request, 'users/skill-form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'skill deleted succesfuly')
        return redirect('user-account')
    context = {
      'object': skill
    }
    return render(request, 'users/delete-skill.html', context)