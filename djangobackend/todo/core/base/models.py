import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Todo(models.Model):
    value = models.TextField()
    checked = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='todos', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('value', 'owner',)

    def __str__(self):
        if not self.checked:
            c = "☐"
        else:
            c = "☑"
        return f"{c} {self.value}"


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
