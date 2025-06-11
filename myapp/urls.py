from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('routes/', views.routes_view, name='routes'),
    path('view-terminal/', views.terminal_view, name='terminal'),
    path('traffic/', views.traffic_view, name='traffic'),
]
