from django.urls import path
from views import change_stairs

urlpatterns = [
    path("change/", change_stairs, name="change_stairs"),
]
