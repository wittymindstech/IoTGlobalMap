from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Device

@admin.register(Device)
class DeviceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
