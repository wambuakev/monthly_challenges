from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

import challenges

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk at least 20 minutes every day!")

def march(request):
    return HttpResponse("Learn Django for at least 20 minutes every day!")

def monthly_challenge(request, month):
    return HttpResponse()