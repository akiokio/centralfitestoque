# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order, orderItem, brands
import csv
import datetime
from datetime import date, timedelta

def saveItemInDatabse(i, parentOrder):
    orderItem.objects.create(item_id=i['item_id'], product_id=i['product_id'], sku=i['sku'], name=i['name'],
                             price=i['price'], order=parentOrder)

def saveOrderInDatabase(o):
    print 'Saving Order: %s' % o['increment_id']
    try:
        databaseOrder = order.objects.get(increment_id=o['increment_id'])
        print('Order in database: %s' % databaseOrder.increment_id)
    except:
        print '%s - %s - %s' % (int(o['created_at'][0:4]), int(o['created_at'][5:7]), int(o['created_at'][8:10]))
        created_at = datetime.datetime.strptime(o['created_at'].split(' ')[0], '%Y-%m-%d')
        updated_at = datetime.datetime.strptime(o['updated_at'].split(' ')[0], '%Y-%m-%d')
        databaseOrder = order.objects.create(increment_id=o['increment_id'],
                     created_at=created_at,updated_at=updated_at,
                     grand_total=o['base_grand_total'], subtotal=o['base_subtotal'], status=o['status'])
        for item in o['items']:
            saveItemInDatabse(item, databaseOrder)


def getVMD30(dateRangeInit, dateStart, item, dateEnd, last30DaysOrders):
    print('Generate VMD30 for : %s' % item)
    totalInPeriod = 0
    for last30DaysOrder in last30DaysOrders:
        for last30DaysItem in last30DaysOrder.orderItem.all():
            if last30DaysItem.sku == item:
                totalInPeriod += 1
    VMD30 = totalInPeriod / 30
    return VMD30


def getVMD(dateStart, item, salesReport, dateRangeInit, dateEnd):
    print('Generate VMD for : %s' % item)
    dateEnd = date(int(dateEnd[0:4]), int(dateEnd[5:7]), int(dateEnd[8:10]))
    dateRangeInDays = dateEnd - dateRangeInit
    if dateRangeInDays.days == 0:
        vmd = float(int(salesReport[item]['qty']) + int(salesReport[item]['qty_holded']) / 1)
    else:
        vmd = float(int(salesReport[item]['qty']) + int(salesReport[item]['qty_holded']) / dateRangeInDays.days)
    return vmd


def saveCSV(salesReport, dateStart, dateEnd):
    print('Saving CSV File')
    dateRangeInit = date(int(dateStart[0:4]), int(dateStart[5:7]), int(dateStart[8:10]))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salesReport.csv"'
    writer = csv.writer(response)
    writer.writerow(['sku', 'name', 'brand', 'qty', 'qty_holded', 'price', 'VMD', 'VMD30'])
    dateMinus30 = dateRangeInit - timedelta(days=30)
    last30DaysOrders = order.objects.filter(created_at__gte=dateMinus30).filter(created_at__lte=dateRangeInit)
    for item in salesReport:
        vmd = getVMD(dateStart, item, salesReport, dateRangeInit, dateEnd)

        # VMD30 = getVMD30(dateRangeInit, dateStart, item, dateEnd, last30DaysOrders)

        writer.writerow([salesReport[item]['sku'], salesReport[item]['name'].encode('utf-8', 'replace')
                        , salesReport[item]['brand'].encode('utf-8', 'replace')
                        , salesReport[item]['qty'], salesReport[item]['qty_holded']
                        , salesReport[item]['price'], vmd])
    return response


def generateCSV(orderArray, dateStart, dateEnd):
    BRANDS_ARRAY = []
    for brand in brands.objects.all():
        BRANDS_ARRAY.append(brand.name.encode('UTF-8'))
    salesReportDict = {}
    itemsHash = []
    for order in orderArray:
        if order['status'] == 'processing':
            for item in order['items']:
                if item['sku'] not in itemsHash:
                    itemDetail = item['name'].split('-')
                    if itemDetail[-1].strip() not in BRANDS_ARRAY and len(itemDetail) >= 2:
                        salesReportDict[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-2],
                                                 'qty': 1,
                                                 'qty_holded': 0,
                                                 'price': item['price'],
                        }
                    else:
                        salesReportDict[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-1],
                                                 'qty': 1,
                                                 'qty_holded': 0,
                                                 'price': item['price'],
                        }
                    itemsHash.append(item['sku'])
                else:
                    salesReportDict[item['sku']]['qty'] += 1
        elif order['status'] == 'holded':
            for item in order['items']:
                if item['sku'] not in itemsHash:
                    itemDetail = item['name'].split('-')
                    if itemDetail[-1].strip().encode('UTF-8') not in BRANDS_ARRAY and len(itemDetail) >= 2:
                        salesReportDict[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-2],
                                                 'qty': 0,
                                                 'qty_holded': 1,
                                                 'price': item['price'],
                        }
                    else:
                        salesReportDict[item['sku']] = {'sku': item['sku'],
                                                 'name': item['name'],
                                                 'brand': itemDetail[-1],
                                                 'qty': 0,
                                                 'qty_holded': 1,
                                                 'price': item['price'],
                        }
                    itemsHash.append(item['sku'])
                else:
                    salesReportDict[item['sku']]['qty_holded'] += 1

    return saveCSV(salesReportDict, dateStart, dateEnd)

def importOrdersSinceDay(request, dateStart, dateEnd):
    print('-- Start import')
    salesReport = Magento()
    salesReport.connect()
    orders = salesReport.listOrdersSinceStatusDate('holded', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('processing', dateStart, dateEnd)
    for order in orders:
        saveOrderInDatabase(order)
    csvFile = generateCSV(orders, dateStart, dateEnd)
    print('-- End import')
    return csvFile