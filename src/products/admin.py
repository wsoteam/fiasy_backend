from django.contrib import admin
from django.contrib.auth.models import User, Group

from django.utils.translation import ugettext_lazy as _

from products.models import Product, Brand, Category, MeasurementUnit


class MeasurementUnitInline(admin.TabularInline):
    model = MeasurementUnit


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
    inlines = [
        MeasurementUnitInline
    ]


for category in Category.objects.all():
    def change_category(modeladmin, request, queryset, category=category):
        queryset.update(category=category)
    admin.site.add_action(
        change_category,
        name=_('Add to ') + str(category.name)
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category, CategoryAdmin)

# admin.site.unregister(User)
# admin.site.unregister(Group)
