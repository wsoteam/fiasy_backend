from django.contrib import admin

from products.models import Product, Brand, Category


# def set_brand(self, request, queryset):
#     for product in queryset:
#         product.brand = Brand.objects.get(pk=1)
#         product.save()
# set_brand.short_description = 'Set Brand'


class CategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ('name', 'parent',)
    list_filter = ('parent',)

    class Meta:
        model = Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'portion',)
    list_filter = ('brand', 'category',)
    search_fields = ('name', 'brand',)
#     actions = (set_brand)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category, CategoryAdmin)
