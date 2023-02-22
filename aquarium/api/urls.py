from django.urls import path
from . import views

urlpatterns = [
    path('aquarium/change', views.aquaChange, name="aquaChange"),
    path('aquarium/check', views.aquaCheck, name="aquaCheck"),
]
