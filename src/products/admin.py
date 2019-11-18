from django.contrib import admin

from django.db.models import Q

from django.utils.translation import ugettext_lazy as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

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


class MeasurementUnitsAddingFilter(admin.SimpleListFilter):
    parameter_name = 'measurement units add'
    title = _('By Measurement Units Adding')

    def lookups(self, request, model_admin):
        return (
            ('with_measurement_units', _('With Measurement Units')),
            ('without_measurement_units', _('Without Measurement Units'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'without_measurement_units':
            return queryset.filter(measurement_units__isnull=True)
        elif self.value() == 'with_measurement_units':
            return queryset.filter(measurement_units__isnull=False)


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
    classes = ['collapse']
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'amount',
                    'name_en',
                    'name_de',
                    'name_pt',
                    'name_es',
                )
            }
        ),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ['name', 'parent']
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name',)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                )
            },
        ),
        (
            _('Name Localization'),
            {
                'fields': (
                    'name_en',
                    'name_de',
                    'name_pt',
                    'name_es',
                ),
                'classes': ('collapse', 'closed'),
            }
        ),
        (
            None,
            {
                'fields': (
                    'parent',
                )
            },
        ),
    )

    class Meta:
        model = Category


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        import_id_fields = ['id']
        fields = (
            'id',
            'name',
            'name_en',
            'name_de',
            'name_pt',
            'name_es',
            'category',
            'brand',
            'full_info',
            'full_info_en',
            'full_info_de',
            'full_info_pt',
            'full_info_es',
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


class ProductAdmin(
    ImportExportModelAdmin,
    NumericFilterModelAdmin,
    admin.ModelAdmin
):
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
        MeasurementUnitsAddingFilter,
        CaregoryProductsFilter,
        ('calories', CustomRangeNumericFilter),
        ('proteins', CustomRangeNumericFilter),
        ('fats', CustomRangeNumericFilter),
        ('carbohydrates', CustomRangeNumericFilter),
        CaregoryFilter,
        'is_liquid',
        'category',
    )
    search_fields = ('name_ru', 'category__name')
    inlines = [
        MeasurementUnitInline
    ]
    list_per_page = 200
    resource_class = ProductResource

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                )
            },
        ),
        (
            _('Name Localization'),
            {
                'fields': (
                    'name_ru',
                    'name_en',
                    'name_de',
                    'name_pt',
                    'name_es',
                ),
                'classes': ('collapse', 'closed'),
            }
        ),
        (
            None,
            {
                'fields': (
                    'category',
                    'brand',
                    'full_info',
                )
            }
        ),
        (
            _('Full Info Localization'),
            {
                'fields': (
                    'full_info_en',
                    'full_info_de',
                    'full_info_pt',
                    'full_info_es',
                ),
                'classes': ('collapse', 'closed'),
            }
        ),
        (
            None,
            {
                'fields': (
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
            }
        ),
    )


def update_actions(
    modeladmin,
    request,
    queryset,
    categories=Category.objects.all().order_by('name')
):
    for category in categories:
        def change_category(modeladmin, request, queryset, category=category):
            queryset.update(category=category)
        admin.site.add_action(
            change_category,
            name=_(str(category.name))
        )


def set_brand_null(modeladmin, request, queryset):
    brand = Brand.objects.get(name='null')
    queryset.update(brand=brand)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category, CategoryAdmin)
admin.site.add_action(update_actions)
admin.site.add_action(set_brand_null, name=_('Set brand null'))
