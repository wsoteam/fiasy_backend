from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from activities.models import (
    Activity,
    CustomUserActivity,
    ActivityTime
)
from api.serializers.activities import (
    ActivitySerializer,
    CustomUserActivitySerializer,
    ActivityTimeSerializer
)


class ActivityViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated, )


class CustomUserActivityViewset(viewsets.ModelViewSet):
    queryset = CustomUserActivity.objects.all()
    serializer_class = CustomUserActivitySerializer
    permission_classes = (IsAuthenticated, )


class ActivityTimeViewset(viewsets.ModelViewSet):
    queryset = ActivityTime.objects.all()
    serializer_class = ActivityTimeSerializer
    permission_classes = (IsAuthenticated, )
