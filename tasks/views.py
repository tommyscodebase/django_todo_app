from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', {
        'tasks': tasks,
    })

def completed(request):
    completed_tasks = Task.objects.filter(completed=True)

    return render(request, 'completed.html', {
        'tasks': completed_tasks,
    })

def remaining(request):
    remaining_tasks = Task.objects.filter(completed=False)
    return render(request, 'remaining.html', {
        'tasks': remaining_tasks,
    })

def add_task(request):
    return render(request, 'add_task.html')

def delete_task(request):
    return render(request, 'delete.html')

def task_detail(request):
    return render(request, 'task_detail.html')
