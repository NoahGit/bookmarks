# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/2/28 20:28
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:image_id>/<slug:slug>/', views.image_detail, name='detail'),
]
