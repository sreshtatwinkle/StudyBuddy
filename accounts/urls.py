from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register_form,name='register'),
    path('login',views.login_form,name='login'),
    path('logout',views.logout,name='logout')
]