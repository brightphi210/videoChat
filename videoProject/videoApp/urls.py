
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.videoCallView, name='meeting'),
    path('logout/', views.logoutView, name='logout'),
    path('join/', views.joinRoom, name='join'),
]  