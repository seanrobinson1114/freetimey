from django.contrib import admin

from trip.models import Trip
from trip.models import TripImage

admin.site.register(Trip)
admin.site.register(TripImage)
