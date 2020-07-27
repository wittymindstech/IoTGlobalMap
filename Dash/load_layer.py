import os
from django.contrib.gis.utils import LayerMapping
from .models import India


india_mapping = {
    'statecode': 'statecode',
    'statename': 'statename',
    'state_ut': 'state_ut',
    'distcode': 'distcode',
    'distname': 'distname',
    'geom': 'MULTIPOLYGON',
}

india_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),"gis_data/India.shp"))

def run(verbose = True):
    lm = LayerMapping(India, india_shp, india_mapping, transform= False, encoding="iso-8859-1")
    lm.save(strict=True, verbose=verbose)