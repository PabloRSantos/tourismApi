from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from api.models.comments import Comments


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
