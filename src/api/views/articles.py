from rest_framework import viewsets
from rest_framework import filters

from articles.models import Article
from api.serializers.articles import ArticleSerializer

from rest_framework.permissions import IsAuthenticated


class ArticleViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body',)
    permission_classes = (IsAuthenticated,)
