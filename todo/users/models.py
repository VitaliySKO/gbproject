from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    username = models.CharField(blank=True, null=True, max_length=150, unique=False,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']