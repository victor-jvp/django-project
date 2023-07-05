from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = "Django course!!"
    return render(request, "index.html", {
        "title": title
    })


def about(request):
    username = "Victor"
    return render(request, "about.html", {
        "username": username
    })


def hello(request, username):
    return HttpResponse("<h1>Hola %s</h1>" % username)


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


def create_task(request):
    if request.method == "GET":
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == "GET":
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
