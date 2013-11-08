# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'item.quantidade_excedente'
        db.add_column(u'salesReport_item', 'quantidade_excedente',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'item.quantidade_faltante'
        db.add_column(u'salesReport_item', 'quantidade_faltante',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'item.quantidade_excedente'
        db.delete_column(u'salesReport_item', 'quantidade_excedente')

        # Deleting field 'item.quantidade_faltante'
        db.delete_column(u'salesReport_item', 'quantidade_faltante')


    models = {
        u'salesReport.brands': {
            'Meta': {'object_name': 'brands'},
            'meta_dias_estoque': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'cmm': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'estoque_atual': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'estoque_disponivel': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'estoque_empenhado': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'margem': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'quantidade_excedente': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'quantidade_faltante': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
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