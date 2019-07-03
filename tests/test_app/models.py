from django.db import models
from django.core.exceptions import ValidationError


class Item(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if "Monty Python" in self.content:
            raise ValidationError("Please! No more monty python jokes.")

        super(Item, self).save(*args, **kwargs)
