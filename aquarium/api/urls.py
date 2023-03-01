from django.urls import path
from . import views

urlpatterns = [
    path('change/', views.aquaChange, name="aquaChange"),
    path('check/', views.aquaCheck, name="aquaCheck"),
]
