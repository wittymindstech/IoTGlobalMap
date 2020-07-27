from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='IOT Device')
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name

    @property
    def popupContent(self):
      return self.name