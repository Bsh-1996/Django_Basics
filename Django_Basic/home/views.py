from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def home(request):

    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})
