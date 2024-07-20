from django.shortcuts import redirect, render

from .models import Task

# Create your views here.
def todo_index(request):
    queriset = Task.objects.all()
    return render(request, 'todo_list.html',{'data': queriset})     

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title = title) 
    return redirect("todo_list")    

def delete_task(request, task_id):
    Task.objects.filter(pk = task_id).delete()
    return redirect("todo_list")

def edit_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    task.completed = True
    task.save()
    return redirect("todo_list")