from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def home(request):

    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})

