from django.db import models

from django.core.validators import MinValueValidator

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from import_export import resources


class Activity(models.Model):
    icon = models.ImageField(_('Icon'))
    name = models.CharField(_('Activity name'), max_length=80)
    сonsumption = models.FloatField(
        _('Consumption'),
        validators=[MinValueValidator(0.0)]
    )
    user = models.ManyToManyField(
        User,
        through='ActivityTime',
        related_name='activities',
        blank=True,
    )

    def __str__(self):
        return self.name


class ActivityTime(models.Model):
    minutes = models.PositiveIntegerField(
        _('Activity Time (Minutes)')
    )
    user = models.ForeignKey(
        User,
        related_name='activity_time',
        on_delete=models.CASCADE
    )
    activity = models.ForeignKey(
        Activity,
        related_name='activity_time',
        on_delete=models.CASCADE
    )


class CustomUserActivity(models.Model):
    name = models.CharField(_('Custom Activity name'), max_length=80)
    сonsumption = models.FloatField(
        _('Consumption'),
        validators=[MinValueValidator(0.0)]
    )
    user = models.ForeignKey(
        User,
        related_name='custom_activities',
        on_delete=models.CASCADE
    )
    activity_time_minutes = models.PositiveIntegerField(
        _('Activity Time (Minutes)'),
        default=0
    )

    def __str__(self):
        return self.name
