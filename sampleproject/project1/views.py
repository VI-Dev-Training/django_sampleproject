from users.models import Profile
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.db.models import Q
from .models import Project, Review, Tag
from .forms import ProjectForm, addReviewForm

# Create your views here.


def project1(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains = search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(tags__in = tags)
    )

    context = {
        'project': projects,
        'search_query': search_query
    }
    return render(request, 'project1/project1.html', context)


def project2(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'project1/project2.html', {
        'project': projectObj
    })


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    projectForm = ProjectForm()
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
            project  = projectForm.save(commit=False)
            project.owner  = profile
            project.save()
            return redirect('project1')
    context = {
        'form': projectForm
    }
    return render(request, "project1/project-form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile  = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        projectForm = ProjectForm(request.POST,request.FILES, instance=project)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('project1')
    context = {
        'form': form
    }
    return render(request, "project1/project-form.html", context)



@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project1')
    context = {
        'object': project
    }
    return render(request, 'project1/delete-project.html', context)

@login_required(login_url="login")
def addReview(request, pk):
    form = addReviewForm()
    context = {
      'form': form
    }
    return render(request, 'project1/add-review.html', context)