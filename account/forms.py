# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/2/20 15:38
# File   : forms.py
# IDE    : PyCharm

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)