from django.urls import path
from . import views

app_name='movies' #Django 5.2 need this
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.show, name='show'),
]