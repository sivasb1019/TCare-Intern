from django.contrib import admin
from django.urls import path
from .views import person

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('person/',person)
]