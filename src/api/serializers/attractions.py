from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from api.models.attractions import Attraction


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'
