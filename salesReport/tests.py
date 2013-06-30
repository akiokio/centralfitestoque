# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from salesReport.models import item as modelItem, orderItem as modelOrderItem, order as modelOrder, brands as modelBrands
from salesReport.views import saveItemInDatabse, saveOrderInDatabase, saveOrderItemInDatabase, getVMD, getVMD30
from salesReport.helpers import simple_order, simple_product, simple_item_in_order
# from salesReport.factory import brandFactory, itemFactory
import datetime

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class salesReportTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_simple_item(self):
        """
            Testa a criação de um item simples na base
        """
        created_item = saveItemInDatabse(simple_product)

        self.assertEqual(True, isinstance(created_item, modelItem))

    def test_create_order(self):
        """
            Testa a criação de um pedido com um item simples
        """
        created_order = saveOrderInDatabase(simple_order)
        self.assertEqual(True, isinstance(created_order, modelOrder))

    def test_vmd_1_day(self):
        """
            Get vmd value for 1 day
        """
        dateRange = datetime.timedelta(days=1)
        item = ['Campo0', 'Campo1', 'Campo2', 'Campo3', 3, 5, 0, 0, 0, 0]
        vmd = getVMD(item, dateRange)

        self.assertEqual(8, vmd)

    def test_vmd_2_days(self):
        """
            Get vmd value for 2 days
        """
        dateRange = datetime.timedelta(days=2)
        item = ['Campo0', 'Campo1', 'Campo2', 'Campo3', 10, 5, 0, 1, 0, 0]
        vmd = getVMD(item, dateRange)

        self.assertEqual(16, vmd)

    def test_vmd30_for_1_item_in_period(self):
        """
            Teste consistency of vmd30, trivialCase
            1 item sold in last 30 days, vmd will be 0.033
        """
        #create existing data
        brand01 = modelBrands(name='Marca01')
        item = modelItem.objects.create(
            product_id = 1,
            weight = 1.0,
            sku = '123',
            name = 'Item1',
            cost = 10,
            price = 20,
            specialPrice = 19.99,
            brand = brand01,
            status = 'enable'
        )
        created_order = saveOrderInDatabase(simple_order)
        orderItem1 = modelOrderItem.objects.create(
            created_at = datetime.datetime.today(),
            updated_at = datetime.datetime.today(),
            quantidade = 3,
            price = 12.99,
            is_child = False,
            productType = 'simple',
            item = item,
            order = created_order
        )
        item = ['123', 'Campo1', 'Campo2', 'Campo3', 10, 5, 0, 1, 0, 0]
        dateMinus30 = datetime.datetime.today() - datetime.timedelta(days=30)
        dateRangeEnd = datetime.datetime.today()
        vmd30 = getVMD30(item, dateMinus30, dateRangeEnd)

        self.assertEqual(0.033, vmd30)

    def test_vmd30_for_2_item_in_period(self):
        """
            Teste consistency of vmd30, trivialCase
            2 item sold in last 30 days, vmd will be 0.0666666 round to 0.067
        """
        #create existing data
        created_order = saveOrderInDatabase(simple_order)
    
        item = ['2290', 'Campo1', 'Campo2', 'Campo3', 10, 5, 0, 1, 0, 0]
        dateMinus30 = datetime.datetime.today() - datetime.timedelta(days=30)
        dateRangeEnd = datetime.datetime.today()
        vmd30 = getVMD30(item, dateMinus30, dateRangeEnd)

        self.assertEqual(0.067, vmd30)
#
# class importTestCase(TestCase):
#     def setUp(self):
#         pass




