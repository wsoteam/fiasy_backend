from rest_framework import serializers

from activities.models import Activity, CustomUserActivity, ActivityTime


class ActivityTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTime
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'icon',
            'name',
            'сonsumption',
            'activity_time'
        ]

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['activity_time'] = ActivityTimeSerializer(
    #         instance.activity_time.all(),
    #         many=True
    #     ).data
    

class CustomUserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserActivity
        fields = '__all__'
