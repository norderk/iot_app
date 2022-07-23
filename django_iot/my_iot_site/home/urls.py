from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('iot/', views.iot_view, name='iot'),
    path('spotify/', views.spotify_view, name="spotify"),
    path('weather/', views.weather_view, name="weather"),
    path('stats/', views.stats_view, name="stats"),
    path('simple_function/', views.simple_function, name='simple_function'),
    path('simple_function_on/', views.simple_function_on, name='simple_function_on'),
    path('test_slug/<slug:slug>/', views.test_slug),

    # routing pure function calls
    # path('call_mqtt/', views.iot_action, name='call_mqtt/')

]
