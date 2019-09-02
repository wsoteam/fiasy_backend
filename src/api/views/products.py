from rest_framework import viewsets
from rest_framework import filters

from products.models import Product
from api.serializers.products import ProductSerializer


class CustomSearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        if request.query_params.get('name_only'):
            return ['name']
        return super(CustomSearchFilter, self).get_search_fields(view, request)

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')
        return params

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        if search_terms:
            print(search_terms)
            equal_qs = queryset.filter(
                name__iexact=search_terms).order_by('brand')
            obj_to_exclude = [o.id for o in equal_qs]
            contains_qs = queryset.filter(
                name__icontains=search_terms).exclude(
                    id__in=obj_to_exclude).order_by('category')
            queryset = list(equal_qs) + list(contains_qs)
        return queryset


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (CustomSearchFilter,)
    search_fields = ['name']
