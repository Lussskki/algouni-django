from django.shortcuts import render

# Create your views here.

def dropdown(request):
    options = ['Select a category','Umberto eco','George orwell', 'Alan moore']
    return render(request, 'dropdown.html', {'options': options})
