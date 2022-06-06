from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('iot/', views.iot_view, name='iot'),
    path('spotify/', views.spotify_view, name="spotify"),
    path('weather/', views.weather_view, name="weather"),
    path('stats/', views.stats_view, name="stats"),
]
