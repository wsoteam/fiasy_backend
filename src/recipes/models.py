from django.db import models

from products.models import Product

from django.utils.translation import ugettext_lazy as _


class Recipe(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    full_info = models.TextField(_('Full info'), blank=True)
    image = models.ImageField(_('Image'), upload_to='recipe_image')
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
    premium = models.BooleanField(_('Premium'), default=False)
    date = models.DateField(_('Date'), auto_now=True)
    is_moderated = models.BooleanField(_('Is moderated'), default=False)

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')

    def __str__(self):
        return self.name

    def get_ingredients_elements(self):
        for product in self.products.all():
            kilojoules = -1.0 if product.kilojoules == -1.0 \
                else product.kilojoules * self.portion
            calories = -1.0 if product.calories == -1.0 \
                else product.calories * self.portion
            proteins = -1.0 if product.proteins == -1.0 \
                else product.proteins * self.portion
            carbohydrates = -1.0 if product.carbohydrates == -1.0 \
                else product.carbohydrates * self.portion
            sugar = -1.0 if product.sugar == -1.0 \
                else product.sugar * self.portion
            fats = -1.0 if product.fats == -1.0 \
                else product.fats * self.portion
            saturated_fats = -1.0 if product.saturated_fats == -1.0 \
                else product.saturated_fats * self.portion
            monosaturated_fats = -1.0 if product.monosaturated_fats == -1.0 \
                else product.monosaturated_fats * self.portion
            polysaturated_fats = -1.0 if product.polysaturated_fats == -1.0 \
                else product.polysaturated_fats * self.portion
            cholesterol = -1.0 if product.cholesterol == -1.0 \
                else product.cholesterol * self.portion
            cellulose = -1.0 if product.cellulose == -1.0 \
                else product.cellulose * self.portion
            sodium = -1.0 if product.sodium == -1.0 \
                else product.sodium * self.portion
            pottasium = -1.0 if product.pottasium == -1.0 \
                else product.pottasium * self.portion

        return(
            kilojoules,
            calories,
            proteins,
            carbohydrates,
            sugar,
            fats,
            saturated_fats,
            monosaturated_fats,
            polysaturated_fats,
            cholesterol,
            cellulose,
            sodium,
            pottasium
        )


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

    # class Meta:
    #     db_table = "recipes_productamount_products"
