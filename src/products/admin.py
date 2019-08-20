from django.contrib import admin
from django.contrib.auth.models import User, Group

from django.db.models import Q

from django.utils.translation import ugettext_lazy as _

from products.models import Product, Brand, Category, MeasurementUnit


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class MinusWordsFilter(InputFilter):
    parameter_name = 'product'
    title = _('Minus Words (contains)')

    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        for bit in term.split():
            any_name &= (
                ~Q(name__icontains=bit)
            )
        return queryset.filter(any_name)


class BrandFilter(InputFilter):
    parameter_name = 'brand'
    title = _('By Brand')

    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(brand__name__icontains=bit)
            )
        return queryset.filter(any_name)


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
    list_filter = (
        MinusWordsFilter,
        BrandFilter,
        'category')
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

