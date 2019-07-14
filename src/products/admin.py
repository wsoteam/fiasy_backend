from django.contrib import admin
from django.db.models import Q
from django.contrib.admin.utils import lookup_needs_distinct

import operator

from products.models import Product, Brand, Category


class CategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ['name', 'parent']
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name',)

    class Meta:
        model = Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'portion']
    list_filter = ('brand', 'category',)
    search_fields = ('name', 'brand__name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category, CategoryAdmin)
