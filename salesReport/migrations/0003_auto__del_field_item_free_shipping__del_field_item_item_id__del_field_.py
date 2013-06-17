# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'item.free_shipping'
        db.delete_column(u'salesReport_item', 'free_shipping')

        # Deleting field 'item.item_id'
        db.delete_column(u'salesReport_item', 'item_id')

        # Deleting field 'item.id'
        db.delete_column(u'salesReport_item', u'id')


        # Changing field 'item.sku'
        db.alter_column(u'salesReport_item', 'sku', self.gf('django.db.models.fields.IntegerField')(default=0, unique=True))
        # Adding unique constraint on 'item', fields ['sku']
        db.create_unique(u'salesReport_item', ['sku'])


        # Changing field 'item.product_id'
        db.alter_column(u'salesReport_item', 'product_id', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True))
        # Adding unique constraint on 'item', fields ['product_id']
        db.create_unique(u'salesReport_item', ['product_id'])


        # Changing field 'item.price'
        db.alter_column(u'salesReport_item', 'price', self.gf('django.db.models.fields.FloatField')(default=0, max_length=500))

        # Changing field 'item.cost'
        db.alter_column(u'salesReport_item', 'cost', self.gf('django.db.models.fields.FloatField')(max_length=500, null=True))

        # Changing field 'item.name'
        db.alter_column(u'salesReport_item', 'name', self.gf('django.db.models.fields.CharField')(default=0, max_length=500))

    def backwards(self, orm):
        # Removing unique constraint on 'item', fields ['product_id']
        db.delete_unique(u'salesReport_item', ['product_id'])

        # Removing unique constraint on 'item', fields ['sku']
        db.delete_unique(u'salesReport_item', ['sku'])

        # Adding field 'item.free_shipping'
        db.add_column(u'salesReport_item', 'free_shipping',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'item.item_id'
        db.add_column(u'salesReport_item', 'item_id',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'item.id'
        db.add_column(u'salesReport_item', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


        # Changing field 'item.sku'
        db.alter_column(u'salesReport_item', 'sku', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'item.product_id'
        db.alter_column(u'salesReport_item', 'product_id', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'item.price'
        db.alter_column(u'salesReport_item', 'price', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'item.cost'
        db.alter_column(u'salesReport_item', 'cost', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'item.name'
        db.alter_column(u'salesReport_item', 'name', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    models = {
        u'salesReport.brands': {
            'Meta': {'object_name': 'brands'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'primary_key': 'True'})
        },
        u'salesReport.item': {
            'Meta': {'object_name': 'item'},
            'cost': ('django.db.models.fields.FloatField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.FloatField', [], {'max_length': '500'}),
            'product_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
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