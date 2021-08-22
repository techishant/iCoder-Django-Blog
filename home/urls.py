from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
        path('', views.home, name='home'),
        path('contact', views.contact, name='contact'),
        path('about', views.about, name='about'),
        path('register', views.register, name='register'),
        path('login', views.loginPage, name='loginPage'),
        path('logout', views.logoutPage, name='logoutPage'),
        path('dashboard', views.dashboard, name='dashboard')
]