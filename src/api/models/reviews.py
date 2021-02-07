from django.contrib.auth.models import User
from django.db import models

from api.models.tourism_spot import TourismSpot


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    note = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    tourism_spot = models.ForeignKey(TourismSpot, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
