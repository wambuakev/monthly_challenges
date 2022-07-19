from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"
    if month == 'february':
        challenge_text = "Walk at least 20 minutes everyday!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes everyday!"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)