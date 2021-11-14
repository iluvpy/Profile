from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('home/', views.home, name='home'),
	path('create-profile/', views.create_profile, name='create-profile'),
	path('image/<str:token>/', views.image_token, name='image'),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout')
]