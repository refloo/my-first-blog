from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('day/', views.day, name='day'),
    path('study/', views.study, name='study'),
    path('magic/', views.magic, name='magic'),
    path('buy/', views.buy, name='buy'),
    path('day/u/', views.update, name='update'),
    path('day/w/', views.merukari, name='merukari'),
]