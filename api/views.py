from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Services
from .serializers import ServicesSerializer


class SevicesListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
