from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from api.serializers.meals import MealSerializer

from meals.models import Meal, ProductAmount


class MealsViewset(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticated,)
    # queryset = ProductAmount.objects.all()
    # serializer_class = MealProducAmountSerializer
    # permission_classes = (IsAuthenticated,)

