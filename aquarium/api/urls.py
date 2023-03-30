from django.urls import path
from .views import aqua_change, aqua_check

urlpatterns = [
    path("change/", aqua_change, name="aqua_change"),
    path("check/", aqua_check, name="aqua_check"),
]
