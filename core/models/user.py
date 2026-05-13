from django.contrib.auth.models import AbstractUser  
from django.db import models  
from django.conf import settings

User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')