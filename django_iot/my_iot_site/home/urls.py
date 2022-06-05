from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='start-page'),
    path('home/', views.home_view, name='start-page'),
    path('iot/', views.iot_view, name='iot-page'),
    path('spotify/', views.spotify_view, name="spotify-page"),
    path('weather/', views.weather_view, name="weather-page"),
    path('stats/', views.stats_view, name="stats-page"),
]
