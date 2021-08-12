from django import contrib, forms
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
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
            return redirect('profiles')

        else:

            messages.error(request, "username or password is not correct")

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, "logout success")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profiles = Profile.objects.get(id=pk)
    context = {
        'profile': profiles
    }
    return render(request, 'users/user-profile.html', context)
