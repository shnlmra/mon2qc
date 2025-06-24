from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('routes/', views.routes_view, name='routes'),
    path('view-terminal/', views.terminal_view, name='terminal'),
    path('traffic/', views.traffic_view, name='traffic'),
    path('api/predict-delay/', views.predict_delay, name='predict_delay'),
    path('ibp', views.ibp, name='ibp'),
    path('cmviasanmateo', views.cmviasanmateo, name='cmviasanmateo'),
    path('aurora', views.aurora, name='aurora'),
    path('smnorth', views.smnorth, name='smnorth'),
    path('smnorthviasanmateo', views.smnorthviasanmateo, name='smnorthviasanmateo'),
    path('qave', views.qave, name='qave'),




]
