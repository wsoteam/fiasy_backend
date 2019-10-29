from rest_framework import viewsets
from rest_framework import filters

from users.models import User, UserProfile

from rest_framework import generics, mixins, views
from rest_framework.response import Response

from api.serializers.user_profile import (
    UserSerializer,
    UserProfileSerializer,
    SendsaySetMemberSerializer
)

from rest_framework.permissions import IsAuthenticated

from sendsay.api import SendsayAPI


class SendsaySetMemberView(views.APIView):
    serializer_class = SendsaySetMemberSerializer

    def post(self, request):
        serializer = SendsaySetMemberSerializer(data=request.data)
        api = SendsayAPI(login='sav@wsoteam.com', password='13Kalibr13280190')

        if serializer.is_valid():
            email = serializer.data.get('email')
            response = api.request(
                'member.set',
                {
                    'email': email,
                    'addr_type': 'email',
                    'if_exists': 'overwrite',
                    'newbie.confirm': 0,
                    'return_fresh_obj': 1
                }
            )
            return Response(response)
        else:
            return Response({'message': 'Email is not valid'})


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
