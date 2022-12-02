from django.shortcuts import render

# Create your views here.
from django.middleware.csrf import get_token
from django.http import JsonResponse


def csrf(req):
    return JsonResponse({"csrfToken": get_token(req)})


def index(req):
    return render(req, "chat/index.html")


def room(req, room_name):
    return render(req, "chat/room.html", {"room_name": room_name})
