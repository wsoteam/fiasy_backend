from rest_framework import serializers

from django.contrib.auth.models import User

from meals.models import Meal, ProductAmount, Product


class MealProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name']


class MealSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Product.objects.all()
    )

    class Meta:
        model = Meal
        fields = [
            'id',
            'meal',
            'products',
            'user',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = MealProductSerializer(
            instance.products.all(),
            many=True
        ).data
        return representation

    def create(self, validated_data):
        products = validated_data.pop('products')
        meal = Meal.objects.create(**validated_data)
        for product in products:
            meal.products.add(product)
        return meal