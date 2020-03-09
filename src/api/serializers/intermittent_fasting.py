from rest_framework import serializers

from intermittent_fasting.models import Fasting


class FastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fasting
        fields = [
            'id',
            'start',
            'end',
        ]
