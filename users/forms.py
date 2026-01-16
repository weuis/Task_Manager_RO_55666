from django.contrib.auth import get_user_model
from django import forms
from .models import TaskAssignment

User = get_user_model()


class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = ["user"]