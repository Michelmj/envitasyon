from django.urls import path
from .import views

urlpatterns = [
    path('', views.maryaj, name='home'),      # root URL now loads maryaj
    path('detay/', views.detay, name='detay'),
    path('rejis/', views.rejis, name='rejis'),
    path('rad/', views.rad, name='rad'),
    path('vwayaj/', views.vwayaj, name='vwayaj'),
    path('maryaj/', views.maryaj, name='maryaj'),
    path('kesyon/', views.kesyon, name='kesyon'),
    path('istwanou/', views.istwanou, name='istwanou'),
]

