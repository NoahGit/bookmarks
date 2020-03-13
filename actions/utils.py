# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/13 16:18
# File   : utils.py
# IDE    : PyCharm

import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user, verb, target=None):
    # check for any similar action made in the last minute检查任何类似的行动在最后一分钟
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)
    if not similar_actions:
        # no existing actions found未找到现有操作
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
