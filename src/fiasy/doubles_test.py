from products.models import Product

p = Product.objects.get(name='Зеленая Фасоль (Консервированная, с Низким Содержанием Натрия)')
for i in p:
    print(i)