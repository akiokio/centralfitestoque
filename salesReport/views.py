# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order, orderItem, brands
import csv
import datetime
from datetime import date, timedelta

def saveItemInDatabse(i, parentOrder):
    orderItem.objects.create(item_id=i['item_id'], product_id=i['product_id'], sku=i['sku'], name=i['name'],
                             price=i['price'], order=parentOrder, created_at=parentOrder.created_at)

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
                     created_at=created_at, updated_at=updated_at,
                     grand_total=o['base_grand_total'], subtotal=o['base_subtotal'], status=o['status'])
        for item in o['items']:
            saveItemInDatabse(item, databaseOrder)


def getVMD30(item, dateMinus30, dateRangeEnd):
    totalInPeriod = orderItem.objects.filter(sku=item[0]).filter(created_at__range=[dateMinus30, dateRangeEnd])
    vmd30 = len(totalInPeriod) / 30
    return vmd30


def getVMD(item, dateRangeInDays):
    if dateRangeInDays.days == 0:
        vmd = float(item[4] + item[5] / 1)
    else:
        vmd = float(item[4] + item[5] / dateRangeInDays.days)
    return vmd


def saveCSV(productList, dateStart, dateEnd):
    print('Saving CSV File')
    dateRangeInit = date(int(dateStart[0:4]), int(dateStart[5:7]), int(dateStart[8:10]))
    dateRangeEnd = date(int(dateEnd[0:4]), int(dateEnd[5:7]), int(dateEnd[8:10]))
    dateRangeInDays = dateRangeEnd - dateRangeInit
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salesReport.csv"'
    writer = csv.writer(response)
    writer.writerow(['sku', 'name', 'brand', 'price', 'qty', 'qty_holded', 'VMD', 'VMD30'])
    dateMinus30 = dateRangeEnd - timedelta(days=30)
    for item in productList:
        vmd = getVMD(item, dateRangeInDays)

        VMD30 = getVMD30(item, dateMinus30, dateRangeEnd)

        writer.writerow([item[0].encode('UTF-8'), item[1].encode('utf-8', 'replace'), item[2].encode('utf-8', 'replace')
                        , item[3], item[4], item[5], vmd, VMD30])
    return response


def generateCSV(orderArray, dateStart, dateEnd, itemsHash, productList):
    for order in orderArray:
        if order['status'] == 'processing':
            for item in order['items']:
                productList[itemsHash.index(item['sku'])][4] += 1
        elif order['status'] == 'holded':
            for item in order['items']:
                productList[itemsHash.index(item['sku'])][5] += 1

    return saveCSV(productList, dateStart, dateEnd)

def getBrand(item, BRANDS_ARRAY):
    itemDetail = item['name'].split('-')
    if itemDetail[-1].strip().encode('UTF-8') not in BRANDS_ARRAY and len(itemDetail) >= 2:
        #Case X-Pharma
        testString = itemDetail[-1] + '-' + itemDetail[-2]
        if testString == 'X-Pharma':
            return testString
        return itemDetail[-2]
    else:
        return itemDetail[-1]

def importOrdersSinceDay(request, dateStart, dateEnd):
    print('-- Start import')
    salesReport = Magento()
    salesReport.connect()
    orders = salesReport.listOrdersSinceStatusDate('holded', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('processing', dateStart, dateEnd)

    itemsHash = []
    productList = []

    BRANDS_ARRAY = []
    for brand in brands.objects.all():
        BRANDS_ARRAY.append(brand.name.encode('UTF-8'))

    for product in salesReport.getProductArray():
        itemsHash.append(product['sku'])
        productList.append([product['sku'], product['name'], getBrand(product, BRANDS_ARRAY), product['price'], 0, 0])

    for order in orders:
        saveOrderInDatabase(order)
    csvFile = generateCSV(orders, dateStart, dateEnd, itemsHash, productList)
    print('-- End import')
    return csvFile