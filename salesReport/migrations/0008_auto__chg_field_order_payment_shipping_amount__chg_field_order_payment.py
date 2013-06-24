# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'order.payment_shipping_amount'
        db.alter_column(u'salesReport_order', 'payment_shipping_amount', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'order.payment_amount_ordered'
        db.alter_column(u'salesReport_order', 'payment_amount_ordered', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'order.payment_shipping_amount'
        db.alter_column(u'salesReport_order', 'payment_shipping_amount', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'order.payment_amount_ordered'
        db.alter_column(u'salesReport_order', 'payment_amount_ordered', self.gf('django.db.models.fields.FloatField')(default=0))

    models = {
        u'salesReport.brands': {
            'Meta': {'object_name': 'brands'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'primary_key': 'True'})
        },
        u'salesReport.item': {
            'Meta': {'object_name': 'item'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.brands']", 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'specialPrice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'salesReport.order': {
            'Meta': {'object_name': 'order'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'customer_email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer_firstname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'customer_lastname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'discount_amount': ('django.db.models.fields.FloatField', [], {}),
            'grand_total': ('django.db.models.fields.FloatField', [], {}),
            'increment_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['salesReport.item']", 'through': u"orm['salesReport.orderItem']", 'symmetrical': 'False'}),
            'order_id': ('django.db.models.fields.FloatField', [], {}),
            'payment_amount_ordered': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'payment_shipping_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_amount': ('django.db.models.fields.FloatField', [], {}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'salesReport.orderitem': {
            'Meta': {'object_name': 'orderItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.item']"}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.order']"}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'quantidade': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['salesReport']