from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    creation_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} by {self.author.first_name} {self.author.last_name}'

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.title == 'Model Invalid Title':
            raise ValidationError({'title': 'Invalid title at the model level.'})
