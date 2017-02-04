from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

class Trip(models.Model):
    name = models.CharField(primary_key=True, max_length=63, unique=True, help_text='Should be same as folder name')
    date = models.DateField()
    state = models.CharField(max_length=63)
    area = models.CharField(max_length=63, help_text='e.g. Little Bear, Denali, Sante Fe, West Coast, ...')
    type = models.CharField(max_length=63, help_text='e.g. Mountaineering, Hiking, Family Vacation, Climbing, ...')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class TripImage(models.Model):
    name = models.ForeignKey(Trip, related_name='images')
    description = models.CharField(max_length=63, null=True, help_text="trip_name + pic file name")
    image = models.ImageField(storage=fs)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['name']
