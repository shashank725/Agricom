from django.contrib import admin
from .models import *

from leaflet.admin import LeafletGeoAdmin

# Register your models here.

# class IncidencesAdmin(admin.ModelAdmin):
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

class CountriesAdmin(LeafletGeoAdmin):
    list_display = ('countries', 'codes', 'city_code', 'dis', 'geom')

    
admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Countries, CountriesAdmin)