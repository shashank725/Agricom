from django.contrib import admin
from .models import *

from leaflet.admin import LeafletGeoAdmin

# Register your models here.

# class IncidencesAdmin(admin.ModelAdmin):
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

class CountriesAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes', 'cty_code', 'dis')

    
admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountriesAdmin)