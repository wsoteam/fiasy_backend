from rest_framework import serializers

from diet_plans.models import DietPlan, DietPlanCategory


class DietPlanCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlanCategory
        fields = ['id', 'name']


class DietPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietPlan
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = DietPlanCategorySerializer(
            instance.category
        ).data
        return representation
