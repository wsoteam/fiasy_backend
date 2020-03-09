from rest_framework import viewsets, status
from rest_framework.response import Response

from body_measurements.models import BodyMeasurement
from api.serializers.body_measurements import BodyMeasurementSerializer
from rest_framework.permissions import IsAuthenticated


class BodyMeasurementViewset(viewsets.ModelViewSet):
    queryset = BodyMeasurement.objects.all()
    serializer_class = BodyMeasurementSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            chest = request.data['chest']
            waist = request.data['waist']
            weight = request.data['weight']
            hips = request.data['hips']
            body_measurements = BodyMeasurement(
                user=user,
                chest=chest,
                waist=waist,
                weight=weight,
                hips=hips
            )
            body_measurements.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        queryset = BodyMeasurement.objects.filter(user=user)
        return queryset
