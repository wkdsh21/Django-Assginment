"""
URL configuration for djangoProject2 project.

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
from django.urls import path
from django.http import HttpResponse
from djangoProject2.fake_db import user_db

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def user_list(request):
    user_dict={"users":[],}
    for idx,user_name in user_db.items():
        user_dict["users"].append((idx,user_name['이름']))
    return render(request, "user_list.html", user_dict)

def user_info(request, user_id):
    user=user_db[user_id]
    return render(request, "user_info.html", user)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("users/",user_list),
    path("users/<int:user_id>",user_info),
    # path("book_list/<int:num>", book),
]
