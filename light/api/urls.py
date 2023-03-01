from django.urls import path
from . import views


urlpatterns = [
    path('light/', views.changeLight, name='changeLight'),

]
