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

def getQtyHolded(item, dateEnd):
    dateStart = dateEnd - timedelta(days=7)
    totalInPeriod = orderItem.objects.filter(sku=item[0]).filter(created_at__range=[dateStart, dateEnd]).filter(order__status='holded')
    return len(totalInPeriod)

def getVMD30(item, dateMinus30, dateRangeEnd):
    totalInPeriod = orderItem.objects.filter(sku=item[0]).filter(created_at__range=[dateMinus30, dateRangeEnd])
    vmd30 = float(len(totalInPeriod) / 30.0)
    return vmd30


def getVMD(item, dateRangeInDays):
    if dateRangeInDays.days == 0.0:
        vmd = float(item[4] + item[5] + item[6] + item[7] + item[8] + item[9] / 1.0)
    else:
        vmd = float(item[4] + item[5] + item[6] + item[7] + item[8] + item[9] / float(dateRangeInDays.days))
    return vmd


def saveCSV(productList, dateStart, dateEnd):
    print('Saving CSV File')
    dateRangeInit = date(int(dateStart[0:4]), int(dateStart[5:7]), int(dateStart[8:10]))
    dateRangeEnd = date(int(dateEnd[0:4]), int(dateEnd[5:7]), int(dateEnd[8:10]))
    dateRangeInDays = dateRangeEnd - dateRangeInit
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salesReport.csv"'
    writer = csv.writer(response)
    writer.writerow(['sku', 'name', 'brand', 'price', 'qty', 'qty_holded', 'VMD', 'VMD30',
                     'qty_complete', 'qty_fraud', 'qty_fraud2', 'qty_complete2'])
    dateMinus30 = dateRangeEnd - timedelta(days=30)
    for item in productList:
        qtd_holded = getQtyHolded(item, dateRangeEnd)

        vmd = getVMD(item, dateRangeInDays)

        VMD30 = getVMD30(item, dateMinus30, dateRangeEnd)

        writer.writerow([item[0].encode('UTF-8'), item[1].encode('utf-8', 'replace'), item[2].encode('utf-8', 'replace')
                        , item[3], item[4], qtd_holded, vmd, VMD30, item[6], item[7], item[8], item[9]])
    return response

def generateCSV(orderArray, dateStart, dateEnd, itemsHash, productList):
    for order in orderArray:
        if order['status'] == 'processing':
            for item in order['items']:
                try:
                    productList[itemsHash.index(item['sku'])][4] += 1
                except:
                    pass
        elif order['status'] == 'holded':
            for item in order['items']:
                try:
                    productList[itemsHash.index(item['sku'])][5] += 1
                except:
                    pass
        elif order['status'] == 'complete':
            for item in order['items']:
                try:
                    productList[itemsHash.index(item['sku'])][6] += 1
                except:
                    pass
        elif order['status'] == 'fraud':
            for item in order['items']:
                try:
                    productList[itemsHash.index(item['sku'])][7] += 1
                except:
                    pass
        elif order['status'] == 'fraud2':
            for item in order['items']:
                try:
                    productList[itemsHash.index(item['sku'])][8] += 1
                except:
                    pass
        elif order['status'] == 'complete2':
            for item in order['items']:
                try:
                    productList[itemsHash.index(item['sku'])][9] += 1
                except:
                    pass

    return saveCSV(productList, dateStart, dateEnd)

def getBrand(item, BRANDS_ARRAY):
    itemDetail = item['name'].split('-')
    if itemDetail[-1].strip().encode('UTF-8') not in BRANDS_ARRAY and len(itemDetail) >= 2:
        #Case X-Pharma
        testString = itemDetail[-2] + '-' + itemDetail[-1]
        if testString.encode('utf-8').strip() == 'X-Pharma' or testString.encode('utf-8').strip() == 'X-pharma':
            return testString.strip()
        return itemDetail[-2].strip()
    else:
        return itemDetail[-1].strip()

def importOrdersSinceDay(request, dateStart, dateEnd):
    print('-- Start import')
    salesReport = Magento()
    salesReport.connect()
    orders = salesReport.listOrdersSinceStatusDate('holded', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('processing', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('complete', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('fraud', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('fraud2', dateStart, dateEnd) + \
            salesReport.listOrdersSinceStatusDate('complete2', dateStart, dateEnd)

    itemsHash = []
    productList = []

    BRANDS_ARRAY = []
    for brand in brands.objects.all():
        BRANDS_ARRAY.append(brand.name.encode('UTF-8'))

    for product in salesReport.getProductArray():
        itemsHash.append(product['sku'])
        if product['type'] == 'simple':
            productList.append([product['sku'], product['name'], getBrand(product, BRANDS_ARRAY), product['special_price'], 0, 0, 0, 0, 0, 0])
        else:
            productList.append([product['sku'], product['name'], getBrand(product, BRANDS_ARRAY), product['price'], 0, 0, 0, 0, 0, 0])

    for order in orders:
        saveOrderInDatabase(order)
    csvFile = generateCSV(orders, dateStart, dateEnd, itemsHash, productList)
    print('-- End import')
    return csvFile