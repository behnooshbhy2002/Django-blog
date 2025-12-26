from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Read 10 pages of a book every day",
    "may": "Drink at least 8 glasses of water every day",
    "june": "Do 15 minutes of stretching every day",
    "july": "Write 5 minutes of journaling every day",
    "august": "Learn 10 new English words every day",
    "september": "No sugar for the entire month",
    "october": "Meditate for at least 10 minutes every day",
    "november": "Save money: no unnecessary spending",
    "december": "Message or call one friend/family member every day"
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        HttpResponseNotFound("Invalid number")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    challenge_text = None
    try: 
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
    