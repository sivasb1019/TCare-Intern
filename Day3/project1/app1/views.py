from django.shortcuts import render

def welcome(request):
    return render(request, 'app1/welcome.html')