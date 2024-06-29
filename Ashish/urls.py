from django.contrib import admin
from django.urls import path
from Ashish import views;

urlpatterns = [
    path('', views.home , name = 'home'),
    path('login', views.login , name = 'login'),
    path('signup', views.signup , name = 'signup'),
    path('about_us', views.about_us , name = 'about_us'),
    path('profile', views.profile , name = 'profile'),
    path('settings', views.settings , name = 'settings'),
]