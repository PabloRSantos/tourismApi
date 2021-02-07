from rest_framework.viewsets import ModelViewSet
from api.models.comments import Comments
from api.serializers.comments import CommentSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
