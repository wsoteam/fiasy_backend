from django.contrib import admin

from recipes.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_ingredients_elements']


admin.site.register(Recipe, RecipeAdmin)
