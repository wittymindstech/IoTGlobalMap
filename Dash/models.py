from django.db import models

# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    device_type = models.CharField(max_length=60)

    def __str__(self):
        return self.device_name