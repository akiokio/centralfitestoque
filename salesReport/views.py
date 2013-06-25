# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order as orderNaBase, orderItem, brands, item as itemNaBase
import csv
from datetime import date, timedelta, datetime
from .models import order, orderItem, item as itemObject
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DetailView, DeleteView
from datetime import datetime, timedelta
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.timezone import utc, make_aware, localtime, get_current_timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        dateRange = datetime.today() - timedelta(days=30)
        #Cria a tabela da dashboard limpa
        pedidoArray = []
        today = date.today()
        for day in range(0, 32):
            pedidoArray.append([
                str(today.day) + '-' + str(today.month), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ])
            today -= timedelta(days=1)
        pedidoArray.append(['TOTAL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        #Preenche a tabela com os pedidos
        for orderInPeriod in order.objects.filter(created_at__gt=dateRange):
            diferencaDias = date.today() - orderInPeriod.created_at.date()

            #Soma a coluna de dias
            pedidoArray[diferencaDias.days][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[diferencaDias.days][25] += 1
            #Soma a coluna Totais
            pedidoArray[32][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[32][25] += 1
        context['tabelaPedidos'] = pedidoArray
        context['usuario'] = self.request.user
        return context

def timeInUTC(dateString):
        dateReturn = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")
        print dateReturn
        dateReturn = dateReturn + timedelta(hours=3)
        print dateReturn
        return dateReturn

def timeInGMT(dateString):
        dateReturn = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S")
        print dateReturn
        dateReturn = dateReturn - timedelta(hours=3)
        print dateReturn
        return dateReturn

def saveItemInDatabse(i, BRANDS_ARRAY):
    #TODO Testar
    if i['cost']:
        cost = i['cost']
    else:
        cost = 0
    if i['special_price']:
        precoEspecial = i['special_price']
    else:
        precoEspecial = 0

    try:
        newItem = itemObject.objects.create(
                product_id=i['product_id'],
                sku=i['sku'],
                name=i['name'],
                cost=cost,
                price=i['price'],
                specialPrice=precoEspecial,
                status=i['status'],
                # weight=i['weight'] TODO
                )
    except Exception as e:
        print e
        newItem = None
    return newItem

def saveOrderItemInDatabse(order, orderItemToSave):
    try:
        itemToSave = itemObject.objects.get(sku=int(orderItemToSave['sku']))
    except Exception as e:
        itemToSave = saveItemInDatabse(orderItemToSave)
    createdAt = timeInGMT(orderItemToSave['created_at'])
    updated_at = timeInGMT(orderItemToSave['updated_at'])

    newOrderItem = orderItem.objects.create(
        item=itemToSave,
        order=order,
        quantidade=float(orderItemToSave['qty_ordered']),
        created_at=createdAt,
        updated_at=updated_at,
        price=float(orderItemToSave['price'],
    ))
    return newOrderItem

def saveOrderInDatabase(o):
    print 'Saving Order: %s' % o['increment_id']
    try:
        databaseOrder = order.objects.get(increment_id=o['increment_id'])
        print('Order in database: %s' % databaseOrder.increment_id)
        return 'NaBase'
    except:
        createdAt = timeInGMT(o['created_at'])
        updated_at = timeInGMT(o['updated_at'])
        if len(o['payment']['additional_information']) > 0:
            payment_method = o['payment']['additional_information']['PaymentMethod']
        else:
            payment_method = 'Sem Informacao'
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
                                            payment_method=payment_method
                                            )
        for itemInOrder in o['items']:
            saveOrderItemInDatabse(databaseOrder, itemInOrder)

        return 'Importado'

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

def importar(request):
    return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))

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
                saveItemInDatabse(product, BRANDS_ARRAY)
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

def importAllOrders(request):
    if request.method == 'POST':
        naBase = 0
        importado = 0
        dateStart = request.POST.get('dataInicio').split('-')
        dateEnd = request.POST.get('dataFim').split('-')
        dateStartImUTC = timeInUTC(dateStart[2] + '-' + dateStart[1] + '-' + dateStart[0] + ' 00:00:00')
        dateEndImUTC = timeInUTC(dateEnd[2] + '-' + dateEnd[1] + '-' + dateEnd[0] + ' 23:59:59')
        print('-- Start Order import')
        salesReport = Magento()
        salesReport.connect()

        orders = salesReport.listOrdersSinceStatusDate('holded', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'), dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
                salesReport.listOrdersSinceStatusDate('processing', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'), dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
                salesReport.listOrdersSinceStatusDate('complete', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'), dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
                salesReport.listOrdersSinceStatusDate('fraud', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'), dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
                salesReport.listOrdersSinceStatusDate('fraud2', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'), dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S')) + \
                salesReport.listOrdersSinceStatusDate('complete2', dateStartImUTC.strftime('%Y-%m-%d %H:%M:%s'), dateEndImUTC.strftime('%Y-%m-%d %H:%M:%S'))

        for order in orders:
            status = saveOrderInDatabase(order)
            if status == 'Importado':
                importado += 1
            else:
                naBase += 1

        return render_to_response('importar.html',
                          {
                              'status': 'importacaoSucesso',
                              'quantidadeImportada': importado,
                              'naBase': naBase
                          },
                          context_instance=RequestContext(request))
    else:
        return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('home'))
            else:
                pass
                # Return a 'disabled account' error message
        else:
            pass
            # Return an 'invalid login' error message.
    else:
        return render_to_response('registration/login.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def getFaturamentoForDay(date):
    inicioDoDia = date.replace(hour=0, minute=0, second=0)
    fimDoDia = date.replace(hour=23, minute=59, second=59)
    orders = orderNaBase.objects.filter(created_at__range=[inicioDoDia, fimDoDia])
    today = str(date.day) + '-' + str(date.month),
    numeroDePedidos = len(orders)
    valorBrutoFaturado = 0
    receitaFrete = 0
    valorDesconto = 0
    valorBonificado = 0
    valorLiquidoProdutos = 0
    # ALTERARRR!!!!!
    custoProdutos = 1
    # ALTERARRR!!!!!
    valorFrete = 1
    # ALTERARRR!!!!!
    valorTaxaCartao = 0
    somatoriaProdutos = 0

    for order in orders:
        valorBrutoFaturado += order.grand_total
        receitaFrete += order.shipping_amount
        valorDesconto += order.discount_amount

        valorBonificadoPedido = 0
        for item in order.orderitem_set.all():
            somatoriaProdutos += 1
            custoProdutos += item.item.cost
            if item.price == 0.0:
                valorBonificado += item.item.price
                valorBonificadoPedido += item.item.price

        valorLiquidoProdutos += order.grand_total - order.shipping_amount - order.discount_amount - valorBonificadoPedido
        valorFrete += order.shipping_amount

        if order.payment_method == 'BoletoBancario':
            valorTaxaCartao += 3.5
        else:
            valorTaxaCartao += 1.8

    margemBrutaSoProdutos = 1 - (custoProdutos / valorLiquidoProdutos)
    margemBrutaCartaoFrete = 1 - ((custoProdutos + valorFrete + valorTaxaCartao) / (valorLiquidoProdutos + receitaFrete))
    ticketMedio = valorLiquidoProdutos / numeroDePedidos
    nuemroPedidosProdutos = somatoriaProdutos / numeroDePedidos

    print today[0]
    return [
        today[0],
        numeroDePedidos,
        round(valorBrutoFaturado, 2),
        round(receitaFrete, 2),
        round(valorDesconto, 2),
        round(valorBonificado, 2),
        round(valorLiquidoProdutos, 2),
        round(custoProdutos, 2),
        round(valorFrete, 2),
        round(valorTaxaCartao, 2),
        round(margemBrutaSoProdutos, 2),
        round(margemBrutaCartaoFrete, 2),
        round(ticketMedio, 2),
        nuemroPedidosProdutos
    ]
    # return {
    #     'dia': today,
    #     'numeroDePedidos': numeroDePedidos,
    #     'valorBrutoFaturado': valorBrutoFaturado,
    #     'receitaFrete': receitaFrete,
    #     'valorDesconto': valorDesconto,
    #     'valorBonificado': valorBonificado,
    #     'valorLiquidoProdutos': valorLiquidoProdutos,
    #     'custoProdutos': custoProdutos,
    #     'valorFrete': valorFrete,
    #     'valorTaxaCartao': valorTaxaCartao,
    #     'somatoriaProdutos': somatoriaProdutos,
    #     'margemBrutaSoProdutos': margemBrutaSoProdutos,
    #     'margemBrutaCartaoFrete': margemBrutaCartaoFrete,
    #     'ticketMedio': ticketMedio,
    #     'nuemroPedidosProdutos': nuemroPedidosProdutos,
    # }

class Faturamento(TemplateView):
    template_name = 'faturamento.html'

    def get_context_data(self, **kwargs):
        context = super(Faturamento, self).get_context_data(**kwargs)
        #Cria a tabela da dashboard limpa
        tabela = []
        today = datetime.now()
        for day in range(0, 7):
            tabela.append(getFaturamentoForDay(today))
            today -= timedelta(days=1)
        tabela.append(['TOTAL'])

        print tabela

        context['tabelaFaturamento'] = tabela
        return context