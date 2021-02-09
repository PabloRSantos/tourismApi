from django.db import models

from api.models.attractions import Attraction
from api.models.location import Location
# from api.models.comments import Comments


class TourismSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tourism_spot', blank=True, null=True)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # comments = models.ManyToManyField(Comments)
    # reviews = models.ManyToManyField(Reviews)

    def __str__(self):
        return self.name
