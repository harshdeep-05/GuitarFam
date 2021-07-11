from re import template
from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name='accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logut/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.Signup.as_view(),name='signup'),
    
]
