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
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def blog_list(request):
    book_text=''

    for i in range(0, 10):
        book_text += f'book {i}'
    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지 입니다'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'{lang} 언어 페이지 입니다.')
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("book_list/", blog_list),
    path("book_list/<int:num>", book),
    path("language/<str:lang>", language),
]
