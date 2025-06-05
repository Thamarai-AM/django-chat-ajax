from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list-chat',views.list_chat_rooms,name='list'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]