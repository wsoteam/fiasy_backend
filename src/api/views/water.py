from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from api.serializers.water import WaterSerializer

from water.models import WaterDrinking


class WaterViewset(viewsets.ModelViewSet):

    queryset = WaterDrinking.objects.all()
    serializer_class = WaterSerializer
    permission_classes = (IsAuthenticated,)
