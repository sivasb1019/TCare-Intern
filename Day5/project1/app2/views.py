from django.shortcuts import render
from datetime import datetime, time

# Create your views here.

def greetings(request):
    current_time = datetime.now().time()
    if time(6, 0, 0) <= current_time < time(12, 0 ,0) :
        message = "Good Morning Buddy"
    elif time(12, 0, 0) <= current_time < time(16, 0 ,0):
        message = "Good Afternoon Buddy"
    elif time(16, 0, 0) <= current_time < time(18, 0 ,0):
        message = "Good Evening Buddy"
    elif time(18, 0, 0) <= current_time < time(23, 0 ,0):
        message = "Good Night Buddy"
    else:
        message = "Its Midnight, Go tho sleep Buddy"

    current_time = current_time.strftime('%I:%M %p')
    context = {'message': message, 'current_time': current_time}
    
    return render(request, 'app2/greetings.html', context)
