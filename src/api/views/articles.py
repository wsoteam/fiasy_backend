from rest_framework import viewsets
from rest_framework import filters

from articles.models import Article, ArticleSeries
from api.serializers.articles import ArticleSerializer, ArticleSeriesSerializer

from rest_framework.permissions import IsAuthenticated


class ArticleViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body',)
    permission_classes = (IsAuthenticated,)


class ArticleSeriesViewset(viewsets.ModelViewSet):
    queryset = ArticleSeries.objects.all()
    serializer_class = ArticleSeriesSerializer
    permission_classes = (IsAuthenticated,)
