from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    is_finished = models.BooleanField(default=False)