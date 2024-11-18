from django import forms

from app.models import ToDoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = (
            "is_complete",
            "created_at",
            "modified_at",
            "author",
        )
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = (
            "created_at",
            "modified_at",
            "author",
        )
