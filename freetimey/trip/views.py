from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Context, loader

from .models import Trip

class Object(object):
    pass

# Create your views here.
def homepage(request):
    trip_list = Trip.objects.all()
    # trip = Trip.objects.get(pk="Denali July 2015")
    # image_list = trip.images.all()
    trip_images = Object()
    trip_images.trips = trip_list
    trip_images.images = [None] * len(trip_list)
    for index, trip in enumerate(trip_list):
        # trip_images.trip = trip
        trip_images.images[index] = getTripImages(trip)
    template = loader.get_template('index.html')
    # context = Context({'trip_list': trip_list, 'image_list': image_list, 'trip_images': trip_images})
    context = Context({'trip_list': trip_list, 'trip_images': trip_images, 'number_of_trips': range(len(trip_list))})
    output = template.render(context)
    return HttpResponse(output)

def getTripImages(trip_name):
    print "parameter for function: "
    print trip_name
    trip = Trip.objects.get(pk=trip_name)
    image_list = trip.images.all()
    return image_list
