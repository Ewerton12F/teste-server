from .views import SevicesListView
from django.urls import path

urlpatterns = [
    path("services-list", SevicesListView.as_view(), name="services-list"),
]
