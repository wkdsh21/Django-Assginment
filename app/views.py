from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from app.forms import TodoForm, TodoUpdateForm
from app.models import ToDoList


# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required(login_url="login")
def todo_list(request):
    todolist=request.user.todolist_set
    print(type(todolist))
    q = request.GET.get('q')
    if q:
        todolist = todolist.filter(Q(title__icontains=q) | Q(description__icontains=q))
    else:
        todolist=todolist.all()
    paginator = Paginator(todolist, 10)  # Paginator 객체를 인스턴스화 합니다.
    page_number = request.GET.get('page')  # GET 요청으로부터 page에 담긴 쿼리 파라미터 값을 가져옴
    page_obj = paginator.get_page(page_number)  # 가져온 페이지 숫자를 이용해서 페이지에 대한 오브젝트를 가져옵니다.
    context = {
        'page_obj': page_obj
    }
    return render(request, 'todo/todo_list.html', context)


@login_required(login_url="login")
def todo_info(request, todo_id):
    todo = get_object_or_404(ToDoList, pk=todo_id)
    context = {"todo": todo.__dict__}
    return render(request, "todo/todo_info.html", context)


@login_required(login_url="login")
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.author = request.user
        todo.save()
        print(todo.id)
        return redirect(reverse("todo_info", kwargs={"todo_id": todo.id}))
    context = {"form": form}
    return render(request, "todo/todo_create.html", context)

@login_required(login_url="login")
def todo_update(request, todo_id):
    todo=get_object_or_404(ToDoList, pk=todo_id, author=request.user)
    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    context = {"form": form}
    return render(request, "todo/todo_update.html" ,context)

@login_required(login_url="login")
def todo_delete(request, todo_id):
    todo = get_object_or_404(ToDoList, id=todo_id, user=request.user)
    todo.delete()
    return redirect(reverse('todo_list'))