from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response

from users.models import User, UserProfile
from products.models import Product
from rest_framework import status

from rest_framework import generics, mixins, views

from api.serializers.user_profile import (
    UserSerializer,
    UserProfileSerializer,
    DeleteFavProductSerializer,
    AddFavProductSerializer
)


from rest_framework.permissions import IsAuthenticated


# class UserProfileViewset(mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         viewsets.GenericViewSet):
class UserProfileViewset(viewsets.ModelViewSet):

    # queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user)
        return queryset


# class UserViewset(mixins.CreateModelMixin,
#                 mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 viewsets.GenericViewSet):
class UserViewset(viewsets.ModelViewSet):

    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id)
        return queryset


class DeleteFavProductView(views.APIView):
    serializer_class = DeleteFavProductSerializer

    def post(self, request):
        serializer = DeleteFavProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.data.get('product')
            product = Product.objects.get(id=product_id)
            user = self.request.user
            if product in user.favorite_products.all():
                user.favorite_products.remove(product)
                return Response(
                    {f'{product.name} was deleted from {user.username} favorites'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {f'{product.name} is not in {user.username} favorites'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AddFavProductView(views.APIView):
    serializer_class = AddFavProductSerializer

    def post(self, request):
        serializer = AddFavProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.data.get('product')
            product = Product.objects.get(id=product_id)
            user = self.request.user
            if product in user.favorite_products.all():
                return Response(
                    {f'{product.name} already in {user.username} favorites'},
                    status=status.HTTP_409_CONFLICT
                )
            else:
                user.favorite_products.add(product)
                return Response(
                    {f'{product.name} was added to {user.username} favorites'},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
