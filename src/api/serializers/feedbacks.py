from rest_framework import serializers

from feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)