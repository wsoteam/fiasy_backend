from rest_framework import serializers

from products.models import Product, MeasurementUnit, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measurement_units'] = MeasurementUnitSerializer(
            instance.measurement_units.all(),
            many=True
        ).data
        return representation
