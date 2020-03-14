# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/14 10:26
# File   : signals.py
# IDE    : PyCharm

from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()