from __future__ import unicode_literals

from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Trip(models.Model):
    trip_name = models.charField(max_length=63)
    picture_name = models.charField(max_length=63)
    blob = ImageField(
    

