from rest_framework import viewsets

from body_measurements.models import BodyMeasurement
from api.serializers.body_measurements import BodyMeasurementSerializer
from rest_framework.permissions import IsAuthenticated


class BodyMeasurementViewset(viewsets.ModelViewSet):
    queryset = BodyMeasurement.objects.all()
    serializer_class = BodyMeasurementSerializer
    permission_classes = (IsAuthenticated,)
