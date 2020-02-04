from rest_framework import serializers

from water.models import WaterDrinking


class WaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterDrinking
        fields = '__all__'
