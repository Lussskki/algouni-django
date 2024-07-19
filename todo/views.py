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