# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from salesReport.models import item, orderItem, order, brands
from salesReport.views import saveItemInDatabse, saveOrderInDatabase, saveOrderItemInDatabase
from salesReport.helpers import simple_order, simple_product, simple_item_in_order


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class salesReportTestCase(TestCase):
    def setUp(self):
        brand01 = brands.objects.create(name='Nutrilatina')

    def test_create_simple_item(self):
        """
            Testa a criação de um item simples na base
        """
        created_item = saveItemInDatabse(simple_product)

        self.assertEqual(True, isinstance(created_item, item))

    def test_create_order(self):
        """
            Testa a criação de um pedido com um item simples
        """
        created_order = saveOrderInDatabase(simple_order)
        self.assertEqual(True, isinstance(created_order, order))

