from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from products.models import Product

MEAL_CHOICES = (
    ('breakfast', _('Breakfast')),
    ('lunch', _('Lunch')),
    ('snack', _('Snack')),
    ('dinner', _('Dinner')),
)


class Meal(models.Model):
    meal = models.CharField(choices=MEAL_CHOICES, max_length=9)
    products = models.ManyToManyField(
        Product,
        verbose_name=_("Products"),
        related_name='meal_products',
        through='ProductAmount',
    )
    user = models.ForeignKey(
        User,
        related_name='meals',
        on_delete=models.CASCADE
    )


class ProductAmount(models.Model):
    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        related_name='meal_product_amount',
        on_delete=models.CASCADE
    )
    meal = models.ForeignKey(
        Meal,
        blank=True,
        null=True,
        related_name='meal_product_amount',
        on_delete=models.CASCADE
    )
    amount = models.FloatField(_('Amount'), default=0)
