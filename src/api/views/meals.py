from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from api.serializers.meals import (
    MealSerializer,
    MealProducAmountSerializer,
    MealProducAmountListSerializer
)

from meals.models import Meal, ProductAmount
from products.models import Product


class MealsViewset(viewsets.ModelViewSet):

    serializer_class = MealSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Meal.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            print(serializer)
            meal = request.data['meal']
            meal_obj = Meal(
                user=user,
                meal=meal
            )
            meal_obj.save()
            return Response(
                MealSerializer(meal_obj).data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MealsProductViewset(viewsets.ModelViewSet):
    serializer_class = MealProducAmountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        meals = user.meals.all()
        queryset = ProductAmount.objects.filter(meal__in=meals)
        return queryset

    
