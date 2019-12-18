from rest_framework import serializers

from feedbacks.models import Feedback, FeedbackType


class FeedbackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackType
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)