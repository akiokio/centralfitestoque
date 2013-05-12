# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.contrib import admin
from salesReport.models import order, orderItem, brands

admin.site.register(order)
admin.site.register(orderItem)
admin.site.register(brands)