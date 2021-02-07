from rest_framework.viewsets import ModelViewSet
from api.models.location import Location
from api.serializers.locations import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
