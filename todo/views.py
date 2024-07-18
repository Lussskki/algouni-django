from django.shortcuts import render

from .models import Task

# Create your views here.
def todo_index(request):
    queriset = Task.objects.all()
    return render(request, 'todo_list.html',{'data': queriset})     