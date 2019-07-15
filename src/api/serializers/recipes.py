from rest_framework import serializers
from rest_framework import filters

from recipes.models import Recipe

from api.serializers.products import ProductSerializer


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation
