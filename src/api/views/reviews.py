from rest_framework.viewsets import ModelViewSet
from api.models.reviews import Reviews
from api.serializers.reviews import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
