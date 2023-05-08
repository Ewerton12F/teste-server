from .views import ServiceDetailView
from .views import SevicesListView
from django.urls import path

app_name = "api"

urlpatterns = [
    path("services-list/<int:pk>", ServiceDetailView.as_view(), name="service-detail"),
    path("services-list", SevicesListView.as_view(), name="services-list"),
]
