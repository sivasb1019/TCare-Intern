from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    message = "<h1>Welcome SB</h1>"
    return HttpResponse(message)