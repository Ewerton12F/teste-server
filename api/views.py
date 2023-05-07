from .models import Services
from .serializers import ServicesSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


class SevicesListView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServiceDetailView(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
