from rest_framework import serializers

from articles.models import Article, ArticleCategory, Author, ArticleSeries


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSeries
        fields = ['id', 'name', 'users']

    # def update(self, instance, validated_data):
    #     if validated_data['users']:
    #         users = validated_data.pop('users')
    #         article_series = instance.update(**validated_data)
    #     for user in users:
    #         article_series.users.add(user)
    #     return article_series


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
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


