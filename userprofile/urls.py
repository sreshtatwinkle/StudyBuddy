from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('register',views.registration,name='register'),
    path('login',views.login_form,name='login'),
    path('logout',views.logout_form,name='logout'),
    path('addmodules',views.addmodules,name='addmodules'),
    path('profiles',views.profiles,name='profiles')
]