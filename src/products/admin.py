from django.contrib import admin

from django.db.models import Q

from django.utils.translation import ugettext_lazy as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from admin_numeric_filter.admin import NumericFilterModelAdmin,\
    RangeNumericFilter

from products.models import Product, Brand, Category, MeasurementUnit


class CaregoryFilter(admin.SimpleListFilter):
    parameter_name = 'category'
    title = _('By Category Adding')

    def lookups(self, request, model_admin):
        return (
            ('with_category', _('With category')),
            ('without_category', _('Without category'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'without_category':
            return queryset.filter(category__isnull=True)
        elif self.value() == 'with_category':
            return queryset.filter(category__isnull=False)


class BrandAddingFilter(admin.SimpleListFilter):
    parameter_name = 'brand add'
    title = _('By Brand Adding')

    def lookups(self, request, model_admin):
        return (
            ('with_brand', _('With brand')),
            ('without_brand', _('Without brand'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'without_brand':
            return queryset.filter(brand__isnull=True)
        elif self.value() == 'with_brand':
            return queryset.filter(brand__isnull=False)


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
    title = _('Negative Keywords')

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


class CaregoryProductsFilter(InputFilter):
    title = _('By Category Parent')
    parameter_name = 'category parent'

    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        any_name &= (
           Q(category__parent__name=term)
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


class CustomRangeNumericFilter(RangeNumericFilter):
    template = 'admin/admin_numeric_filter/filter_numeric_range.html'


class MeasurementUnitInline(admin.TabularInline):
    model = MeasurementUnit


class CategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ['name', 'parent']
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name',)

    class Meta:
        model = Category


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        exclude = ('id',)
        import_id_fields = ['name']
        fields = (
            'id',
            'name',
            'category',
            'brand',
            'full_info',
            'barcode',
            'portion',
            'is_liquid',
            'kilojoules',
            'calories',
            'proteins',
            'carbohydrates',
            'sugar',
            'fats',
            'saturated_fats',
            'monounsaturated_fats',
            'polyunsaturated_fats',
            'cholesterol',
            'cellulose',
            'sodium',
            'pottasium'
        )


def add_actions():
    for category in Category.objects.all():
        def change_category(modeladmin, request, queryset, category=category):
            queryset.update(category=category)
        admin.site.add_action(
            change_category,
            name=_(str(category.name))
        )


class ProductAdmin(ImportExportModelAdmin, NumericFilterModelAdmin, admin.ModelAdmin):
    list_display = [
        'name',
        'brand',
        'category',
        'portion',
        'calories',
        'proteins',
        'fats',
        'carbohydrates'
    ]
    list_filter = (
        MinusWordsFilter,
        BrandFilter,
        BrandAddingFilter,
        CaregoryProductsFilter,
        ('calories', CustomRangeNumericFilter),
        ('proteins', CustomRangeNumericFilter),
        ('fats', CustomRangeNumericFilter),
        ('carbohydrates', CustomRangeNumericFilter),
        CaregoryFilter,
        'is_liquid',
        'category',
    )
    search_fields = ('name', 'category__name')
    inlines = [
        MeasurementUnitInline
    ]
    list_per_page = 200
    resource_class = ProductResource



# class AddActionsAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/add_actions.html'

for category in Category.objects.all():
    def change_category(modeladmin, request, queryset, category=category):
        queryset.update(category=category)
    admin.site.add_action(
        change_category,
        name=_(str(category.name))
    )




admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(AddActionsAdmin)
