from django.contrib import admin

from recipes.models import Recipe, ProductAmount

from products.admin import InputFilter

from products.models import Product

from django.db.models import Q

from django.utils.translation import ugettext_lazy as _


class ProductFilter(InputFilter):
    parameter_name = 'product'
    title = _('By Products')

    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(products__name__icontains=bit)
            )
        return queryset.filter(any_name)


class ProductInlineAdmin(admin.TabularInline):
    model = ProductAmount
    extra = 1
    raw_id_fields = ('product',)


class RecipeAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_display = ['name']
    list_filter = (ProductFilter,)
    search_fields = ('name', 'full_info', 'products__name',)
    inlines = [ProductInlineAdmin]


admin.site.register(Recipe, RecipeAdmin)
