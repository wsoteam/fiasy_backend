from rest_framework import serializers

from users.models import User, UserProfile
from api.serializers.activities import (
    ActivitySerializer,
    CustomUserActivitySerializer,
    ActivityTimeSerializer,
    CustomActivityTimeSerializer
)


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "uid",
            "image",
            "gender",
            "activity",
            "goals",
            "age",
            "height",
            "weight",
            "birth_date",
            "max_carbo",
            "max_fats",
            "max_calories",
            "max_proteins",
            "water_count",
            "user",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):

    profile = UserProfileSerializer(read_only=True)
    activities = ActivitySerializer(many=True)
    custom_activities = CustomUserActivitySerializer(many=True)
    activity_time = ActivityTimeSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
            "meals",
            "water_drinking",
            "article_series",
            "diet_plans",
            "body_measurements",
            "intermittent_fasting",
            "favorite_products",
            "activities",
            "activity_time",
            "custom_activities",
        ]


# class AddFavProductSerializer(serializers.Serializer):

#     favorited_by = serializers.IntegerField(min_value=1)
#     product = serializers.IntegerField(min_value=1)


# class DeleteFavProductSerializer(AddFavProductSerializer):
#     pass
