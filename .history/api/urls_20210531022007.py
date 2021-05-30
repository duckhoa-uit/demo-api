from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/register/', views.register, name='register'),
    # path('auth/login/', views.login, name='login'),
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('users/', views.getAllUsers, name='all_users'),
    
]