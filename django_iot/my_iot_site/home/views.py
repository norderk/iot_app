from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def iot_view(request):
    return render(request, "iot.html", {})


def spotify_view(request):
    return HttpResponse("this is Spotify")


def stats_view(request):
    return HttpResponse("this is stats")


def weather_view(request):
    return HttpResponse("this is the weather")
