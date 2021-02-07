from rest_framework.viewsets import ModelViewSet
from api.models.attractions import Attraction
from api.serializers.attractions import AttractionSerializer


class AttractionsViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
