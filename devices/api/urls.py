from django.urls import path
from views import add_new_card, add_new_device

urlpatterns = [
    path("add/", add_new_device, name="addDevice"),
    path("add/card/", add_new_card, name="addCard"),
]
