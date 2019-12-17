from rest_framework import views
from rest_framework.response import Response

from api.serializers.feedbacks import FeedbackSerializer



class FeedbackView(views.APIView):
    serializer_class = FeedbackSerializer

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save() 
            return Response({'message': 'Feedback is added'})
        else:
            return Response({'message': 'Error! All fields are required'})