from django.db import models


class Location(models.Model):
    street = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    nation = models.CharField(max_length=70)
    lat = models.IntegerField(null=True, blank=True)
    lon = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.street
