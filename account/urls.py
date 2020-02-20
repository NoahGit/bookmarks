# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/2/20 15:50
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]
