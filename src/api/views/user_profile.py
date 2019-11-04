from rest_framework import viewsets
from rest_framework import filters

from users.models import User, UserProfile

from rest_framework import generics, mixins, views

from api.serializers.user_profile import (
    UserSerializer,
    UserProfileSerializer,
)

from rest_framework.permissions import IsAuthenticated


class UserProfileViewset(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewset(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = (CustomSearchFilter,)
    # search_fields = ['name']
    # permission_classes = (IsAuthenticated,)
