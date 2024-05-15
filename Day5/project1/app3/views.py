from django.shortcuts import render
from app3.models import Person
from app3.forms import PersonInfoForm
# Create your views here.

def personData(request):
    data = Person.objects.all()
    context = {'person_data': data}
    
    return render(request, "app3/person.html", context)

def personRequest(request):
    form = PersonInfoForm()
    context = {'form': form}
    
    return render(request, "app3/person_request.html", context)
