import time
import os
from django.shortcuts import render
from django.http import HttpResponse
import sys
import subprocess
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt

def home_view(request):
    return render(request, "home.html", {})

@csrf_exempt
def iot_view(request, *args, **kwargs):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print("AJAX WAS USED!")
    return render(request, "iot.html", {})

@csrf_exempt
def iot_action(request, *args, **kwargs):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print("AJAX WAS USED!")
    topic = "living_room"
    payload = "ON"
    arg_lst = ["python3", "test_system.py", "--topic", f"{topic}", "--payload", f"{payload}"]
    subprocess.Popen(arg_lst, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

def spotify_view(request):
    return render(request, "spotify.html", {})

def stats_view(request):
    return render(request, "stats.html", {})

def weather_view(request):
    return render(request, "weather.html", {})
