from rest_framework import serializers

from articles.models import Article, ArticleCategory, Author, ArticleSeries


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSeries
        fields = ['id', 'name']


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    # category = ArticleCategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = ArticleCategorySerializer(
            instance.category
        ).data
        representation['author'] = AuthorSerializer(
            instance.author
        ).data
        representation['series'] = ArticleSeriesSerializer(
            instance.series
        ).data
        return representation