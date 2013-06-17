# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'item'
        db.create_table(u'salesReport_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_id', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('free_shipping', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'salesReport', ['item'])

        # Adding model 'order'
        db.create_table(u'salesReport_order', (
            ('increment_id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('customer_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('subtotal', self.gf('django.db.models.fields.FloatField')()),
            ('grand_total', self.gf('django.db.models.fields.FloatField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('shipping_method', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('customer_email', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('customer_firstname', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('customer_lastname', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('order_id', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'salesReport', ['order'])

        # Adding model 'orderItem'
        db.create_table(u'salesReport_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(max_length=500, null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(max_length=500, null=True, blank=True)),
            ('quantidade', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('item_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salesReport.item'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salesReport.order'])),
        ))
        db.send_create_signal(u'salesReport', ['orderItem'])

        # Adding model 'brands'
        db.create_table(u'salesReport_brands', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, primary_key=True)),
        ))
        db.send_create_signal(u'salesReport', ['brands'])


    def backwards(self, orm):
        # Deleting model 'item'
        db.delete_table(u'salesReport_item')

        # Deleting model 'order'
        db.delete_table(u'salesReport_order')

        # Deleting model 'orderItem'
        db.delete_table(u'salesReport_orderitem')

        # Deleting model 'brands'
        db.delete_table(u'salesReport_brands')


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
            'item_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.item']"}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.order']"}),
            'quantidade': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['salesReport']