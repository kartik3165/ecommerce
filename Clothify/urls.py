from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('auth', views.auth, name='auth'),

    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login')
]