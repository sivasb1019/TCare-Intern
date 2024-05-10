from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, time

# Create your views here.

def greetings(request):
    current_time = datetime.now().time()
    if time(6, 0, 0) <= current_time < time(12, 0 ,0) :
        message = "<h1> Good Morning Buddy </h1>"
    elif time(12, 0, 0) <= current_time < time(16, 0 ,0):
        message = "<h1> Good Afternoon Buddy </h1>"
    elif time(16, 0, 0) <= current_time < time(18, 0 ,0):
        message = "<h1> Good Evening Buddy </h1>"
    elif time(18, 0, 0) <= current_time < time(23, 0 ,0):
        message = "<h1> Good Night Buddy </h1>"
    else:
        message = "<h1> Its Midnight, Go tho sleep Buddy </h1>"
        
    message = message + f"<h3>{current_time.strftime('%I:%M %p')}</h3>"
    return HttpResponse(message)
