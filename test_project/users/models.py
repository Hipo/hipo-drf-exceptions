from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False, help_text='Only staff users can access Django Admin.')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if self.first_name == "invalid_model_first_name":
            raise ValidationError({"first_name": "Invalid entry at the model level."})
