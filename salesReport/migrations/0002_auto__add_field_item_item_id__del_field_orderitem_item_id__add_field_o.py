# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'item.item_id'
        db.add_column(u'salesReport_item', 'item_id',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'orderItem.item_id'
        db.delete_column(u'salesReport_orderitem', 'item_id_id')

        # Adding field 'orderItem.item'
        db.add_column(u'salesReport_orderitem', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['salesReport.item']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'item.item_id'
        db.delete_column(u'salesReport_item', 'item_id')

        # Adding field 'orderItem.item_id'
        db.add_column(u'salesReport_orderitem', 'item_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['salesReport.item']),
                      keep_default=False)

        # Deleting field 'orderItem.item'
        db.delete_column(u'salesReport_orderitem', 'item_id')


    models = {
        u'salesReport.brands': {
            'Meta': {'object_name': 'brands'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'primary_key': 'True'})
        },
        u'salesReport.item': {
            'Meta': {'object_name': 'item'},
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'free_shipping': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'product_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'salesReport.order': {
            'Meta': {'object_name': 'order'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'customer_email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer_firstname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'customer_lastname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'grand_total': ('django.db.models.fields.FloatField', [], {}),
            'increment_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['salesReport.item']", 'through': u"orm['salesReport.orderItem']", 'symmetrical': 'False'}),
            'order_id': ('django.db.models.fields.FloatField', [], {}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'salesReport.orderitem': {
            'Meta': {'object_name': 'orderItem'},
            'created_at': ('django.db.models.fields.DateField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.item']"}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.order']"}),
            'quantidade': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['salesReport']