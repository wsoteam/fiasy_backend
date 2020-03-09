from rest_framework import serializers

from body_measurements.models import BodyMeasurement


class BodyMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyMeasurement
        fields = [
            'id',
            'weight',
            'chest',
            'waist',
            'hips',
            'date'
        ]


