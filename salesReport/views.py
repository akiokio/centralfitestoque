# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order, orderItem
import csv
import datetime

def saveItemInDatabse(i, parentOrder):
    orderItem.objects.create(item_id=i['item_id'], product_id=i['product_id'], sku=i['sku'], name=i['name'],
                             price=i['price'], order=parentOrder)

def saveOrderInDatabase(o):
    print 'Saving Order: %s' % o['increment_id']
    try:
        databaseOrder = order.objects.get(increment_id=o['increment_id'])
        print('Order in database: %s' % databaseOrder.increment_id)
    except:
        databaseOrder = order.objects.create(increment_id=o['increment_id'], created_at=o['created_at'], updated_at=o['updated_at'],
                             grand_total=o['grand_total'], subtotal=o['subtotal'], status=o['status'])
        for item in o['items']:
            saveItemInDatabse(item, databaseOrder)

def generateCSV(orderArray):
    BRANDS_ARRAY = ['Integralmédica', 'Probiótica', 'Nutrilatina', 'Neonutri', 'Midway', 'X-pharma',
               'Sundown Naturals', 'Musclemeds', 'Muscle Pharm', 'Optimum', 'Dymatize', 'Nutrex',
               'Bony Açaí', 'Pretorian', 'Nutricé', 'Rennovee', 'BNRG', 'Cytosport','MHP', 'MHP Nutrition',
               'Pretorian Hard Sports', 'Nutrilatina AGE']
    salesReport = {}
    itemsHash = []
    for order in orderArray:
        if order['status'] == 'pending':
            for item in order['items']:
                if item['sku'] not in itemsHash:
                    itemDetail = item['name'].split('-')
                    if itemDetail[-1].strip().encode('UTF-8') not in BRANDS_ARRAY and len(itemDetail) >= 2:
                        salesReport[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-2],
                                                 'qty': 1,
                                                 'qty_holded': 0,
                                                 'price': item['price'],
                        }
                    else:
                        salesReport[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-1],
                                                 'qty': 1,
                                                 'qty_holded': 0,
                                                 'price': item['price'],
                        }
                    itemsHash.append(item['sku'])
                else:
                    salesReport[item['sku']]['qty'] += 1
        elif order['status'] == 'holded':
            for item in order['items']:
                if item['sku'] not in itemsHash:
                    itemDetail = item['name'].split('-')
                    if itemDetail[-1].strip().encode('UTF-8') not in BRANDS_ARRAY and len(itemDetail) >= 2:
                        salesReport[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-2],
                                                 'qty': 0,
                                                 'qty_holded': 1,
                                                 'price': item['price'],
                        }
                    else:
                        salesReport[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-1],
                                                 'qty': 0,
                                                 'qty_holded': 1,
                                                 'price': item['price'],
                        }
                    itemsHash.append(item['sku'])
                else:
                    salesReport[item['sku']]['qty_holded'] += 1
    print salesReport

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salesReport.csv"'

    writer = csv.writer(response)
    writer.writerow(['sku', 'name', 'brand', 'qty', 'qty_holded', 'price'])
    for item in salesReport:
            writer.writerow([salesReport[item]['sku'], salesReport[item]['name'].encode('utf-8', 'replace')
                            , salesReport[item]['brand'].encode('utf-8', 'replace')
                            , salesReport[item]['qty'], salesReport[item]['qty_holded']
                            , salesReport[item]['price']])
    return response

def importOrdersSinceDay(request, dateStart):
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
    orders = salesReport.listOrdersSinceStatusDate('holded', dateStart) + \
            salesReport.listOrdersSinceStatusDate('pending', dateStart)
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