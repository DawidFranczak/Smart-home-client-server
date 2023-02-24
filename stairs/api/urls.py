from django.urls import path
from . import views

urlpatterns = [
    path('change/', views.changeStairs, name="changeStairs"),
]
