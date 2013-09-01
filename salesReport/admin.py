# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.contrib import admin
from salesReport.models import order, orderItem, brands, item, status_history, csvReport

class orderItemInlines(admin.StackedInline):
    model = orderItem

class statusHistoryInlines(admin.StackedInline):
    model = status_history

class brandAdmin(admin.ModelAdmin):
    list_display = ['name', 'meta_dias_estoque']
    list_filter = ['name', 'meta_dias_estoque']
    search_fields = ['name', 'meta_dias_estoque']

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
    list_display = ['product_id', 'sku', 'name', 'cost', 'price', 'specialPrice', 'brand__sku', 'status', 'vmd']
    list_filter = ['product_id', 'sku', 'name', 'cost', 'price', 'specialPrice', 'brand__sku', 'status', 'vmd']
    search_fields = ['product_id', 'sku', 'name', 'cost', 'price', 'specialPrice', 'brand__sku', 'status', 'vmd']

class csvReportAdmin(admin.ModelAdmin):
    list_display = ['csvFile', 'created_at']
    list_filter = ['csvFile', 'created_at']
    search_fields = ['csvFile', 'created_at']

class status_historyAdmin(admin.ModelAdmin):
    list_display = ['status', 'created_at', 'order']
    list_filter = ['status', 'created_at', 'order']
    search_fields = ['status', 'created_at', 'order__increment_id']

admin.site.register(order, orderAdmin)
admin.site.register(orderItem, orderItemAdmin)
admin.site.register(item, itemAdmin)
admin.site.register(brands, brandAdmin)
admin.site.register(csvReport, csvReportAdmin)

admin.site.register(status_history, status_historyAdmin)