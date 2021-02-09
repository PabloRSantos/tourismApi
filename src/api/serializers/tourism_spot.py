from rest_framework.serializers import ModelSerializer
from api.models.tourism_spot import TourismSpot


class TourismSpotSerializer(ModelSerializer):
    class Meta:
        model = TourismSpot
        fields = '__all__'
