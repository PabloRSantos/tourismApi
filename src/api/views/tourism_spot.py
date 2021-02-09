from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from api.models.attractions import Attraction
from api.models.tourism_spot import TourismSpot
from api.serializers.attractions import AttractionSerializer
from api.serializers.tourism_spot import TourismSpotSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, response
from rest_framework.decorators import action


class TourismSpotViewSet(ModelViewSet):
    queryset = TourismSpot.objects.filter(approved=True)
    serializer_class = TourismSpotSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'description']
    filter_fields = ['name', 'description']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    @action(methods=['post'], detail=True)
    def attractions(self, request, pk):
        instance = TourismSpot.objects.get(id=pk)

        attractions_id = request.data['attractions']

        instance.attractions.set(attractions_id)

        instance.save()

        serialized_instance = self.get_serializer(instance)

        return response.Response(serialized_instance.data)
