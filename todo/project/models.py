from django.db import models

from users.models import CustomUser


class Project(models.Model):
    name_project = models.CharField(max_length=64)
    url_project = models.URLField(max_length=200, blank=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name_project


class TODO(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    name_todo = models.CharField(max_length=64)
    text_todo = models.TextField()
    date_create_todo = models.DateTimeField(auto_now_add=True)
    date_update_todo = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    status_todo = models.BooleanField(default=True)

    def __str__(self):
        return self.name_todo
