# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/2/26 16:36
# File   : authentication.py
# IDE    : PyCharm

from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    # @staticmethod
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    # @staticmethod
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
