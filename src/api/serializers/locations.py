from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from api.models.location import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
