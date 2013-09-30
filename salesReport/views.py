# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
import csv, math
from datetime import date, timedelta, datetime
from .models import order as orderNaBase, orderItem, brands,  item as itemObject, status_history, csvReport as reportFile
from django.shortcuts import render_to_response
from django.template import RequestContext
from xlrd import open_workbook
from .correios import correios_frete_simples
from centralFitEstoque.settings import FRETE_ORIGEM
from django.core.serializers import serialize
from django.utils import simplejson
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db import transaction

def timeInUTC(dateString):
        dateReturn = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        dateReturn = dateReturn + timedelta(hours=3)
        return dateReturn

def timeInGMT(dateString):
        dateReturn = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")
        dateReturn = dateReturn - timedelta(hours=3)
        return dateReturn

def saveItemInDatabse(i):
    if not 'cost' in i:
        i['cost'] = 0

    #Certo produtos não tem special_price
    if not 'special_price' in i:
        i['special_price'] = 0

    #Certos produtos não envia o status
    if not 'status' in i:
        i['status'] = True
    #Alguns produtos não tem weight
    if not 'weight' in i:
        i['weight'] = 0

    if i['status'] == '1':
        i['status'] = True
    else:
        i['status'] = False

    if 'marca' in i and i['marca'] != None:
        try:
            marca = brands.objects.get(name=i['marca'])
        except Exception as e:
            marca = brands.objects.create(name=i['marca'], meta_dias_estoque=1)
    else:
        marca = None

    dateInit = datetime.today().replace(hour=0, minute=0, second=0) - timedelta(hours=3)
    dateEnd = datetime.today().replace(hour=23, minute=59, second=59) - timedelta(days=30) - timedelta(hours=3)
    vmd = getVMD30(i, dateEnd, dateInit)

    if 'special_price' in i and i['special_price'] != None:
        valor_produto = i['special_price']
    else:
        valor_produto = i['price']

    valor_faturado_do_dia = vmd * float(valor_produto)

    try:
        newItem = itemObject.objects.filter(product_id=i['product_id'])
        if len(newItem) == 0:
            newItem = itemObject.objects.create(
                    product_id=i['product_id'],
                    sku=i['sku'],
                    name=i['name'],
                    cost=i['cost'],
                    price=i['price'],
                    specialPrice=i['special_price'],
                    status=i['status'],
                    weight=i['weight'],
                    cmm=i['cost'],
                    estoque_atual=0,
                    estoque_empenhado=0,
                    estoque_disponivel=0,
                    margem=0,
                    brand=marca,
                    vmd=vmd,
                    valor_faturado_do_dia=valor_faturado_do_dia,
                    )
            return newItem
        else:
            return newItem[0]

    except Exception as e:
        print e


def saveOrderStatusHistory(iteration, order):
    if not iteration['status']:
        iteration['status'] = 'None'
    return status_history.objects.create(
        comment=iteration['comment'],
        status=iteration['status'],
        entity_name=iteration['entity_name'],
        created_at=datetime.strptime(iteration['created_at'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
        order=order,
    )



def saveOrderItemInDatabase(order, orderItemToSave):
    try:
        itemToSave = itemObject.objects.get(sku=int(orderItemToSave['sku']))
    except Exception as e:
        itemToSave = saveItemInDatabse(orderItemToSave)

    if orderItemToSave['parent_item_id'] != None:
        is_child = orderItemToSave['parent_item_id']
    else:
        is_child = False

    newOrderItem = orderItem.objects.create(
        item=itemToSave,
        order=order,
        quantidade=float(orderItemToSave['qty_ordered']),
        created_at=datetime.strptime(orderItemToSave['created_at'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
        updated_at=datetime.strptime(orderItemToSave['updated_at'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
        price=float(orderItemToSave['price']),
        is_child=is_child,
        productType=orderItemToSave['product_type'],
    )

    #Fix se estiver none os campos
    if not itemToSave.estoque_disponivel:
        itemToSave.estoque_disponivel = 0
    if not itemToSave.estoque_empenhado:
        itemToSave.estoque_empenhado = 0
    if not itemToSave.estoque_atual:
        itemToSave.estoque_atual = 0

    if order.status == 'holded':
        itemToSave.estoque_empenhado += 1
    elif order.status == 'processing' or order.status == 'complete' or order.status == 'complete2':
        itemToSave.estoque_atual -= 1

    itemToSave.estoque_disponivel = itemToSave.estoque_atual - itemToSave.estoque_empenhado

    if itemToSave.brand:
        fator_quantidade = (itemToSave.vmd * itemToSave.brand.meta_dias_estoque) - itemToSave.estoque_disponivel
        if (fator_quantidade) >= 0:
            itemToSave.quantidade_excedente = math.ceil(fator_quantidade)
            itemToSave.quantidade_faltante = 0
        else:
            itemToSave.quantidade_faltante = math.ceil(fator_quantidade)
            itemToSave.quantidade_excedente = 0

    #Update the vmd
    dateInit = datetime.today().replace(hour=0, minute=0, second=0) - timedelta(hours=3)
    dateEnd = datetime.today().replace(hour=23, minute=59, second=59) - timedelta(days=30) - timedelta(hours=3)
    itemToSave.vmd = getVMD30ForDatabaseItem(itemToSave, dateEnd, dateInit)

    #Update the valor_faturado_do_dia
    preco_item = itemToSave.specialPrice if itemToSave.specialPrice else itemToSave.price
    itemToSave.valor_faturado_do_dia = itemToSave.vmd * float(preco_item)

    itemToSave.save()
    return newOrderItem

@transaction.commit_on_success
def saveOrderInDatabase(o):
    print 'Saving Order: %s' % o['increment_id']
    databaseOrder = orderNaBase.objects.filter(increment_id=o['increment_id'])
    if len(databaseOrder) > 0:
        print('Order in database: %s' % databaseOrder[0].increment_id)
        return databaseOrder[0]
    else:
        if len(o['payment']['additional_information']) > 0:
            payment_method = o['payment']['additional_information']['PaymentMethod']
        else:
            payment_method = 'Sem Informacao'
        pesoPedido = 0
        for item in o['items']:
            pesoPedido += float(item['weight'].replace(',', '.'))
        shipping_amount_simulate = correios_frete_simples(FRETE_ORIGEM, o['billing_address']['postcode'], 30, 30, 30, pesoPedido)
        if o['shipping_method']:
            if o['shipping_method'].split('_')[2] == '41112':
                shipping_amount_centralfit = float(shipping_amount_simulate['sedex']['valor'].replace(',', '.'))
            else:
                shipping_amount_centralfit = float(shipping_amount_simulate['pac']['valor'].replace(',', '.'))
        else:
            shipping_amount_centralfit = 10
            o['shipping_method'] = 'Envio Especial'

        if float(o['grand_total']) == 0.0:
            o['grand_total'] = o['subtotal']
            o['base_grand_total'] = o['subtotal']

        databaseOrder = orderNaBase(
                                            increment_id=o['increment_id'],
                                            created_at= datetime.strptime(o['created_at'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
                                            updated_at=datetime.strptime(o['updated_at'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
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

        #Salvar o historico de iteracoes do pedido
        for iteration in o['status_history']:
            saveOrderStatusHistory(iteration, databaseOrder)
        databaseOrder.save()

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
        totalInPeriod = orderItem.objects.filter(item__sku=item[0]).filter(created_at__range=[dateMinus30, dateRangeEnd]).exclude(order__status='canceled').exclude(order__status='holded')
    except Exception as e:
        print e
        totalInPeriod = []
    vmd30 = round(float(len(totalInPeriod) / 30.0), 3)
    return vmd30

def getVMD30ForDatabaseItem(item, dateMinus30, dateRangeEnd):
    try:
        totalInPeriod = orderItem.objects.filter(item__sku=item.sku).filter(created_at__range=[dateMinus30, dateRangeEnd]).exclude(order__status='canceled').exclude(order__status='holded')
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

def getBrand(item):
    BRANDS_ARRAY = []
    for brand in brands.objects.all():
        BRANDS_ARRAY.append(brand.name.encode('UTF-8'))
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
            productList.append([product['sku'], product['name'], getBrand(product), product['special_price'], 0, 0, 0, 0, 0, 0, status])
        else:
            productList.append([product['sku'], product['name'], getBrand(product), product['price'], 0, 0, 0, 0, 0, 0, status])

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

        for product in itemObject.objects.all():
            itemsHash.append(product.sku)
            itemDict = {
                'name': product.name
            }
            if product.status:
                status = 'Enable'
            else:
                status = 'Disable'
            if product.specialPrice:
                productList.append([product.sku, product.name, getBrand(itemDict), product.specialPrice, 0, 0, 0, 0, 0, 0, status])
            else:
                productList.append([product.sku, product.name, getBrand(itemDict), product.price, 0, 0, 0, 0, 0, 0, status])

        dataInicial = datetime.strptime(request.POST.get('dataInicio'), '%d-%m-%Y')
        dataFinal = datetime.strptime(request.POST.get('dataFim') + ' 23:59:59', '%d-%m-%Y %H:%M:%S')

        orders = orderNaBase.objects.filter(created_at__range=[dataInicial, dataFinal])

        for order in orders:
            if order.status == 'processing':
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
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def importAllProducts(request):
    if request.method == 'POST':
        updateItemDetail()
        print('-- Start Product import')
        salesReport = Magento()
        salesReport.connect()
        quantidadeImportada = 0
        BRANDS_ARRAY = []
        for brand in brands.objects.all():
            BRANDS_ARRAY.append(brand.name.encode('UTF-8'))
        for product in salesReport.getProductArray():
            if RepresentsInt(product['sku']):
                exist = itemObject.objects.filter(sku=product['sku'])
                if len(exist) == 0:
                    saveItemInDatabse(product)
                    quantidadeImportada += 1
        return render_to_response('importar.html',
                          {
                              'status': '',
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
        wb = open_workbook(MEDIA_ROOT + '/' + path)
        for s in wb.sheets():
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                try:
                    if values[2] != 0:
                        produto = itemObject.objects.get(sku=values[2])
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
        print u'trying update order %s' % orderToBeUpdated.increment_id
        new_order_info = salesReport.getSingleOrderInfo(orderToBeUpdated.increment_id)
        if new_order_info['status'] != orderToBeUpdated.status:
            print 'Order Updated %s !' % orderToBeUpdated.increment_id

            #Atualiza o estoque
            #Caso 2: De pedido holded -> canceled subtrai um no estoque compremetido
            if orderToBeUpdated.status ==  'holded' and new_order_info['status'] == 'canceled':
                for item in orderToBeUpdated.orderitem_set.all():
                    item.item.estoque_empenhado -= item.quantidade
                    item.item.estoque_disponivel = item.item.estoque_atual - item.item.estoque_empenhado
                    item.item.save()

            #Caso 1: De pedido processing -> canceled soma um no estoque disponivel
            if orderToBeUpdated.status ==  'processing' and new_order_info['status'] == 'canceled':
                for item in orderToBeUpdated.orderitem_set.all():
                    item.item.estoque_atual += item.quantidade
                    item.item.estoque_disponivel = item.item.estoque_atual - item.item.estoque_empenhado
                    item.item.save()


            orderToBeUpdated.status = new_order_info['status']
            orderToBeUpdated.updated_at = datetime.strptime(new_order_info['updated_at'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

            #salva novas iteracoes no histórico
            for iteraction in new_order_info['status_history']:
                ja_existe = False
                for orderIteraction in orderToBeUpdated.status_history_set.all():
                    if orderIteraction.created_at.strftime("%Y-%m-%d %H:%M:%S") == iteraction['created_at'] and orderIteraction.comment == iteraction['comment']:
                        ja_existe = True
                if not ja_existe:
                    databaseIteration = saveOrderStatusHistory(iteraction, orderToBeUpdated)
                    print u'Nova iteracao adicionada: %s - %s' % (databaseIteration.created_at, databaseIteration.status)

            orderToBeUpdated.save()
            quantidadeAtualizada += 1
    return quantidadeAtualizada


def extractOrderInfoFromMagento(order_id):
    salesReport = Magento()
    salesReport.connect()
    return salesReport.getSingleOrderInfo(order_id)


def SingleOrderInfo(request, order_id):
    orderJson = extractOrderInfoFromMagento(order_id)
    return HttpResponse(simplejson.dumps(orderJson))


def atualizarStatusPedido(request):
    quantidadeAtualizada = updateLast7daysOrderStatus()

    return render_to_response('importar.html',
                              {'status': 'atualizadoSucesso',
                               'quantidadeAtualizada': quantidadeAtualizada,
                              },
                              context_instance=RequestContext(request))

def generateCsvFileCron(dataInicial, dataFinal):
    itemsHash = []
    productList = []

    for product in itemObject.objects.all():
        itemsHash.append(product.sku)

        if not product.brand:
            marca = u'Não associou a marca'
        else:
            marca = product.brand.name


        if product.status:
            status = 'Enable'
        else:
            status = 'Disable'

        if product.specialPrice:
            price = product.specialPrice

        else:
            price = product.price

        productList.append([product.sku, product.name, marca, price, 0, 0, 0, 0, 0, 0, status])

    orders = orderNaBase.objects.filter(created_at__range=[dataInicial, dataFinal])

    for order in orders:
        if order.status == 'processing':
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

    print('Saving CSV File')
    dateRangeInDays = dataFinal - dataInicial
    with open('centralFitEstoque/media/csv_report/report_' + dataInicial.strftime('%m%d') + '_' + dataFinal.strftime('%m%d') + '.csv', 'wb+') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['sku', 'name', 'brand', 'price', 'qty', 'qty_holded', 'VMD', 'VMD30',
                         'qty_complete', 'qty_fraud', 'qty_fraud2', 'qty_complete2', 'status'])
        dateMinus30 = dataFinal - timedelta(days=30)
        for item in productList:
            qtd_holded = getQtyHolded(item, dataFinal)

            vmd = getVMD(item, dateRangeInDays)

            VMD30 = getVMD30(item, dateMinus30, dataFinal)

            writer.writerow([item[0], item[1].encode('utf-8', 'replace'), item[2].encode('utf-8', 'replace')
                            , item[3], item[4], qtd_holded, vmd, VMD30, item[6], item[7], item[8], item[9], item[10]])

        from django.core.files import File
        djangoFile = File(csvfile)
        csvReport = reportFile(csvFile=djangoFile, created_at=datetime.now())
        csvReport.save()

    return csvReport.csvFile.url

def generateCsvFileCronTeste(request):
    dateInit = datetime.today().replace(hour=0, minute=0, second=0) - timedelta(days=1)
    dateEnd = datetime.today().replace(hour=23, minute=59, second=59) - timedelta(days=1)

    dateInitInUtc = timeInUTC('%s-%s-%s 00:00:00' % (dateInit.year, dateInit.month, dateInit.day))
    dateEndInUtc = timeInUTC('%s-%s-%s 23:59:59' % (dateEnd.year, dateEnd.month, dateEnd.day))

    url_sales_report = generateCsvFileCron(dateInitInUtc, dateEndInUtc)

    return HttpResponse(simplejson.dumps({'status': 'success', 'url': url_sales_report}))

def update_brand(request):
    salesReport = Magento()
    salesReport.connect()
    quantidadeImportada = 0
    for product in salesReport.getProductArray():
        if RepresentsInt(product['sku']):
            exist = itemObject.objects.filter(sku=product['sku'])
            if len(exist) == 0:
                saveItemInDatabse(product)
                quantidadeImportada += 1

    return redirect(reverse('importar'))

def removeOldHoldedOrdersFrom(rangeInicio, rangeFim):
    #tem que fazer uma rotina para tirar do estoque empenhado tb de 8 dias
    data_fim = datetime.today() - timedelta(days=rangeFim)
    data_inicio = datetime.today() - timedelta(days=rangeInicio)
    pedidos_alterados =  0
    orders = orderNaBase.objects.filter(created_at__range=[data_inicio, data_fim], status='holded')
    for order in orders:
        for item in order.orderitem_set.all():
            if not item.removido_estoque:
                item.item.estoque_empenhado -= item.quantidade
                item.item.estoque_atual += item.quantidade
                item.item.estoque_disponivel += item.quantidade
                item.save()
                pedidos_alterados += 1

    return pedidos_alterados


def updateItemDetail():
    #Atualizar diariamente os precos e o status dos produtos
    salesReport = Magento()
    salesReport.connect()
    quantidade_atualizada = 0
    for product in salesReport.getProductArray():
        atualizado = False
        if RepresentsInt(product['sku']):
            item = itemObject.objects.filter(product_id=product['product_id'])
            if len(item) > 0:
                item = item[0]
                if item.price != float(product['price']):
                    item.price = float(product['price'])
                    atualizado = True
                if 'special_price' in product and product['special_price'] and item.specialPrice != float(product['special_price']):
                    item.specialPrice = float(product['special_price'])
                    atualizado = True
                if atualizado:
                    item.save()
                    quantidade_atualizada += 1
            else:
                saveItemInDatabse(product)

    return quantidade_atualizada

def updateVMDCron():
    dateInit = datetime.today().replace(hour=0, minute=0, second=0) - timedelta(hours=3)
    dateEnd = datetime.today().replace(hour=23, minute=59, second=59) - timedelta(days=30) - timedelta(hours=3)

    for item in itemObject.objects.all():
        item.vmd = getVMD30ForDatabaseItem(item, dateEnd, dateInit)
        item.save()

def updateVlrFaturadoDiaCron():

    for item in itemObject.objects.all():
        valor_produto = item.specialPrice if item.specialPrice else item.price
        item.valor_faturado_do_dia = item.vmd * valor_produto
        item.save()