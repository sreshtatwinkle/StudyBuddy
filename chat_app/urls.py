from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('chat_page/<str:username>/', views.chat_page, name='chat_page'),
    path('send_message/<str:username>/', views.send_message, name='send_message'),
    path('chat_room/',views.chat_room,name='chat_room')
]
