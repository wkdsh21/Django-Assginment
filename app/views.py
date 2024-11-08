from django.http import HttpResponse
from django.shortcuts import render
from app.models import ToDoList


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def todo_list(request):
    todolist=ToDoList.objects.all()
    todolist=[{"id":todo.id, "title":todo.title} for todo in todolist]
    context = {"todolist":todolist}
    return render(request, "todo_list.html", context)

def todo_info(request, todo_id):
    todo=ToDoList.objects.get(pk=todo_id)
    context={"todo":{
        "title":todo.title,
        "description":todo.description,
        "start_date":todo.start_date,
        "end_date":todo.end_date,
        "is_complete":todo.is_complete,
        "created_at":todo.created_at,
        "modified_at":todo.modified_at,
    }}
    return render(request, "todo_info.html", context)