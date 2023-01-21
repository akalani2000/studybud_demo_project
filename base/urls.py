from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('update_user', views.update_user, name='update-user'),

    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.user_profile, name='profile'),

    path('room/<str:pk>/', views.room, name='room'),
    path('topics', views.user_topics, name='topics'),
    path('activities', views.user_activities, name='activities'),
    path('create_room', views.create_room, name='create-room'),
    path('update_room/<str:pk>/', views.update_room, name='update-room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete-room'),

    path('delete_message/<str:pk>/', views.delete_message, name='delete-message'),

]

