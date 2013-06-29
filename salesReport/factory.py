# -*- coding: utf-8 -*-
__author__ = 'akiokio'
import factory
from .models import item, orderItem, order, brands

class brandFactory(factory.FACTORY):
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
    brand = factory.SubFactory(brandFactory, name='Nutrilatina')
    status = True

class orderFactory(factory.Factory):
    FACTORY_FOR = order
