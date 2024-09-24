from django.shortcuts import render
from .models import Todos

# Create your views here.
def landing(request):
    todos = Todos.objects.all()

    context = {
        "title": "Welcome to the To-Do List App",
        "todo": todos.first()
    }
    return render(request, 'landing.html', context)