from django.http import HttpResponse, JsonResponse

from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def index(request):
    titulo = "Django Course!!"
    return render(request,'index.html',{
        'tittle' : titulo
    })

def about(request):
    username = 'Samuel';
    return render(request, 'about.html',{
        'username' : username
    })

def hello(request,username):
    return HttpResponse("<h1>Hello World, %s</h1>"%username)


def projects(request):
    # projects = list(Project.objects.values())
    
    projects = Project.objects.all()
    
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html',{
        'projects' : projects
    })

def tasks(request):
    tasks = Task.objects.all()
    # task = get_object_or_404(Task,id=id)   
    # return HttpResponse("task: %s"%task.title)
    return render(request, 'tasks/tasks.html',{
        'tasks' : tasks
    })
    
def createTask(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id = 2)
        return redirect('tasks')
    
def createProject(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    

def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        'project' : project,
        'tasks' : tasks
    })