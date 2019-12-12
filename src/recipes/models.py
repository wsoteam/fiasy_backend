from django.db import models

from products.models import Product

from django.utils.translation import ugettext_lazy as _

from multiselectfield import MultiSelectField


MEAL_CHOICES = (
    ('breakfast', _('Breakfast')),
    ('lunch', _('Lunch')),
    ('shack', _('Snack')),
    ('dinner', _('Dinner')),
)


class Recipe(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    full_info = models.TextField(_('Full info'), blank=True)
    image = models.ImageField(_('Image'), upload_to='recipe_image')
    meal = MultiSelectField(choices=MEAL_CHOICES, null=True)
    cooking_time = models.IntegerField(
        _('Cooking time'),
        blank=True,
        null=True
    )
    cooking_process = models.TextField(_('Cooking process'), blank=True)
    portion = models.FloatField(default=100)
    products = models.ManyToManyField(
        Product,
        verbose_name=_("Products"),
        blank=True,
        through='ProductAmount',
        related_name='products'
    )
    date = models.DateField(_('Date'), auto_now=True)

    kilojoules = models.FloatField(
        _('Kilojoules'),
        default=-1.0
    )
    calories = models.FloatField(
        _('Calories'),
        default=-1.0
    )
    proteins = models.FloatField(
        _('Proteins'),
        default=-1.0
    )
    carbohydrates = models.FloatField(
        _('Carbohydrates'),
        default=-1.0
    )
    sugar = models.FloatField(
        _('Sugar'),
        default=-1.0
    )
    fats = models.FloatField(
        _('Fats'),
        default=-1.0
    )
    saturated_fats = models.FloatField(
        _('Saturated fats'),
        default=-1.0
    )
    unsaturated_fats = models.FloatField(
        _('Unsaturated fats'),
        default=-1.0
    )
    cholesterol = models.FloatField(
        _('Cholesterol'),
        default=-1.0
    )
    cellulose = models.FloatField(
        _('Cellulose'),
        default=-1.0
    )
    sodium = models.FloatField(
        _('Sodium'),
        default=-1.0
    )
    pottasium = models.FloatField(
        _('Pottasium'),
        default=-1.0
    )
    premium = models.BooleanField(_('Premium'), default=False)
    is_moderated = models.BooleanField(_('Is moderated'), default=False)

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')

    def __str__(self):
        return self.name


class ProductAmount(models.Model):
    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        related_name='amount',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        blank=True,
        null=True,
        related_name='amount',
        on_delete=models.CASCADE
    )
    amount = models.FloatField(_('Amount'), default=0)

    def __str__(self):
        return self.product.name
