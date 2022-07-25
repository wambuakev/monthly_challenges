from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february":"Walk at least 20 minutes everyday!",
    "march":"Learn Django for at least 20 minutes everyday!",
    "april":"Eat no meat for the entire month!",
    "may":"Walk at least 20 minutes everyday!",
    "june":"Learn Django for at least 20 minutes everyday!",
    "july":"Eat no meat for the entire month!",
    "august":"Walk at least 20 minutes everyday!",
    "september":"Learn Django for at least 20 minutes everyday!",
    "october":"Eat no meat for the entire month!",
    "november":"Walk at least 20 minutes everyday!",
    "december":"Learn Django for at least 20 minutes everyday!",
    
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    # "<ul><a href="...">January</a></li><ul><a href="...">February</a></li>..."
    
    response_data = f"<ul>{list_items}</ul"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/janaury/
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    #try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    #except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    