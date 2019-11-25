from sendsay_api.sendsay.api import SendsayAPI

from rest_framework import views

from rest_framework.response import Response

from api.serializers.sendsay import (
    SendsaySetMemberSerializer,
    _ios_group_id,
    _android_group_id
)


class SendsaySetMemberView(views.APIView):
    serializer_class = SendsaySetMemberSerializer

    def post(self, request):
        serializer = SendsaySetMemberSerializer(data=request.data)
        api = SendsayAPI(login='sav@wsoteam.com', password='13Kalibr13280190')
        if serializer.is_valid():
            email = serializer.data.get('email')
            group = serializer.data.get('os').lower()
            if group == 'android':
                group_id = _android_group_id
            elif group == 'ios':
                group_id = _ios_group_id
            api.request(
                'member.set',
                {
                    'email': email,
                    'addr_type': 'email',
                    'if_exists': 'overwrite',
                    'newbie.confirm': 0,
                    'return_fresh_obj': 1,
                    'obj': {
                        '-group': {
                            group_id: 1,
                        }
                    }
                }
            )
            return Response({'message': email + ' is added'})
        else:
            return Response({'message': 'Email is not valid'})
