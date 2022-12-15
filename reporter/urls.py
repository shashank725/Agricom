from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('incidences/', IncidencesView, name='incidences'),
    path('countries/', CountriesView, name='countries'),
]
