from rest_framework.viewsets import ModelViewSet
from api.models.tourism_spot import TourismSpot
from api.serializers.tourism_spot import TourismSpotSerializer


class TourismSpotViewSet(ModelViewSet):
    queryset = TourismSpot.objects.all()
    serializer_class = TourismSpotSerializer
