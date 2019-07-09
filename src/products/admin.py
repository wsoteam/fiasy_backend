from django.contrib import admin

from products.models import Product, Brand


# def set_brand(self, request, queryset):
#     for product in queryset:
#         product.brand = Brand.objects.get(pk=1)
#         product.save()
# set_brand.short_description = 'Set Brand'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'portion')
    list_filter = ('brand',)
    search_fields = ('name', 'brand')
#     actions = (set_brand)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
