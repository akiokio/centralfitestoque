# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.contrib import admin
from salesReport.models import order, orderItem, brands

class orderItemInlines(admin.StackedInline):
    model = orderItem

class orderAdmin(admin.ModelAdmin):
    list_display = ['increment_id', 'status', 'created_at', 'grand_total']
    list_filter = ['status', 'created_at']
    search_fields = ['increment_id', 'status', 'created_at', 'grand_total']

class orderItemAdmin(admin.ModelAdmin):
    list_display = ['sku', 'item_id', 'created_at', 'name', 'price']
    list_filter = ['sku', 'item_id', 'created_at', 'name', 'price']
    search_fields = ['sku', 'item_id', 'created_at', 'name', 'price']

admin.site.register(order, orderAdmin)
admin.site.register(orderItem, orderItemAdmin)
admin.site.register(brands)