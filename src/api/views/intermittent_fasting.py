from rest_framework import viewsets

from api.serializers.intermittent_fasting import FastingSerializer
from intermittent_fasting.models import Fasting

from rest_framework.permissions import IsAuthenticated


class FastingViewset(viewsets.ModelViewSet):
    queryset = Fasting.objects.all()
    serializer_class = FastingSerializer
    permission_classes = (IsAuthenticated,)
