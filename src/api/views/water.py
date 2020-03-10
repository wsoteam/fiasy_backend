from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from api.serializers.water import WaterSerializer

from water.models import WaterDrinking


class WaterViewset(viewsets.ModelViewSet):

    queryset = WaterDrinking.objects.all()
    serializer_class = WaterSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            amount = request.data['amount']
            water = WaterDrinking(user=user, amount=amount)
            water.save()
            return Response(
                WaterSerializer(water).data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        queryset = WaterDrinking.objects.filter(user=user)
        return queryset
