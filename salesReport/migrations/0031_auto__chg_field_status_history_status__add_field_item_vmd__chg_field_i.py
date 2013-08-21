# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'status_history.status'
        db.alter_column(u'salesReport_status_history', 'status', self.gf('django.db.models.fields.CharField')(default=0, max_length=250))
        # Adding field 'item.vmd'
        db.add_column(u'salesReport_item', 'vmd',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


        # Changing field 'item.cmm'
        # db.alter_column(u'salesReport_item', 'cmm', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'item.cost'
        # db.alter_column(u'salesReport_item', 'cost', self.gf('django.db.models.fields.FloatField')(default=0))

    def backwards(self, orm):

        # Changing field 'status_history.status'
        db.alter_column(u'salesReport_status_history', 'status', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))
        # Deleting field 'item.vmd'
        db.delete_column(u'salesReport_item', 'vmd')


        # Changing field 'item.cmm'
        db.alter_column(u'salesReport_item', 'cmm', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'item.cost'
        db.alter_column(u'salesReport_item', 'cost', self.gf('django.db.models.fields.FloatField')(null=True))

    models = {
        u'salesReport.brands': {
            'Meta': {'object_name': 'brands'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'primary_key': 'True'})
        },
        u'salesReport.csvreport': {
            'Meta': {'object_name': 'csvReport'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'csvFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'salesReport.item': {
            'Meta': {'object_name': 'item'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.brands']", 'null': 'True', 'blank': 'True'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cmm': ('django.db.models.fields.FloatField', [], {}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'estoque_atual': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'estoque_disponivel': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'estoque_empenhado': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'margem': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'specialPrice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vmd': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'salesReport.order': {
            'Meta': {'object_name': 'order'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'custoProdutos': ('django.db.models.fields.FloatField', [], {}),
            'customer_email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer_firstname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'customer_lastname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'discount_amount': ('django.db.models.fields.FloatField', [], {}),
            'grand_total': ('django.db.models.fields.FloatField', [], {}),
            'increment_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['salesReport.item']", 'through': u"orm['salesReport.orderItem']", 'symmetrical': 'False'}),
            'margemBrutaCartaoFrete': ('django.db.models.fields.FloatField', [], {}),
            'margemBrutaSoProdutos': ('django.db.models.fields.FloatField', [], {}),
            'order_id': ('django.db.models.fields.FloatField', [], {}),
            'payment_amount_ordered': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'payment_shipping_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'receitaFrete': ('django.db.models.fields.FloatField', [], {}),
            'shipping_address_postcode': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'shipping_address_region': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'shipping_address_street': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'shipping_amount': ('django.db.models.fields.FloatField', [], {}),
            'shipping_amount_centralfit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'somatoriaProdutos': ('django.db.models.fields.FloatField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'valorBonificado': ('django.db.models.fields.FloatField', [], {}),
            'valorBonificadoPedido': ('django.db.models.fields.FloatField', [], {}),
            'valorBrutoFaturado': ('django.db.models.fields.FloatField', [], {}),
            'valorDesconto': ('django.db.models.fields.FloatField', [], {}),
            'valorFrete': ('django.db.models.fields.FloatField', [], {}),
            'valorLiquidoProdutos': ('django.db.models.fields.FloatField', [], {}),
            'valorTaxaCartao': ('django.db.models.fields.FloatField', [], {}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'salesReport.orderitem': {
            'Meta': {'object_name': 'orderItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_child': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.item']"}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.order']"}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'productType': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'quantidade': ('django.db.models.fields.FloatField', [], {}),
            'removido_estoque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'salesReport.status_history': {
            'Meta': {'object_name': 'status_history'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'entity_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesReport.order']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['salesReport']