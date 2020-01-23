from rest_framework import viewsets
from rest_framework import filters

from diet_plans.models import DietPlan
from api.serializers.diet_plans import DietPlanSerializer
from rest_framework.permissions import IsAuthenticated


class DietPlanViewset(viewsets.ReadOnlyModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = (IsAuthenticated,)
