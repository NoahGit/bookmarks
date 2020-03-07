# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/7 10:30
# File   : decorators.py
# IDE    : PyCharm

from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
