from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


ACTIVITY_LEVEL_CHOICES = (
    ('min', _('Minimal stress')),
    ('easy', _('Inactive')),
    ('ave', _('Average stress')),
    ('hard', _('Daily training')),
    ('int', _('Intensive training')),
    ('daily_int', _('Daily intensive training')),
    ('extra_hard', _('Extra hard training')),
)

GOALS_CHOICES = (
    ('keeping', _('Keeping fit')),
    ('losing', _('Losing weight')),
    ('ganing', _('Muscle gaininig')),
    ('preservation', _('Muscle reservation and fat burning')),
)

GENDER_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(_('Height'))
    weight = models.FloatField(_('Weight'))
    birth_date = models.DateField(_('Birth date'))
    age = models.IntegerField(_('Age'))
    activity = models.CharField(max_length=10, choices=ACTIVITY_LEVEL_CHOICES)
    goal = models.CharField(max_length=12, choices=GOALS_CHOICES)
    max_carbo = models.IntegerField(_('Carbohydrates'))
    max_fats = models.IntegerField(_('Fats'))
    max_calories = models.IntegerField(_('Calories'))
    max_proteins = models.IntegerField(_('Proteins'))
    registraion_date = models.DateField(
        _('Registraion date'),
        auto_now_add=True
    )
