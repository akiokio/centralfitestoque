# -*- coding: utf-8 -*-
__author__ = 'akiokio'
import factory
from .models import item, orderItem, order, brands
import datetime
from random import randint, random

class brandFactory(factory.Factory):
    FACTORY_FOR = brands

    name = factory.Sequence(lambda n: 'marca_{0}'.format(n))
    meta_dias_estoque = randint(1, 20)

class itemFactory(factory.Factory):
    FACTORY_FOR = item


    product_id = randint(1, 2000)
    name = factory.LazyAttribute(lambda obj: 'Item%s' % obj.sku)
    weight = 1
    sku = factory.Sequence(lambda n: '%s' % n)
    cost = 10
    price = 20
    specialPrice = 15
    brand = factory.SubFactory(brandFactory)
    status = True
    cmm = 0.333
    vmd = 0
    estoque_atual = 10
    estoque_empenhado = 3
    estoque_disponivel = 7
    valor_faturado_do_dia = 0


class orderFactory(factory.Factory):
    FACTORY_FOR = order

    increment_id = factory.Sequence(lambda n: '%s' % n)
    created_at = datetime.datetime.today()
    updated_at = datetime.datetime.today()
    is_active = True
    customer_id = randint(1, 10000)
    subtotal = randint(1, 100)
    grand_total = randint(1, 1000)
    status = 'complete'
    shipping_method = 'pedroteixeira_correios_41111'
    shipping_amount = randint(1, 50)
    customer_email = factory.LazyAttribute(lambda a: '{0}.{1}@centralfitestoque.com'.format(a.customer_firstname, a.customer_lastname).lower())
    customer_firstname = 'John'
    customer_lastname = 'Doe'
    order_id = factory.Sequence(lambda n: '{0}'.format(n))
    discount_amount = 0.0
    payment_method = 'CreditCard'
    payment_shipping_amount = ''
    shipping_amount_centralfit = randint(1, 50)
    payment_amount_ordered = ''
    shipping_address_postcode = '04105-020'
    shipping_address_region = 'Sao Paulo'
    shipping_address_street = 'Rua Jd. Ivone, 17'
    weight = round(randint(1,30), 2)


class orderItemFactory(factory.Factory):
    FACTORY_FOR = orderItem

    created_at = datetime.datetime.today()
    updated_at = datetime.datetime.today() + datetime.timedelta(minutes=30)
    quantidade = randint(1, 20)
    price = 100
    is_child = False
    productType = 'simple'
    removido_estoque = False

    item = factory.SubFactory(itemFactory)
    order = factory.SubFactory(orderFactory)
