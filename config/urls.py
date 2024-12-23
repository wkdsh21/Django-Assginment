"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse
from app import views
from app.views import todo_delete, todo_update
from member import views as model_views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("todo/", views.todo_list, name="todo_list"),
    path("todo/<int:todo_id>/", views.todo_info, name="todo_info"),
    path("accounts/login/", model_views.login, name="login"),
    path("accounts/signup/", model_views.sign_up, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("todo/create/", views.todo_create, name="todo_create"),
    path("todo/<int:todo_id>/update/", views.todo_update, name="todo_update"),
    path("todo/<int:todo_id>/delete/", views.todo_delete, name="todo_delete"),
    path("cbv/", include("app.urls"))
]
