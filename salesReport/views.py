# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order as orderNaBase, orderItem, brands, item as itemNaBase
import csv
from datetime import date, timedelta, datetime
from .models import order, orderItem, item as itemObject
from django.shortcuts import render_to_response
from django.template import RequestContext
from xlrd import open_workbook
from .correios import correios_frete_simples
from centralFitEstoque.settings import FRETE_ORIGEM

def timeInUTC(dateString):
        dateReturn = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")
        dateReturn = dateReturn + timedelta(hours=3)
        return dateReturn

def timeInGMT(dateString):
        dateReturn = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")
        dateReturn = dateReturn - timedelta(hours=3)
        return dateReturn

def saveItemInDatabse(i):
    #TODO Testar
    if not 'cost' in i:
        i['cost'] = 0

    #Certo produtos não tem special_price
    if not 'special_price' in i:
        i['special_price'] = 0

    #Certos produtos não envia o status
    if not 'status' in i:
        i['status'] = True

    newItem = itemObject.objects.create(
            product_id=i['product_id'],
            sku=i['sku'],
            name=i['name'],
            cost=i['cost'],
            price=i['price'],
            specialPrice=i['special_price'],
            status=i['status'],
            weight=i['weight'],
            )
    return newItem

def saveOrderItemInDatabase(order, orderItemToSave):
    try:
        itemToSave = itemObject.objects.get(sku=int(orderItemToSave['sku']))
    except Exception as e:
        itemToSave = saveItemInDatabse(orderItemToSave)
    createdAt = timeInGMT(orderItemToSave['created_at'])
    updated_at = timeInGMT(orderItemToSave['updated_at'])

    if orderItemToSave['parent_item_id'] != None:
        is_child = orderItemToSave['parent_item_id']
    else:
        is_child = False

    newOrderItem = orderItem.objects.create(
        item=itemToSave,
        order=order,
        quantidade=float(orderItemToSave['qty_ordered']),
        created_at=createdAt,
        updated_at=updated_at,
        price=float(orderItemToSave['price']),
        is_child=is_child,
        productType=orderItemToSave['product_type'],
    )
    return newOrderItem

def saveOrderInDatabase(o):
    print 'Saving Order: %s' % o['increment_id']
    databaseOrder = order.objects.filter(increment_id=o['increment_id'])
    if len(databaseOrder) > 0:
        print('Order in database: %s' % databaseOrder.increment_id)
        return 'NaBase'
    else:
        createdAt = timeInGMT(o['created_at'])
        updated_at = timeInGMT(o['updated_at'])
        if len(o['payment']['additional_information']) > 0:
            payment_method = o['payment']['additional_information']['PaymentMethod']
        else:
            payment_method = 'Sem Informacao'
        pesoPedido = 0
        for item in o['items']:
            pesoPedido += float(item['weight'].replace(',', '.'))
        shipping_amount_simulate = correios_frete_simples(FRETE_ORIGEM, o['billing_address']['postcode'], 30, 30, 30, pesoPedido)
        if o['shipping_method'].split('_')[2] == '41112':
            shipping_amount_centralfit = float(shipping_amount_simulate['sedex']['valor'].replace(',', '.'))
        else:
            shipping_amount_centralfit = float(shipping_amount_simulate['pac']['valor'].replace(',', '.'))
        databaseOrder = order.objects.create(
                                            increment_id=o['increment_id'],
                                            created_at= createdAt,
                                            updated_at=updated_at,
                                            is_active=True,
                                            customer_id=o['customer_id'],
                                            grand_total=o['base_grand_total'],
                                            subtotal=o['base_subtotal'],
                                            status=o['status'],
                                            customer_email=o['customer_email'],
                                            order_id=o['order_id'],
                                            shipping_amount=o['shipping_amount'],
                                            shipping_method=o['shipping_method'],
                                            discount_amount=o['discount_amount'],
                                            payment_method=payment_method,
                                            shipping_address_postcode = o['shipping_address']['postcode'],
                                            shipping_address_region = o['shipping_address']['region'],
                                            shipping_address_street = o['shipping_address']['street'],
                                            weight=o['weight'],
                                            shipping_amount_centralfit=shipping_amount_centralfit
                                            )
        for itemInOrder in o['items']:
            saveOrderItemInDatabase(databaseOrder, itemInOrder)

        return databaseOrder

def getQtyHolded(item, dateEnd):
    dateStart = dateEnd - timedelta(days=7)
    try:
        totalInPeriod = orderItem.objects.filter(item__sku=item[0]).filter(created_at__range=[dateStart, dateEnd]).filter(order__status='holded')
    except Exception as e:
        print e
        totalInPeriod = []
    return len(totalInPeriod)

def getVMD30(item, dateMinus30, dateRangeEnd):
    try:
        totalInPeriod = orderItem.objects.filter(item__sku=item[0]).filter(created_at__range=[dateMinus30, dateRangeEnd])
    except Exception as e:
        print e
        totalInPeriod = []
    vmd30 = round(float(len(totalInPeriod) / 30.0), 3)
    return vmd30


def getVMD(item, dateRangeInDays):
    if dateRangeInDays.days == 0.0:
        vmd = round(float(item[4] + item[5] + item[6] + item[7] + item[8] + item[9] / 1.0), 3)
    else:
        vmd = round(float(item[4] + item[5] + item[6] + item[7] + item[8] + item[9] / float(dateRangeInDays.days)), 3)
    return vmd


def saveCSV(productList, dateStart, dateEnd):
    print('Saving CSV File')
    dateRangeInDays = dateEnd - dateStart
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salesReport.csv"'
    writer = csv.writer(response)
    writer.writerow(['sku', 'name', 'brand', 'price', 'qty', 'qty_holded', 'VMD', 'VMD30',
                     'qty_complete', 'qty_fraud', 'qty_fraud2', 'qty_complete2', 'status'])
    dateMinus30 = dateEnd - timedelta(days=30)
    for item in productList:
        qtd_holded = getQtyHolded(item, dateEnd)

        vmd = getVMD(item, dateRangeInDays)

        VMD30 = getVMD30(item, dateMinus30, dateEnd)

        writer.writerow([item[0], item[1].encode('utf-8', 'replace'), item[2].encode('utf-8', 'replace')
                        , item[3], item[4], qtd_holded, vmd, VMD30, item[6], item[7], item[8], item[9], item[10]])
    return response

def generateCSV(orderArray, dateStart, dateEnd, itemsHash, productList):
    #Salva a quantidade de pedidos por tupo
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
        if product['status'] == '1':
            status = 'Enable'
        else:
            status = 'Disable'
        if product['special_price']:
            productList.append([product['sku'], product['name'], getBrand(product, BRANDS_ARRAY), product['special_price'], 0, 0, 0, 0, 0, 0, status])
        else:
            productList.append([product['sku'], product['name'], getBrand(product, BRANDS_ARRAY), product['price'], 0, 0, 0, 0, 0, 0, status])

    for order in orders:
        saveOrderInDatabase(order)
    csvFile = generateCSV(orders, dateStart, dateEnd, itemsHash, productList)
    print('-- End import')
    return csvFile


def exportar(request):
    if request.method == "POST":
        itemsHash = []
        productList = []
        BRANDS_ARRAY = []

        for brand in brands.objects.all():
            BRANDS_ARRAY.append(brand.name.encode('UTF-8'))

        for product in itemNaBase.objects.all():
            itemsHash.append(product.sku)
            itemDict = {
                'name': product.name
            }
            if product.status:
                status = 'Enable'
            else:
                status = 'Disable'
            if product.specialPrice:
                productList.append([product.sku, product.name, getBrand(itemDict, BRANDS_ARRAY), product.specialPrice, 0, 0, 0, 0, 0, 0, status])
            else:
                productList.append([product.sku, product.name, getBrand(itemDict, BRANDS_ARRAY), product.price, 0, 0, 0, 0, 0, 0, status])

        dataInicial = datetime.strptime(request.POST.get('dataInicio'), '%d-%m-%Y')
        dataFinal = datetime.strptime(request.POST.get('dataFim') + ' 23:59:59', '%d-%m-%Y %H:%M:%S')

        orders = orderNaBase.objects.filter(created_at__range=[dataInicial, dataFinal])

        for order in orders:
            if order.status == 'processing':
                print order.orderitem_set.all()
                for itemOrder in order.orderitem_set.all():
                    try:
                        productList[itemsHash.index(itemOrder.item.sku)][4] += 1
                    except:
                        pass
            elif order.status == 'holded':
                for itemOrder in order.orderitem_set.all():
                    try:
                        productList[itemsHash.index(itemOrder.item.sku)][5] += 1
                    except:
                        pass
            elif order.status == 'complete':
                for itemOrder in order.orderitem_set.all():
                    try:
                        productList[itemsHash.index(itemOrder.item.sku)][6] += 1
                    except:
                        pass
            elif order.status == 'fraud':
                for itemOrder in order.orderitem_set.all():
                    try:
                        productList[itemsHash.index(itemOrder.item.sku)][7] += 1
                    except:
                        pass
            elif order.status == 'fraud2':
                for itemOrder in order.orderitem_set.all():
                    try:
                        productList[itemsHash.index(itemOrder.item.sku)][8] += 1
                    except:
                        pass
            elif order.status == 'complete2':
                for itemOrder in order.orderitem_set.all():
                    try:
                        productList[itemsHash.index(itemOrder.item.sku)][9] += 1
                    except:
                        pass

        return saveCSV(productList, dataInicial, dataFinal)
    else:
        return render_to_response('exportar.html',
                              {'status': 'ok'},
                              context_instance=RequestContext(request))

def importAllProducts(request):
    if request.method == 'POST':
        print('-- Start Product import')
        salesReport = Magento()
        salesReport.connect()
        quantidadeImportada = 0
        BRANDS_ARRAY = []
        for brand in brands.objects.all():
            BRANDS_ARRAY.append(brand.name.encode('UTF-8'))
        for product in salesReport.getProductArray():
            try:
                item = item.objects.get(product['sku'])
            except Exception as e:
                saveItemInDatabse(product)
                quantidadeImportada += 1
        return render_to_response('importar.html',
                          {
                              'status': 'importacaoSucesso',
                              'quantidadeImportada': quantidadeImportada
                          },
                          context_instance=RequestContext(request))
    else:
        return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))


def importOrders(dateEndImUTC, dateStartImUTC, importado, naBase):
    salesReport = Magento()
    salesReport.connect()
    orders = salesReport.listOrdersSinceStatusDate('holded', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'),
                                                   dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
             salesReport.listOrdersSinceStatusDate('processing', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'),
                                                   dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
             salesReport.listOrdersSinceStatusDate('complete', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'),
                                                   dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
             salesReport.listOrdersSinceStatusDate('fraud', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'),
                                                   dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
             salesReport.listOrdersSinceStatusDate('fraud2', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'),
                                                   dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
             salesReport.listOrdersSinceStatusDate('complete2', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'),
                                                   dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S'))
    for order in orders:
        status = saveOrderInDatabase(order)
        if status == 'NaBase':
            naBase += 1
        else:
            importado += 1

    return importado, naBase


def importAllOrders(request):
    if request.method == 'POST':
        naBase = 0
        importado = 0
        dateStart = request.POST.get('dataInicio').split('-')
        dateEnd = request.POST.get('dataFim').split('-')
        dateStartImUTC = timeInUTC(dateStart[2] + '-' + dateStart[1] + '-' + dateStart[0] + ' 00:00:00')
        dateEndImUTC = timeInUTC(dateEnd[2] + '-' + dateEnd[1] + '-' + dateEnd[0] + ' 23:59:59')
        print('-- Start Order import')
        importado, naBase = importOrders(dateEndImUTC, dateStartImUTC, importado, naBase)

        return render_to_response('importar.html',
                          {
                              'status': 'importacaoSucesso',
                              'quantidadeImportada': importado,
                              'naBase': naBase,
                              'RangeImportado': 'de %s ate %s'% (request.POST.get('dataInicio'), request.POST.get('dataFim'))
                          },
                          context_instance=RequestContext(request))
    else:
        return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))



def importProductCost(request):
    if request.method == "POST":
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        from centralFitEstoque.settings import MEDIA_ROOT

        quantidadeAtualizada = 0

        file = request.FILES['docfile']
        path = default_storage.save('tabelaCustoProduto.xlsx', ContentFile(file.read()))
        wb = open_workbook(MEDIA_ROOT + path)
        for s in wb.sheets():
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                print
                try:
                    if values[2] != 0:
                        produto = itemNaBase.objects.get(sku=values[2])
                        print produto, produto.cost
                        produto.cost = values[4]
                        produto.save()
                        quantidadeAtualizada += 1
                except Exception as e:
                    print e

        return render_to_response('importar.html',
                              {'status': 'importacaoSucesso',
                               'atualizadoSucesso': quantidadeAtualizada
                              },
                              context_instance=RequestContext(request))
    else:
        return HttpResponseForbidden


def updateLast7daysOrderStatus():
    data_inicio = datetime.today() - timedelta(days=7)
    orders = orderNaBase.objects.filter(created_at__gt=data_inicio, status__in=['holded', 'processing'])
    quantidadeAtualizada = 0
    salesReport = Magento()
    salesReport.connect()
    #call magento and update orderStatus
    for orderToBeUpdated in orders:
        print 'trying update order %s' % orderToBeUpdated.increment_id
        new_order_info = salesReport.getSingleOrderInfo(orderToBeUpdated.increment_id)
        if new_order_info['status'] != orderToBeUpdated.status:
            print 'Order Updated %s !' % orderToBeUpdated.increment_id
            orderToBeUpdated.status = new_order_info['status']
            orderToBeUpdated.save()
            quantidadeAtualizada += 1
    return quantidadeAtualizada


def atualizarStatusPedido(request):
    quantidadeAtualizada = updateLast7daysOrderStatus()

    return render_to_response('importar.html',
                              {'status': 'atualizadoSucesso',
                               'quantidadeAtualizada': quantidadeAtualizada,
                              },
                              context_instance=RequestContext(request))