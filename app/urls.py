from django.urls import path

from app.cb_views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

app_name = 'cbv'

urlpatterns = [
    path("todo/", TodoListView.as_view(), name="todo_list"),
    path("todo/<int:todo_id>/", TodoDetailView.as_view(), name="todo_info"),
    path("todo/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:todo_id>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:todo_id>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]