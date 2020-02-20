from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response

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
    permission_classes = (IsAuthenticated,)


class UserViewset(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


# class DeleteFavProductView(views.APIView):
#     serializer_class = DeleteFavProductSerializer

#     def post(self, request):
#         serializer = DeleteFavProductSerializer(data=request.data)
#         if serializer.is_valid():
#             favorited_by = serializer.data.get('favorited_by')
#             product = serializer.data.get('product')
#             user = User.objects.get(id=favorited_by)
#             r = user.profile.favorite_products.remove(product)
#             print(favorited_by, product, user)
#             return Response(
#                 {'Product was deleted from ' + user.username + ' favorites'}
#             )
#         else:
#             return Response({'Not Created'})


# class AddFavProductView(views.APIView):
#     serializer_class = AddFavProductSerializer

#     def post(self, request):
#         serializer = AddFavProductSerializer(data=request.data)
#         if serializer.is_valid():
#             favorited_by = serializer.data.get('favorited_by')
#             product = serializer.data.get('product')
#             user = User.objects.get(id=favorited_by)
#             r = user.profile.favorite_products.add(product)
#             print(favorited_by, product, user)
#             return Response(
#                 {'Product was added to ' + user.username + ' favorites'}
#             )
#         else:
#             return Response({'Not Created'})
