from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category, Brand, MeasurementUnit


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'full_info',
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


# @register(Brand)
# class BrandTranslationOptions(TranslationOptions):
#     fields = (
#         'name',
#         'full_info',
#     )


@register(MeasurementUnit)
class MeasurementUnitranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
