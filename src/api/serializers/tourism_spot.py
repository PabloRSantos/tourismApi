# from django.db import transaction
from api.models.tourism_spot import TourismSpot
from api.serializers.locations import LocationSerializer
from api.serializers.attractions import AttractionSerializer
from api.models.location import Location
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TourismSpotSerializer(WritableNestedModelSerializer):
    location = LocationSerializer(required=False)
    attractions = AttractionSerializer(
        many=True, required=False)

    class Meta:
        model = TourismSpot
        fields = '__all__'
        # read_only_fields = ['location', 'attractions']
