from django.contrib import admin
from django.urls import path
from .views import greetings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('greetings/',greetings)
]