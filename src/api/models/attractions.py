from django.db import models

# from api.models.tourism_spot import TourismSpot


class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    schedule = models.TextField()
    minAge = models.PositiveIntegerField()
    image = models.ImageField(upload_to='attractions', blank=True, null=True)
    # tourism_spot = models.ManyToManyField(TourismSpot)

    def __str__(self):
        return self.name
