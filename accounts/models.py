import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):

    """Custom User model extends a pre-defined django AbstractUser model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
