from django.urls import path

from .views import SevicesListView

urlpatterns = [
    path("services-list", SevicesListView.as_view(), name="services-list"),
]
