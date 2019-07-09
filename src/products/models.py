from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    full_info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    full_info = models.TextField(blank=True)
    barcode = models.CharField(max_length=20, blank=True, null=True)
    portion = models.FloatField(default=100)
    is_liquid = models.BooleanField()
    '''default=-1.0 is according to technical assignment'''
    kilojoules = models.FloatField(default=-1.0)
    calories = models.FloatField(default=-1.0)
    proteins = models.FloatField(default=-1.0)
    carbohydrates = models.FloatField(default=-1.0)
    sugar = models.FloatField(default=-1.0)
    fats = models.FloatField(default=-1.0)
    saturated_fats = models.FloatField(default=-1.0)
    monosaturated_fats = models.FloatField(default=-1.0)
    polysaturated_fats = models.FloatField(default=-1.0)
    cholesterol = models.FloatField(default=-1.0)
    cellulose = models.FloatField(default=-1.0)
    sodium = models.FloatField(default=-1.0)
    pottasium = models.FloatField(default=-1.0)

    def __str__(self):
        return self.name
