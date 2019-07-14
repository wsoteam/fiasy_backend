from django.db import models

from products.models import Product


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    full_info = models.TextField(blank=True)
    image = models.ImageField(upload_to='recipe_image')
    cooking_time = models.IntegerField(blank=True, null=True)
    cooking_process = models.TextField(blank=True)
    portion = models.FloatField(default=100)
    products = models.ManyToManyField(
        Product,
        blank=True
    )
    date = models.DateField(auto_now=True)
    is_moderated = models.BooleanField(default=False)

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
