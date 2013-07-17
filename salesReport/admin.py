# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.contrib import admin
from salesReport.models import order, orderItem, brands, item, status_history, csvReport

class orderItemInlines(admin.StackedInline):
    model = orderItem

class statusHistoryInlines(admin.StackedInline):
    model = status_history

class orderAdmin(admin.ModelAdmin):
    list_display = ['increment_id', 'status', 'created_at', 'grand_total', 'customer_email']
    list_filter = ['status', 'created_at', 'customer_email']
    search_fields = ['increment_id', 'status', 'created_at', 'grand_total', 'customer_email']

    inlines = [orderItemInlines, statusHistoryInlines]

class orderItemAdmin(admin.ModelAdmin):
    list_display = ['quantidade', 'item', 'created_at', 'price', 'productType', 'is_child']
    list_filter = ['quantidade', 'item', 'created_at', 'price', 'productType', 'is_child']
    search_fields = ['quantidade', 'item', 'created_at', 'price', 'productType', 'is_child']

class itemAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'sku', 'name', 'cost', 'price', 'specialPrice', 'brand']
    list_filter = ['product_id', 'sku', 'name', 'cost', 'price', 'specialPrice', 'brand']
    search_fields = ['product_id', 'sku', 'name', 'cost', 'price', 'specialPrice', 'brand']

admin.site.register(order, orderAdmin)
admin.site.register(orderItem, orderItemAdmin)
admin.site.register(item, itemAdmin)
admin.site.register(brands)
admin.site.register(csvReport)