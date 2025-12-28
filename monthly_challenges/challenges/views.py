from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })
    
    # for m in months:
    #     cap_m = m.capitalize()
    #     m_path = reverse("month-challenge", args=[m])
    #     list_items += f"<li><a href=\"{m_path}\">{cap_m}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h2>Invalid number</h2>")
    else: 
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/month
        return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = None
    try: 
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{month} : {challenge_text}</h1>"
        
        # response_data_html = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data_html)
        # cap_month = month.capitalize()
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month": month
        })
        
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    