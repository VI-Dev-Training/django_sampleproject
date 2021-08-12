from django import forms
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm

# Create your views here.


def project1(request):
    projects = Project.objects.all()
    context = {
        'project': projects
    }
    return render(request, 'project1/project1.html', context)


def project2(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'project1/project2.html', {
        'project': projectObj
    })


def createProject(request):
    projectForm = ProjectForm()

    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('project1')
    context = {
        'form': projectForm
    }
    return render(request, "project1/project-form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
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


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project1')
    context = {
        'object': project
    }
    return render(request, 'project1/delete-project.html', context)