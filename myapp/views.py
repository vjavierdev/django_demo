from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.

def index(request):
    title = 'Welcome to Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello World  "+ username+"</h1>")

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'projects': projects
})

def tasks(request):

    tasks = list(Task.objects.all())
    return render(request, 'tasks.html', {
        'tasks': tasks
})
    ##task = get_object_or_404(Task, id=id)
    ##return HttpResponse('Tasks: %s' % task.title)


