from django.contrib import admin
from django.urls import path
from .views import personData, personRequest

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('person_data/',personData),
    path('person_request/',personRequest)
]