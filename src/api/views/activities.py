from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            name = request.data['name']
            сonsumption = request.data['сonsumption']
            custom_activity = CustomUserActivity(
                user=user,
                name=name,
                сonsumption=сonsumption
            )
            custom_activity.save()
            return Response(
                CustomUserActivitySerializer(custom_activity).data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivityTimeViewset(viewsets.ModelViewSet):
    serializer_class = ActivityTimeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = ActivityTime.objects.filter(user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            minutes = request.data['minutes']
            activity = Activity.objects.get(id=request.data['activity'])
            activity_time = ActivityTime(
                user=user,
                minutes=minutes,
                activity=activity
            )
            activity_time.save()
            return Response(
                ActivityTimeSerializer(activity_time).data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomActivityTimeViewset(viewsets.ModelViewSet):
    serializer_class = CustomActivityTimeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        activities = user.custom_activities.all()
        queryset = CustomActivityTime.objects.filter(activity__in=activities)
        return queryset
           