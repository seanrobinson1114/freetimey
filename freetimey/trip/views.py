from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Context, loader

from .models import Trip

# Create your views here.
def homepage(request):
    trip_list = Trip.objects.all()
    # output = ", ".join([trip.name for trip in trip_list])
    template = loader.get_template('index.html')
    context = Context({'trip_list': trip_list})
    output = template.render(context)
    return HttpResponse(output)
