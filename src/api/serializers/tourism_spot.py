from rest_framework.serializers import ModelSerializer, Serializer
from api.models.tourism_spot import TourismSpot


class TourismSpotSerializer(ModelSerializer):
    class Meta:
        model = TourismSpot
        fields = ('id', 'name', 'description')
