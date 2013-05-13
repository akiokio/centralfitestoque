# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.contrib import admin
from salesReport.models import order, orderItem, brands

class orderAdmin(admin.ModelAdmin):
    list_display = ['increment_id', 'status', 'created_at', 'grand_total']
    list_filter = ['status', 'created_at']
    search_fields = ['increment_id', 'status', 'created_at', 'grand_total']

admin.site.register(order, orderAdmin)
admin.site.register(orderItem)
admin.site.register(brands)