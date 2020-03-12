from rest_framework import serializers

from django.contrib.auth.models import User

from meals.models import Meal, ProductAmount, Product
from .products import SimpleProductSerializer


class MealProductSerializer(serializers.ModelSerializer):
    meal_product_amount = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ProductAmount.objects.all()
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'meal_product_amount']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['meal_product_amount'] = MealProducAmountListSerializer(
            instance.meal_product_amount.all(),
            many=True
        ).data
        return representation


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = [
            'id',
            'meal',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(instance.products)
        representation['products'] = MealProductSerializer(
            instance.products.all(),
            many=True
        ).data
        return representation


class MealProducAmountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAmount
        fields = ['id', 'amount', 'product', 'meal']


class MealProducAmountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAmount
        fields = ['id', 'product', 'amount']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = SimpleProductSerializer(
            instance.product
        ).data
        return representation


# class MealSerializer(serializers.ModelSerializer):

#     products = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Product.objects.all()
#     )

#     class Meta:
#         model = Meal
#         fields = [
#             'id',
#             'meal',
#             'products',
#             'user',
#         ]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['products'] = MealProductSerializer(
#             instance.products.all(),
#             many=True
#         ).data
#         return representation

#     def create(self, validated_data):
#         products = validated_data.pop('products')
#         meal = Meal.objects.create(**validated_data)
#         for product in products:
#             meal.products.add(product)
#         return meal


# class MealProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'meal_product_amount']

#     # def to_representation(self, instance):
#     #     representation = super().to_representation(instance)
#     #     representation['meal_product_amount'] = MealProducAmounttSerializer(
#     #         instance.meal_product_amount.all(),
#     #         many=True
#     #     ).data
#     #     return representation


# class MealProducAmountSerializer(serializers.ModelSerializer):

#     product = MealProductSerializer

#     class Meta:
#         model = ProductAmount
#         fields = ['amount', 'product', 'meal']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['product'] = MealProductSerializer(
#             # instance.products.all(),
#             many=True
#         ).data
#         return representation

        