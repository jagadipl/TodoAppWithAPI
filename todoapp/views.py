from django.shortcuts import render
from .models import Todo

# Create your views here.
def homepage(request):
    todos = Todo.objects.all()
    return render(request,'todoapp/todo_list.html',{
        'todos': todos
        
    })