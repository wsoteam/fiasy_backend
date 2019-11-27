from rest_framework import viewsets
from rest_framework import filters

from products.models import Product
from api.serializers.products import (
    ProductSerializer,
    EnProductSerializer,
    DeProductSerializer,
    EsProductSerializer,
    PtProductSerializer,
    GetProductSerializer,
    EnGetProductSerializer,
    DeGetProductSerializer,
    EsGetProductSerializer,
    PtGetProductSerializer
)

from rest_framework.permissions import IsAuthenticated

from elasticsearch_dsl import MultiSearch, Search

from django_elasticsearch_dsl_drf.constants import (
    SUGGESTER_COMPLETION,
    SUGGESTER_PHRASE,
    SUGGESTER_TERM,
    LOOKUP_FILTER_TERM,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    FunctionalSuggesterFilterBackend,
    SuggesterFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from products.documents import ProductDocument


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
            starts_with_qs = queryset.filter(
                name__istartswith=search_terms).exclude(
                    id__in=obj_to_exclude).order_by('brand')
            queryset = list(equal_qs) + list(starts_with_qs)
        return queryset


class GetProductViewset(DocumentViewSet):
    """
    ES Document ReadOnly ViewSet
    """

    document = ProductDocument
    serializer_class = GetProductSerializer

    # lookup_field = 'name'

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
        FunctionalSuggesterFilterBackend,
        SuggesterFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
    ]

    # Suggester fields
    suggester_fields = {
        'name_suggest': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
                SUGGESTER_PHRASE,
                SUGGESTER_TERM,
            ],
            'options': {
                'size': 5,  # Override default number of suggestions
            },
        },
        'brand_suggest': {
            'field': 'brand.name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
                SUGGESTER_PHRASE,
                SUGGESTER_TERM,
            ],
            'options': {
                'size': 5,  # Override default number of suggestions
            },
        }
    }

    search_fields = (
        'name',
        # 'name_en',
        # 'name_de',
        # 'name_pt',
        # 'name_es',
        # 'brand.name',
        "get_search_field"
    )

    filter_fields = {
        'name': 'name',
        'brand': 'brand.name',
        'category': 'category.name',
    }

    ordering_fields = {
        'name': 'name',
        'brand': 'brand.name',
    }

    ordering = ('_score', 'name')


class EnGetProductViewset(GetProductViewset):
    serializer_class = EnGetProductSerializer
    search_fields = (
        'name_en',
        # 'get_search_field'
    )

    suggester_fields = {
        'name_suggest': {
            'field': 'name_en.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
                SUGGESTER_PHRASE,
                SUGGESTER_TERM,
            ],
            'options': {
                'size': 5,  # Override default number of suggestions
            },
        },
    }


class DeGetProductViewset(GetProductViewset):
    serializer_class = DeGetProductSerializer
    search_fields = (
        'name_de',
        # 'get_search_field'
    )

    suggester_fields = {
        'name_suggest': {
            'field': 'name_de.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
                SUGGESTER_PHRASE,
                SUGGESTER_TERM,
            ],
            'options': {
                'size': 5,  # Override default number of suggestions
            },
        },
    }


class PtGetProductViewset(GetProductViewset):
    serializer_class = PtGetProductSerializer
    search_fields = (
        'name_pt',
        # 'get_search_field'
    )

    suggester_fields = {
        'name_suggest': {
            'field': 'name_pt.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
                SUGGESTER_PHRASE,
                SUGGESTER_TERM,
            ],
            'options': {
                'size': 5,  # Override default number of suggestions
            },
        },
    }


class EsGetProductViewset(GetProductViewset):
    serializer_class = EsGetProductSerializer
    search_fields = (
        'name_es',
        # 'get_search_field'
    )

    suggester_fields = {
        'name_suggest': {
            'field': 'name_es.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
                SUGGESTER_PHRASE,
                SUGGESTER_TERM,
            ],
            'options': {
                'size': 5,  # Override default number of suggestions
            },
        },
    }


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (CustomSearchFilter,)
    search_fields = ['name', 'brand__name']
    # permission_classes = (IsAuthenticated,)


class EnProductViewset(ProductViewset):
    serializer_class = EnProductSerializer


class DeProductViewset(ProductViewset):
    serializer_class = DeProductSerializer


class EsProductViewset(ProductViewset):
    serializer_class = PtProductSerializer


class PtProductViewset(ProductViewset):
    serializer_class = EsProductSerializer
