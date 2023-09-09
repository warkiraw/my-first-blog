from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('base', views.basik, name='basic'),
    path('game1', views.get_random_number, name='get_random_number'),
    path('game2', views.get_random_box, name='get_random_box'),
    path('game3', views.get_mathik, name='get_mathik'),
    path('game4/', views.problems, name='problems'),
    path('make_problems', views.make_problems, name='make_problems'),
]