from rest_framework import viewsets
from rest_framework import filters

from products.models import Product
from api.serializers.products import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'brand__name',)
