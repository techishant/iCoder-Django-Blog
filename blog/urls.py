from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('new', views.new, name='new'),
    path('deletepost', views.deletepost, name='deletepost'),
    path('editpost', views.editpost, name='editpost'),
    path('update', views.update, name='update'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]