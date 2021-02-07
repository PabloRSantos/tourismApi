from django.db import models
from django.contrib.auth.models import User

from api.models.tourism_spot import TourismSpot


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    tourism_spot = models.ForeignKey(TourismSpot, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
