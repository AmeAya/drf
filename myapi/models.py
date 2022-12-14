from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Todo(models.Model):
    task = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True, blank=False)
    completed = models.BooleanField(default=False, blank=False)
    expire_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
