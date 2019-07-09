from rest_framework import viewsets

from products.models import Product
from api.serializers.products import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
