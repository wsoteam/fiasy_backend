from rest_framework import serializers
from rest_framework import filters

from recipes.models import Recipe, ProductAmount
from products.models import Product

from api.serializers.products import ProductSerializer


class ProductAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAmount
        fields = ('amount',)


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'amount'
        )

    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['amount'] = ProductAmountSerializer(
                instance.amount.all(),
                many=True
            ).data
            return representation


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = RecipeProductSerializer(
            instance.products.all(),
            many=True
        ).data
        return representation
