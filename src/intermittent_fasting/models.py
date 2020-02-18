from django.db import models
from django.contrib.auth.models import User


class Fasting(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    users = models.ForeignKey(
        User,
        related_name='intermittent_fasting',
        on_delete=models.CASCADE
    )
