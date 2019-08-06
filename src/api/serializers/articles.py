from rest_framework import serializers

from articles.models import Article, ArticleCategory


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    # category = ArticleCategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
