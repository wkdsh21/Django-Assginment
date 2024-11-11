from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from app.models import ToDoList


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def todo_list(request):
    todolist=ToDoList.objects.all()
    todolist=[{"id":todo.id, "title":todo.title} for todo in todolist]
    context = {"todolist":todolist}
    return render(request, "todo_list.html", context)

@login_required(login_url='login')
def todo_info(request, todo_id):
    todo = get_object_or_404(ToDoList, pk=todo_id)
    context = {"todo":{
        "title":todo.title,
        "description":todo.description,
        "start_date":todo.start_date,
        "end_date":todo.end_date,
        "is_complete":todo.is_complete,
        "created_at":todo.created_at,
        "modified_at":todo.modified_at,
    }}
    return render(request, "todo_info.html", context)