from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.basic,name="basic"),
    path('stockpicker', views.stockpicker, name = 'stockpicker'),
    path('stocktracker/', views.stocktracker, name = 'stocktracker'),
]