from django.db import models

from django.contrib.auth.models import User


class BodyMeasurement(models.Model):
    weight = models.FloatField()
    chest = models.FloatField()
    waist = models.FloatField()
    hips = models.FloatField()
    user = models.ForeignKey(
        User,
        related_name='body_measurements',
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
