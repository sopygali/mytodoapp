from django.forms import ModelForm
from .models import Task, User, Mark # did we change it in UserForm
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'creator', 'completer', 'email', 'password1', 'password2' ]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['host']

class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'
        exclude = ['user', 'task']