from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from activities.models import (
    Activity,
    CustomUserActivity,
    ActivityTime,
    CustomActivityTime
)
from api.serializers.activities import (
    ActivitySerializer,
    CustomUserActivitySerializer,
    ActivityTimeSerializer,
    CustomActivityTimeSerializer
)


class ActivityViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated, )


class CustomUserActivityViewset(viewsets.ModelViewSet):
    serializer_class = CustomUserActivitySerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return user.custom_activities.all()


class ActivityTimeViewset(viewsets.ModelViewSet):
    serializer_class = ActivityTimeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = ActivityTime.objects.filter(user=user)
        return queryset


class CustomActivityTimeViewset(viewsets.ModelViewSet):
    serializer_class = CustomActivityTimeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        activities = user.custom_activities.all()
        queryset = CustomActivityTime.objects.filter(activity__in=activities)
        return queryset
