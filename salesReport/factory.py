# -*- coding: utf-8 -*-
__author__ = 'akiokio'
import factory
from .models import item, orderItem, order, brands
import datetime
from random import randint, random

class brandFactory(factory.Factory):
    FACTORY_FOR = brands

    name = 'Marca1'

class itemFactory(factory.Factory):
    FACTORY_FOR = item

    name = factory.LazyAttribute(lambda obj: 'Item%s' % obj.sku)
    weight = 0
    sku = factory.Sequence(lambda n: '%s' % n)
    cost = 10
    price = 20
    specialPrice = 15
    brand = factory.SubFactory(brandFactory)
    status = True

class orderFactoryCompleteCreditCard(factory.Factory):
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
    customer_email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
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
    weight = round(random(1,30), 2)
