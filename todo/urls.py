from django.urls import path
from .views import todo_index, add_task

urlpatterns = [ 
    path('', todo_index, name = 'todo_list'), 
    path('add/', add_task , name = 'add_task')
]     