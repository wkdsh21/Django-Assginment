from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.urls import reverse


# Create your views here.


def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse("login"))
    context = {"form": form}
    return render(request, "signup.html", context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        user_login(request, form.get_user())
        return redirect(reverse("todo_list"))
    context = {"form": form}
    return render(request, "login.html", context)
