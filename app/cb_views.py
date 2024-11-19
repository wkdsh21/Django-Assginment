from keyword import kwlist

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import Http404

from app.models import ToDoList


class TodoListView(LoginRequiredMixin,ListView):
    model = ToDoList
    template_name = 'todo/todo_list.html'
    paginate_by = 10
    ordering = ('-created_at',)
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(author = self.request.user)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))

        return queryset

class TodoDetailView(LoginRequiredMixin,DetailView):
    model = ToDoList
    template_name = "todo/todo_info.html"
    pk_url_kwarg = 'todo_id'
    def get_object(self):
        object = super().get_object()
        if not self.request.user.is_superuser and object.author != self.request.user:
                raise Http404("permission denied")
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = context.get('object').__dict__
        return context

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = ToDoList
    template_name = "todo/todo_create.html"
    fields = ('title', 'description', 'start_date', 'end_date')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('cbv:todo_info' ,kwargs = {'todo_id': self.object.id})

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = ToDoList
    pk_url_kwarg = 'todo_id'
    template_name = "todo/todo_update.html"
    fields = ('title', 'description', 'start_date', 'end_date', 'is_complete')

    def get_object(self):
        object = super().get_object()
        if not self.request.user.is_superuser and object.author != self.request.user:
            raise Http404("permission denied")
        return object

    def get_success_url(self):
        return reverse_lazy('cbv:todo_info',kwargs = {'todo_id': self.object.id})

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDoList
    pk_url_kwarg = 'todo_id'

    def get_object(self):
        print(self.request.method)
        object = super().get_object()
        if not self.request.user.is_superuser and object.author != self.request.user:
            raise Http404("permission denied")
        return object

    def get_success_url(self):
        return reverse_lazy('cbv:todo_list')
