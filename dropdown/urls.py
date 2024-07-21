from django.urls import path
from .views import dropdown

urlpatterns = [
    path('', dropdown)
]