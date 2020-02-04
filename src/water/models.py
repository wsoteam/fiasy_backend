from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


class WaterDrinking(models.Model):
    amount = models.IntegerField(_('Amount'))
    timestamp = models.DateTimeField(_('Timestamp'), auto_now=True)
    user = models.ForeignKey(
        User,
        related_name='water_drinking',
        on_delete=models.CASCADE
    )
