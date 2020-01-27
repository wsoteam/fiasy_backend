from rest_framework import serializers

from users.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

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
            "favorite_products"
        ]


class UserSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
        ]


class AddFavProductSerializer(serializers.Serializer):

    favorited_by = serializers.IntegerField(min_value=1)
    product = serializers.IntegerField(min_value=1)


class DeleteFavProductSerializer(AddFavProductSerializer):
    pass
