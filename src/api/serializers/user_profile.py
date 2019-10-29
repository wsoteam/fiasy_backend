from rest_framework import serializers

from users.models import User, UserProfile


class SendsaySetMemberSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",           
            "last_login",
            "date_joined",
        ]

    # def to_representation(self, instance):
    #         representation = super().to_representation(instance)
    #     representation['measurement_units'] = MeasurementUnitSerializer(
    #         instance.measurement_units.all(),
    #         many=True
    #     ).data
    #     representation['category'] = CategorySerializer(
    #         instance.category
    #     ).data
    #     representation['brand'] = BrandSerializer(
    #         instance.brand
    #     ).data
    #     return representation

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile', None)
    #     user = super(UserSerializer, self).create(validated_data)
    #     self.update_or_create_profile(user, profile_data)
    #     return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile', None)
    #     self.update_or_create_profile(instance, profile_data)
    #     return super(UserSerializer, self).update(instance, validated_data)

    # def update_or_create_profile(self, user, profile_data):
    #     # This always creates a Profile if the User is missing one;
    #     # change the logic here if that not right for your app
    #     Profile.objects.update_or_create(user=user, defaults=profile_data)
