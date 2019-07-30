from rest_framework import viewsets
from rest_framework import filters

from recipes.models import Recipe
from api.serializers.recipes import RecipeSerializer


class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'full_info',)
