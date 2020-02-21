# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/2/20 15:50
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]
