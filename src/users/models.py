from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

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
    ('gaining', _('Muscle gaininig')),
    ('preservation', _('Muscle preservation and fat burning')),
)

GENDER_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        unique=True,
        null=True
    )
    uid = models.CharField(max_length=28, null=True, blank=True)
    image = models.ImageField(
        _('Image'),
        upload_to='profile_image',
        blank=True
    )
    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )
    activity = models.CharField(
        _('Activity'),
        max_length=10,
        choices=ACTIVITY_LEVEL_CHOICES,
        blank=True
    )
    goals = models.CharField(
        _('Goals'),
        max_length=12,
        choices=GOALS_CHOICES,
        blank=True
    )
    age = models.IntegerField(_('Age'), null=True, blank=True)
    height = models.FloatField(_('Height'), null=True, blank=True)
    weight = models.FloatField(_('Weight'), null=True, blank=True)
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)
    max_carbo = models.IntegerField(_('Carbohydrates'), null=True, blank=True)
    max_fats = models.IntegerField(_('Fats'), null=True, blank=True)
    max_calories = models.IntegerField(_('Calories'), null=True, blank=True)
    max_proteins = models.IntegerField(_('Proteins'), null=True, blank=True)
    water_count = models.IntegerField(_('Water'), null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_age(self):
        import datetime
        self.age = int((datetime.date.today() - self.birthday).days / 365.25)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.profile.save()
