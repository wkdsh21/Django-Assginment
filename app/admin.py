from django.contrib import admin

# Register your models here.

from django.contrib import admin
from app.models import ToDoList


# (A)
@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "start_date", "end_date"]
    list_display_links = ["title"]
    list_filter = ["is_complete", "start_date"]
