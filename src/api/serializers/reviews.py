from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from api.models.reviews import Reviews


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
