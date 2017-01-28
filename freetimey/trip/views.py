from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def greeting(request):
    return HttpResponse('Hello, from Trips')
