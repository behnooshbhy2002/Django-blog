from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for entire month"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes"
    elif month == "march":
        challenge_text = "Learn Django"
    elif month == "april":
        challenge_text = "Do your best"
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)