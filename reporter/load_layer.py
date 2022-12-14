import os
from django.contrib.gis.utils import LayerMapping
from .models import Countries

countries_mapping = {
    'countries' : 'countries',
    'codes' : 'codes',
    'city_code' : 'city_CODE',
    'dis' : 'dis',
    'geom' : 'MULTIPOLYGON',
}

country_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/countries.shp'))

def run(verbose=True):
    lm = LayerMapping(Countries, country_shp, countries_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)