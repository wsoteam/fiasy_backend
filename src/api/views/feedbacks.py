from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from feedbacks.models import FeedbackType

from api.serializers.feedbacks import (
    FeedbackSerializer,
    FeedbackTypeSerializer
)


class FeedbackTypeView(views.APIView):
    serializer_class = FeedbackTypeSerializer()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = FeedbackType.objects.all()
        serializer = FeedbackTypeSerializer(queryset, many=True)
        return Response(serializer.data)


class FeedbackView(views.APIView):
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Feedback is added'})
        else:
            return Response({'message': 'Error! All fields are required'})
