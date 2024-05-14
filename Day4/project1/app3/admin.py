from django.contrib import admin
from app3.models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    person_details = ['name', 'age', 'role']

admin.site.register(Person, PersonAdmin)