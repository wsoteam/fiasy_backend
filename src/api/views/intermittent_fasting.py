from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers.intermittent_fasting import FastingSerializer
from intermittent_fasting.models import Fasting

from rest_framework.permissions import IsAuthenticated


class FastingViewset(viewsets.ModelViewSet):
    queryset = Fasting.objects.all()
    serializer_class = FastingSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            start = request.data['start']
            end = request.data['end']
            intermittent_fasting = Fasting(
                users=user,
                start=start,
                end=end
            )
            intermittent_fasting.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        queryset = Fasting.objects.filter(users=user)
        return queryset
