from django.urls import path

from .views import toggle_light

urlpatterns = [
    path("light/", toggle_light, name="change_light"),
]
