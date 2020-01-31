from django.contrib import admin

from meals.models import Meal, ProductAmount


class ProductInlineAdmin(admin.TabularInline):
    model = ProductAmount
    extra = 1
    raw_id_fields = ('product',)


class MealAdmin(admin.ModelAdmin):
    list_display = ['meal']
    inlines = [ProductInlineAdmin]


admin.site.register(Meal, MealAdmin)
