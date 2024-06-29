from django.contrib import admin
from django.urls import path
from Ashish import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('about_us', views.about_us, name='about_us'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('shop/', views.shop, name='shop'),
    path('edit/<int:pk>/', views.furniture_edit, name='furniture_edit'),
    path('furniture/new/', views.furniture_create, name='furniture_create'),
    path('furniture/<int:pk>/', views.furniture_detail, name='furniture_detail'),
    path('furniture/<int:pk>/edit/',
         views.furniture_edit, name='furniture_update'),
    path('furniture/<int:pk>/delete/',
         views.furniture_delete, name='furniture_delete'),
    path('delete/<int:pk>/', views.furniture_delete,
         name='furniture_delete'),  # Example delete view
    path('furniture/<int:pk>/delete/', views.furniture_delete,
         name='furniture_delete_confirm'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
]
