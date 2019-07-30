from django.contrib import admin

from recipes.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_ingredients_elements']
    list_filter = ('products__name',)
    search_fields = ('name', 'full_info', 'products__name',)


admin.site.register(Recipe, RecipeAdmin)
