from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=20, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)

    # objects = BaseUserManager()
