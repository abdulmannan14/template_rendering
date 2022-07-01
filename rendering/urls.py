from django.contrib import admin
from django.urls import path, include
from . import views as rendering_views

urlpatterns = [
    path('', rendering_views.index, name='index'),
    path('login', rendering_views.login, name='login'),
    path('signup', rendering_views.signup, name='signup'),
]
