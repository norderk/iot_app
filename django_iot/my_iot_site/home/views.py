import time
import os
from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "home.html", {})


def iot_view(request, *args, **kwargs):
    print(args)
    return render(request, "iot.html", {})


def spotify_view(request):
    return render(request, "spotify.html", {})


def stats_view(request):
    return render(request, "stats.html", {})


def weather_view(request):
    return render(request, "weather.html", {})
