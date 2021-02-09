from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from api.models.tourism_spot import TourismSpot
from api.serializers.tourism_spot import TourismSpotSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


class TourismSpotViewSet(ModelViewSet):
    queryset = TourismSpot.objects.filter(approved=True)
    serializer_class = TourismSpotSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'description']
    filter_fields = ['name', 'description']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
