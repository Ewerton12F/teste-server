from .models import Services
from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ["id", "title", "smalldesc", "largedesc", "icon"]
