from django.urls import path
from .views import todo_index, add_task, delete_task, edit_task

urlpatterns = [ 
    path('', todo_index, name = 'todo_list'), 
    path('add/', add_task , name = 'add_task'),
    path('delete/<int:task_id>', delete_task, name = 'delete_task'),
    path('edit/<int:task_id>', edit_task, name = 'edit_task'),
]      