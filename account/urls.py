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
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="account/password_reset_form.html",
             email_template_name="account/password_reset_email.html",
             subject_template_name="account/password_reset_subject.txt",
             success_url="/account/password-reset-done/",
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="account/password_reset_done.html"
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="account/password_reset_confirm.html",
             success_url="/account/password-reset-complete/",
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="account/password_reset_complete.html"
         ),
         name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
