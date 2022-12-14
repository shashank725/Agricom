from django.contrib import admin
from .models import *

from leaflet.admin import LeafletGeoAdmin

# Register your models here.

# class IncidencesAdmin(admin.ModelAdmin):
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    
admin.site.register(Incidences, IncidencesAdmin)