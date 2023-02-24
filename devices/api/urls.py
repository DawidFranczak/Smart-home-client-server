from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addDevice, name="addDevice"),
    path('add/card/', views.addCard, name="addCard"),
]
