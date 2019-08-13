from django.db import models

from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=80, null=True, unique=True)
    parent = models.ForeignKey(
        'self',
        verbose_name=_("Parent"),
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        if self.parent:
            return self.parent.name + '/' + self.name
        return self.name


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    full_info = models.TextField(_('Full info'), blank=True)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        null=True,
        related_name='products',
        on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name=_("Brand"),
        blank=True,
        null=True,
        related_name='products',
        on_delete=models.CASCADE
    )
    full_info = models.TextField(_('Full info'), blank=True)
    barcode = models.CharField(
        _('Barcode'),
        max_length=20,
        blank=True,
        null=True
    )
    portion = models.FloatField(
        _('Portion'),
        default=100
    )
    is_liquid = models.BooleanField(_('Is liquid'))
    '''default=-1.0 is according to technical assignment'''
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
    monounsaturated_fats = models.FloatField(
        _('Monosaturated fats'),
        default=-1.0
    )
    polyunsaturated_fats = models.FloatField(
        _('Polysaturated fats'),
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

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class MeasurementUnit(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    amount = models.FloatField(_('Amount'), default=0)
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        blank=True,
        null=True,
        related_name="measurement_units",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Measurement unit')
        verbose_name_plural = _('Measurement units')

    def __str__(self):
        return self.name
