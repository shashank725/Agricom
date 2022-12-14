from django.db import models

from django.contrib.gis.db import models
# from django.db.models import Manager as GeoManager

# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __str__(self):
        return self.name
    # class Meta:
    #     verbose_name_plural = "Incidences"

class Countries(models.Model):
    countries = models.CharField(max_length=100)
    codes = models.IntegerField()
    city_code = models.CharField(max_length=100)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.countries