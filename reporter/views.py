from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Incidences, Counties

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'reporter/index.html'

def CountriesView(request):
    countries = serialize('geojson', Counties.objects.all())
    return HttpResponse(countries, content_type='json')

def IncidencesView(request):
    incidences = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidences, content_type='json')

