from django.shortcuts import render
from app3.models import Person
# Create your views here.

def person(request):
    data = Person.objects.all()
    context = {'person_data': data}
    
    return render(request, "app3/person.html", context)
