from todolist.models import MyTask
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = MyTask
        fields = [
            'title',
            'description',
        ]
    