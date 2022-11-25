from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(req):
    return render(req, "chat/index.html")


def room(req, room_name):
    return render(req, "chat/room.html", {"room_name": room_name})
