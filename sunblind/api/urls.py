from django.urls import path

from .views import message_sunblind

urlpatterns = [
    path("message/", message_sunblind, name="message_sunblind"),
]
