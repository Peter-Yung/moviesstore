from django.urls import path
from . import views

app_name='accounts' #Django 5.2 need this
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('orders/', views.orders, name='orders'),
]