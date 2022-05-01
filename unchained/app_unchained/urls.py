from django import urls
from django.urls import path
from . import views

app_name="app_unchained"
urlpatterns=[
    path('', views.index, name='index'),

    path('create', views.create_index, name='create'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('update/<int:id>', views.update_view, name="update" ),
    path('delete/<int:id>', views.delete_view, name='delete' ),

    path('chat', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
]