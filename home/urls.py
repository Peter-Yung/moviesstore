from django.urls import path
from . import views

app_name='home' #Django 5.2 need this
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]