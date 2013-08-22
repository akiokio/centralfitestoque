# -*- coding: utf-8 -*-
__author__ = 'akiokio'

from django.core.management.base import NoArgsCommand
from salesReport.models import item as product, brands
from salesReport.pymagento import Magento
from salesReport.views import getBrand, getVMD30ForDatabaseItem
import datetime

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Command(NoArgsCommand):
    help = "Describe the Command Here"

    def handle_noargs(self, **options):
        print 'Inicio'
        salesReport = Magento()
        salesReport.connect()

        for item in salesReport.getProductArray():
            if RepresentsInt(item['sku']):
                try:
                    database_item = product.objects.get(sku=item['sku'])
                except:
                    break

                if not 'marca' in item:
                    item['marca'] = getBrand(item)

                try:
                    marca = brands.objects.get(name=item['marca'][:100])
                except Exception as e:
                    print e
                    marca = brands.objects.create(name=item['marca'][:100], meta_dias_estoque=1)

                database_item.brand = marca
                database_item.save()

        dateInit = datetime.datetime.today().replace(hour=0, minute=0, second=0) - datetime.timedelta(hours=3)
        dateEnd = datetime.datetime.today().replace(hour=23, minute=59, second=59) - datetime.timedelta(days=30) - datetime.timedelta(hours=3)

        for item in product.objects.all():
            item.vmd = getVMD30ForDatabaseItem(item, dateEnd, dateInit)
            item.save()

