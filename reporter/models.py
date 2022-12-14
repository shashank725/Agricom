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

class Counties(models.Model):
    counties = models.CharField(max_length=100)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=100)
    dis = models.IntegerField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.counties