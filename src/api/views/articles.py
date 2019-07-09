from rest_framework import viewsets

from articles.models import Article
from api.serializers.articles import ArticleSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
