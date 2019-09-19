import sqlite3

from django.core.management.base import BaseCommand

from products.models import Product, Category, Brand


class Command(BaseCommand):

    def handle(self, *args, **options):
        conn = sqlite3.connect('FoodDB.db')
        cur = conn.cursor()
        qs = cur.execute("SELECT * FROM C_FOOD")
        for i in qs:
            if i[7] == 1:
                is_liquid = True,
            else:
                is_liquid = False,
            if i[1] != '':
                brand, created = Brand.objects.get_or_create(name=i[1])
                product = Product.objects.create(
                    brand=Brand.objects.get(name=i[1]),
                    calories=i[2],
                    carbohydrates=i[3],
                    cellulose=i[4],
                    cholesterol=i[5],
                    fats=i[6],
                    is_liquid=is_liquid[0],
                    kilojoules=i[8],
                    monounsaturated_fats=i[9],
                    name=i[10],
                    polyunsaturated_fats=i[14],
                    portion=i[15],
                    pottasium=i[16],
                    proteins=i[17],
                    saturated_fats=i[18],
                    sodium=i[19],
                    sugar=i[20]
                )
                product.save()
                print(product)
            else:
                product = Product.objects.create(
                    brand=None,
                    calories=i[2],
                    carbohydrates=i[3],
                    cellulose=i[4],
                    cholesterol=i[5],
                    fats=i[6],
                    is_liquid=is_liquid[0],
                    kilojoules=i[8],
                    monounsaturated_fats=i[9],
                    name=i[10],
                    polyunsaturated_fats=i[14],
                    portion=i[15],
                    pottasium=i[16],
                    proteins=i[17],
                    saturated_fats=i[18],
                    sodium=i[19],
                    sugar=i[20]
                )
                product.save()
                print(product)
