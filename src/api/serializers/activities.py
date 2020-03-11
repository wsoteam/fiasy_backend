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
        fields = [
            'id',
            'minutes',
            'activity'
        ]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id',
            'icon',
            'name',
            'сonsumption',
        ]



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
            'custom_activity_time'
        ]
