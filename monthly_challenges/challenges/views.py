from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jan(request):
    return HttpResponse("Eat no meat for entire month")

def feb(request):
    return HttpResponse("Walk for at least 20 minutes")