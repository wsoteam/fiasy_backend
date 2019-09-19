from django.core.management.base import BaseCommand

from django.db import models

from products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        fields = [
            'name',
            'brand',
            'calories',
            'proteins',
            'fats',
            'carbohydrates',
        ]
        duplicates = Product.objects.values(*fields)
        duplicates = duplicates.order_by()
        duplicates = duplicates.annotate(
            max_id=models.Max("id"), count_id=models.Count("id")
        )
        duplicates = duplicates.filter(count_id__gt=1)

        for duplicate in duplicates:
            to_delete = Product.objects.filter(
                **{x: duplicate[x] for x in fields}
            )
            to_delete = to_delete.exclude(id=duplicate["max_id"])
            to_delete.delete()
