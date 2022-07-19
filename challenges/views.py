from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/janaury/
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    