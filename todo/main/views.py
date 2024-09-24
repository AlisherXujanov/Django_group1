from django.shortcuts import render

# Create your views here.
def landing(request):
    context = {
        "title": "Welcome to the To-Do List App"
    }
    return render(request, 'landing.html', context)