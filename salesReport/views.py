# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order, orderItem
import csv
import datetime
def saveOrderInDatabase(o):
    print 'Saving Order: %s' % order
    #TODO

def generateCSV(orderArray):
    salesReport = {}
    itemsHash = []
    for order in orderArray:
        if order['status'] == 'pending':
                for item in order['items']:
                    if item['sku'] not in itemsHash:
                        salesReport[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'qty': 1,
                                                 'qty_holded': 0,
                        }
                        itemsHash.append(item['sku'])
                    else:
                        salesReport[item['sku']]['qty'] += 1
        elif order['status'] == 'holded':
            for item in order['items']:
                if item['sku'] not in itemsHash:
                    salesReport[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'qty': 0,
                                                 'qty_holded': 1,
                    }
                    itemsHash.append(item['sku'])
                else:
                    salesReport[item['sku']]['qty_holded'] += 1
    print salesReport
    #Save csv file
    with open('salesReport.csv', 'wb') as file:
        spamwriter = csv.writer(file, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['sku', 'name', 'qty', 'qty_holded'])
        for item in salesReport:
            spamwriter.writerow([salesReport[item]['sku'], salesReport[item]['name'].encode('utf-8', 'replace')
                                , salesReport[item]['qty'], salesReport[item]['qty_holded']])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salesReport.csv"'

    writer = csv.writer(response)
    writer.writerow(['sku', 'name', 'qty', 'qty_holded'])
    for item in salesReport:
            writer.writerow([salesReport[item]['sku'], salesReport[item]['name'].encode('utf-8', 'replace')
                                , salesReport[item]['qty'], salesReport[item]['qty_holded']])
    return response

def importOrders(request):
    print('-- Start import')
    today = datetime.datetime.now()
    if (today.month < 10):
        month = '0' + str(today.month)
    else:
        month = str(today.month)
    today = str(today.year) + '-' + month + '-' + str(today.day)
    print today

    salesReport = Magento()
    salesReport.connect()
    orders = salesReport.listOrdersSinceStatusDate('holded', today) + \
            salesReport.listOrdersSinceStatusDate('pending', today)
    for order in orders:
        saveOrderInDatabase(order)
    csvFile = generateCSV(orders)
    print('-- End import')
    return csvFile

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response