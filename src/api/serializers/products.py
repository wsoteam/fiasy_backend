from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from products.documents import ProductDocument

from products.models import Product, MeasurementUnit, Category, Brand


class GetProductSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument

        fields = (
            'id',
            'name',
            'name_en',
            'name_de',
            'name_pt',
            'name_es',
            'category',
            'brand',
            'full_info',
            'full_info_en',
            'full_info_de',
            'full_info_pt',
            'full_info_es',
            'measurement_units',
            'portion',
            'is_liquid',
            'kilojoules',
            'calories',
            'proteins',
            'carbohydrates',
            'sugar',
            'fats',
            'saturated_fats',
            'monounsaturated_fats',
            'polyunsaturated_fats',
            'cholesterol',
            'cellulose',
            'sodium',
            'pottasium',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name']


class MeasurementUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasurementUnit
        fields = [
            'id',
            'name',
            'amount'
        ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'brand',
            'full_info',
            'measurement_units',
            'portion',
            'is_liquid',
            'kilojoules',
            'calories',
            'proteins',
            'carbohydrates',
            'sugar',
            'fats',
            'saturated_fats',
            'monounsaturated_fats',
            'polyunsaturated_fats',
            'cholesterol',
            'cellulose',
            'sodium',
            'pottasium',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measurement_units'] = MeasurementUnitSerializer(
            instance.measurement_units.all(),
            many=True
        ).data
        representation['category'] = CategorySerializer(
            instance.category
        ).data
        representation['brand'] = BrandSerializer(
            instance.brand
        ).data
        return representation


class EnProductSerializer(ProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_en
        representation['full_info'] = instance.full_info_en
        return representation


class DeProductSerializer(ProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_de
        representation['full_info'] = instance.full_info_de
        return representation


class PtProductSerializer(ProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_pt
        representation['full_info'] = instance.full_info_pt
        return representation


class EsProductSerializer(ProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_es
        representation['full_info'] = instance.full_info_es
        return representation
