# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import salesReport.models as salesReportModels
import salesReport.views as salesReportViews
from salesReport.helpers import simple_order, simple_product, simple_item_in_order, test_order_01, item_test_order_01, simple_order_canceled ,\
    pedido_faturamento_pedido_pedido_com_brinde_01, pedido_faturamento_pedido_pedido_com_brinde_02, periodo_faturamento_pedido_pedido_com_cupom_de_desconto,\
    pedido_faturamento_pedido_pedido_com_frete_a_pagar
from .factorys import brandFactory, itemFactory
import datetime
from dashboard.views import getFaturamentoForDay

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
        created_item = salesReportViews.saveItemInDatabse(simple_product)

        self.assertEqual(True, isinstance(created_item, salesReportModels.item))

    def test_create_order(self):
        """
            Testa a criação de um pedido com um item simples
        """
        created_order = salesReportViews.saveOrderInDatabase(simple_order)
        self.assertEqual(True, isinstance(created_order, salesReportModels.order))

    def test_vmd_1_day(self):
        """
            Get vmd value for 1 day
        """
        dateRange = datetime.timedelta(days=1)
        item = ['Campo0', 'Campo1', 'Campo2', 'Campo3', 3, 5, 0, 0, 0, 0]
        vmd = salesReportViews.getVMD(item, dateRange)

        self.assertEqual(8, vmd)

    def test_vmd_2_days(self):
        """
            Get vmd value for 2 days
        """
        dateRange = datetime.timedelta(days=2)
        item = ['Campo0', 'Campo1', 'Campo2', 'Campo3', 10, 5, 0, 1, 0, 0]
        vmd = salesReportViews.getVMD(item, dateRange)

        self.assertEqual(16, vmd)

    def test_vmd30_for_1_item_in_period(self):
        """
            Teste consistency of vmd30, trivialCase
            1 item sold in last 30 days, vmd will be 0.033
        """
        #create existing data
        brand01 = salesReportModels.brands(name='Marca01')
        item = salesReportModels.item.objects.create(
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
        created_order = salesReportViews.saveOrderInDatabase(simple_order)
        orderItem1 = salesReportModels.orderItem.objects.create(
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
        vmd30 = salesReportViews.getVMD30(item, dateMinus30, dateRangeEnd)

        self.assertEqual(0.033, vmd30)

    def test_vmd30_for_2_item_in_period(self):
        """
            Teste consistency of vmd30, trivialCase
            2 item sold in last 30 days, vmd will be 0.0666666 round to 0.067
        """
        #create existing data
        created_order = salesReportViews.saveOrderInDatabase(simple_order)
    
        item = ['2290', 'Campo1', 'Campo2', 'Campo3', 10, 5, 0, 1, 0, 0]
        dateMinus30 = datetime.datetime(2013, 6, 30) - datetime.timedelta(days=30)
        dateRangeEnd = datetime.datetime(2013, 6, 30)
        vmd30 = salesReportViews.getVMD30(item, dateMinus30, dateRangeEnd)

        self.assertEqual(0.067, vmd30)

    def test_vmd30_for_canceled_item_in_period(self):
        """
            Teste consistency of vmd30, trivialCase
            2 item sold in last 30 days, vmd will be 0.0666666 round to 0.067
        """
        #create existing data
        created_order = salesReportViews.saveOrderInDatabase(simple_order_canceled)

        item = ['2290', 'Campo1', 'Campo2', 'Campo3', 10, 5, 0, 1, 0, 0]
        dateMinus30 = datetime.datetime.today() - datetime.timedelta(days=30)
        dateRangeEnd = datetime.datetime.today()
        vmd30 = salesReportViews.getVMD30(item, dateMinus30, dateRangeEnd)

        self.assertEqual(0.0, vmd30)

class faturamentoTestCase(TestCase):
    """
        0 - Dia consultado
        1 # Pedidos
        2 Vlr Bruto faturado
        3 Receita Frete
        4 Vlr Desconto
        5 Vlr Bonificado
        6 Vlr Liquido Produto
        7 Custo Produtos
        8 Vlr Frete	'
        9 Vlr Taxa Cartão
        10 Margem bruta (Produtos)
        11 Margem bruta (Cartão + Frete)
        12 Tkt Médio
        13 # Produtos pedido
    """
    def setUp(self):
        pass

    def test_faturamento_pedido_01(self):
        """
            Primeiro teste case enviado pelo felipe
            data do pedido=30/06/2013
            Test fraco
        """
        #cria o pedido
        item = salesReportViews.saveItemInDatabse(item_test_order_01)
        order = salesReportViews.saveOrderInDatabase(test_order_01)
        array_esperado = ['1-7', 1, 151.41, 46.51, 10, 0, 94.9, 64.3, 46.51, 2.00, 32.24, 20.22, 94.9, 1.0]
        date = datetime.datetime.strptime('01/07/2013', '%d/%m/%Y')

        faturamento_array = getFaturamentoForDay(date, [0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.assertEqual(array_esperado, faturamento_array)

    def test_faturamento_pedido_pedido_com_frete_a_pagar(self):
        #cria o pedido
        order = salesReportViews.saveOrderInDatabase(pedido_faturamento_pedido_pedido_com_frete_a_pagar)
        array_esperado = ['3-7', 1, 30.86, 6.96, 0, 0, 23.9, 12.5, 6.96, 0.89, 47.7, 34.04, 23.9, 1.0]
        date = datetime.datetime.strptime('03/07/2013', '%d/%m/%Y')

        faturamento_array = getFaturamentoForDay(date, [0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.assertEqual(array_esperado, faturamento_array)

    def test_faturamento_pedido_pedido_com_brinde_01(self):
        #cria o pedido
        order = salesReportViews.saveOrderInDatabase(pedido_faturamento_pedido_pedido_com_brinde_01)
        array_esperado = ['4-7', 1, 159.7, 0, 0, 2.1, 157.6, 100.5, 19.4, 4.63, 36.23, 20.99, 157.6, 3.0]
        date = datetime.datetime.strptime('04/07/2013', '%d/%m/%Y')

        faturamento_array = getFaturamentoForDay(date, [0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.assertEqual(array_esperado, faturamento_array)

    def test_faturamento_pedido_pedido_com_brinde_02(self):
        #cria o pedido
        order = salesReportViews.saveOrderInDatabase(pedido_faturamento_pedido_pedido_com_brinde_02)
        array_esperado = ['2-7', 1, 294.9, 0, 0, 0, 294.9, 183.22, 21, 8.55, 37.87, 27.85, 294.9, 1.0]
        date = datetime.datetime.strptime('02/07/2013', '%d/%m/%Y')

        faturamento_array = getFaturamentoForDay(date, [0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.assertEqual(array_esperado, faturamento_array)

    def test_faturamento_pedido_pedido_com_cupom_de_desconto(self):
        #cria o pedido
        order = salesReportViews.saveOrderInDatabase(periodo_faturamento_pedido_pedido_com_cupom_de_desconto)
        array_esperado = ['3-7', 1, 169.9, 0, 16.99, 0, 152.91, 109.3, 28.1, 4.43, 28.52, 7.24, 152.91, 1.0]
        date = datetime.datetime.strptime('03/07/2013', '%d/%m/%Y')

        faturamento_array = getFaturamentoForDay(date, [0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        self.assertEqual(array_esperado, faturamento_array)


class ExportTestCase(TestCase):
    """
        TODO

    """
    def setUp(self):
        pass

    def export_csv_report(self):
        print 'Executing: export csv test'


class UpdateItemTestCase(TestCase):
    '''
        This test should guarantee the new status for products

    '''

    def setUp(self):
        item = itemFactory(product_id=76,
                                  name=u'LA Top Definition 120 cápsulas (com Cromo) - Integralmédica',
                                  status=False)
        item.save()

    def test_update_item_status(self):
        product_array = {
            'product_id': 76,
            'sku': 76,
            'status': 1,
            'price': 99.99,
            'special_price': 89.99,
        }
        quantidade_atualizada = salesReportViews.updateProductInformation(product_array, 0)
        item = salesReportModels.item.objects.get(product_id=76)
        self.assertEqual(True, item.status)
        self.assertEqual(1, quantidade_atualizada)




class curvaABC(TestCase):
    """
        Test for screen curvaABC
    """

    def setUp(self):
        pass

    def test_item_with_10_percento_of_sales(self):
        """
            Should give:
            valor_faturado_do_dia == 10.00
            valor_faturado_no_periodo == 100
            percentage = 10%
            abc_letter = A
        """
        pass

