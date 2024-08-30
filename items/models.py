from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.name == 'Invalid Name':
            raise ValueError("This name is not allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
