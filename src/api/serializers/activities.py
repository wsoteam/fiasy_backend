from rest_framework import serializers

from activities.models import (
    Activity,
    CustomUserActivity,
    ActivityTime,
    CustomActivityTime
)


class ActivityTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTime
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id',
            'icon',
            'name',
            'сonsumption',
            # 'activity_time'
        ]

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['activity_time'] = ActivityTimeSerializer(
    #         instance.activity_time.all(),
    #         many=True
    #     ).data


class CustomActivityTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomActivityTime
        fields = [
            'id',
            'activity_time',
            'activity',
            'timestamp'
        ]


class CustomUserActivitySerializer(serializers.ModelSerializer):

    custom_activity_time = CustomActivityTimeSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUserActivity
        fields = [
            'id',
            'name',
            'сonsumption',
            'user',
            'custom_activity_time'
        ]
