from django.db import models

# Create your models here.

class Device(models.Model):
    '''Models to store sensor data. Implied no defaults since none were implied'''
    date = models.DateField()
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude =models.DecimalField(max_digits=10, decimal_places=4)
    sensor_id = models.IntegerField()
    reading = models.IntegerField()
