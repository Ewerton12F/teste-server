from .models import Services
from .serializers import ServicesSerializer
from rest_framework.generics import ListAPIView


class SevicesListView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
