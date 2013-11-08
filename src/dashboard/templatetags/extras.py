# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def divide(value, arg):
    return value / arg

@register.filter
def sum(value, arg):
    return value + arg

@register.filter
def remove_minus_sign(value):
    return str(value).replace('-', '')

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    if field == 'order_by' and field in dict_.keys():
      if dict_[field].startswith('-') and dict_[field].lstrip('-') == value:
      # click twice on same column, revert ascending/descending
        dict_[field] = value
      else:
        dict_[field] = "-"+value
    else:
      dict_[field] = value

    return dict_.urlencode()