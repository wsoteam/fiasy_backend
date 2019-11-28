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


class EnGetProductSerializer(GetProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_en
        representation['full_info'] = instance.full_info_en
        for i in representation['measurement_units']:
            i['name'] = i['name_en']
        return representation


class DeGetProductSerializer(GetProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_de
        representation['full_info'] = instance.full_info_de
        for i in representation['measurement_units']:
            i['name'] = i['name_de']
        return representation


class PtGetProductSerializer(GetProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_pt
        representation['full_info'] = instance.full_info_pt
        for i in representation['measurement_units']:
            i['name'] = i['name_pt']
        return representation


class EsGetProductSerializer(GetProductSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name_es
        representation['full_info'] = instance.full_info_es
        for i in representation['measurement_units']:
            i['name'] = i['name_es']
        return representation


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
