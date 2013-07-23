# -*- coding: utf-8 -*-
from django.db import models

class status_history(models.Model):
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    entity_name = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    order = models.ForeignKey('order')

    def __unicode__(self):
        return self.status

class brands(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'brands'
        verbose_name_plural = 'brands'

class item(models.Model):
    product_id = models.IntegerField(primary_key=True)
    weight = models.CharField(max_length=500, null=True, blank=True)
    sku = models.IntegerField(unique=True)
    name = models.CharField(max_length=500)
    cost = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    specialPrice = models.FloatField(null=True, blank=True)
    brand = models.ForeignKey(brands, null=True, blank=True)
    brand_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()
    cmm = models.FloatField(null=True, blank=False)
    estoque_atual = models.IntegerField(null=True, blank=False)
    estoque_empenhado = models.IntegerField(null=True, blank=False)
    estoque_disponivel = models.IntegerField(null=True, blank=False)

    def __unicode__(self):
        return '%s - %s' % (self.product_id, self.name)

class order(models.Model):
    increment_id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField()
    customer_id = models.BigIntegerField(null=True, blank=True)
    subtotal = models.FloatField()
    grand_total = models.FloatField()
    status = models.CharField(max_length=500)
    shipping_method = models.CharField(max_length=500, null=True, blank=True)
    shipping_amount = models.FloatField()
    customer_email = models.CharField(max_length=500, null=True, blank=True)
    customer_firstname = models.CharField(max_length=500, null=True, blank=True)
    customer_lastname = models.CharField(max_length=500, null=True, blank=True)
    order_id = models.FloatField()
    discount_amount = models.FloatField()
    payment_method = models.CharField(max_length=500, null=True, blank=True)
    payment_shipping_amount = models.FloatField(null=True, blank=True)
    shipping_amount_centralfit = models.FloatField(null=True, blank=True)
    payment_amount_ordered = models.FloatField(null=True, blank=True)
    shipping_address_postcode = models.CharField(max_length=500)
    shipping_address_region = models.CharField(max_length=500)
    shipping_address_street = models.CharField(max_length=500)
    weight = models.FloatField()

    #Dados Faturamento
    valorBrutoFaturado = models.FloatField(null=True, blank=True)
    receitaFrete = models.FloatField(null=True, blank=True)
    valorDesconto = models.FloatField(null=True, blank=True)
    valorBonificado = models.FloatField(null=True, blank=True)
    valorBonificadoPedido = models.FloatField(null=True, blank=True)
    custoProdutos = models.FloatField(null=True, blank=True)
    somatoriaProdutos = models.FloatField(null=True, blank=True)
    valorLiquidoProdutos = models.FloatField(null=True, blank=True)
    valorFrete = models.FloatField(null=True, blank=True)
    valorTaxaCartao = models.FloatField(null=True, blank=True)
    margemBrutaSoProdutos = models.FloatField(null=True, blank=True)
    margemBrutaCartaoFrete = models.FloatField(null=True, blank=True)

    item = models.ManyToManyField(item, through='orderItem')

    def __unicode__(self):
        return '%s' % self.increment_id

    def generateBillingInformation(self):
        self.valorBrutoFaturado = 0
        self.receitaFrete = 0
        self.valorDesconto = 0
        self.custoProdutos = 0
        self.valorBonificado = 0
        self.valorBonificadoPedido = 0
        self.somatoriaProdutos = 0
        self.valorLiquidoProdutos = 0
        self.valorFrete = 0
        self.valorTaxaCartao = 0

        self.valorBrutoFaturado += float(self.grand_total)
        if self.discount_amount != 0.0:
            self.valorBrutoFaturado += (float(self.discount_amount) * (-1))
        self.receitaFrete += float(self.shipping_amount)
        self.valorDesconto += (float(self.discount_amount) * (-1))

        self.valorBonificadoPedido = 0
        for item in self.orderitem_set.all():
            #Para produtos com tipos especiais somar o custo somente dos produtos simples
            #Somente produtos simples são somados no variavel somatoria de produtos para calcular o # de produtos pedidos
            if item.productType == 'simple':
                self.custoProdutos += item.item.cost * item.quantidade
            #Para o valor bonificado somar somente os produtos simples (filhos)
            if float(item.price) == 0.0 and item.is_child == False:
                self.valorBonificado += item.item.cost
                self.valorBonificadoPedido += item.item.cost
            if float(item.price) > 0.0:
                #soma ao total de itens analisados, não leva em consideração brindes e produtos complexos(somatoria d produtos simples)
                self.somatoriaProdutos += item.quantidade

        self.valorLiquidoProdutos += float(self.grand_total) - float(self.shipping_amount) - self.valorBonificadoPedido
        if float(self.shipping_amount) > 0.0:
            self.valorFrete += float(self.shipping_amount)
        else:
            self.valorFrete += float(self.shipping_amount_centralfit)

        if self.payment_method == 'BoletoBancario':
            self.valorTaxaCartao += 2.0
        else:
            self.valorTaxaCartao += (float(self.grand_total) * 0.029)

        if self.custoProdutos > 0.0:
            self.margemBrutaSoProdutos = (1 - (self.custoProdutos / self.valorLiquidoProdutos)) * 100
            self.margemBrutaCartaoFrete = (1 - ((self.custoProdutos + self.valorFrete + self.valorTaxaCartao) / (self.valorLiquidoProdutos + self.receitaFrete))) * 100

        self.save()

    def getBillingInfo(self):
        return self.valorBrutoFaturado, self.receitaFrete, self.valorDesconto, self.custoProdutos, self.valorBonificadoPedido, \
        self.valorBonificadoPedido, self.somatoriaProdutos, self.valorLiquidoProdutos, self.valorFrete, self.valorTaxaCartao

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(order, self).save()


class orderItem(models.Model):
    created_at = models.DateTimeField(max_length=500, null=True, blank=True)
    updated_at = models.DateTimeField(max_length=500, null=True, blank=True)
    quantidade = models.FloatField()
    price = models.FloatField()
    is_child = models.BooleanField(default=False)
    productType = models.CharField(max_length=155)

    item = models.ForeignKey(item)
    order = models.ForeignKey(order)

    def __unicode__(self):
        return '%s - %s' % (self.item.name, self.order.increment_id)

class csvReport(models.Model):
    csvFile = models.FileField(upload_to='csv_report')
    created_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.csvFile.url


