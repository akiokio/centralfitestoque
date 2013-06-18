# -*- coding: utf-8 -*-
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.pymagento import Magento
from salesReport.models import order, orderItem, brands
import csv
from datetime import date, timedelta, datetime
from .models import order, orderItem, item as itemObject
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DetailView, DeleteView
from datetime import datetime, timedelta
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.timezone import utc, make_aware, localtime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        dateRange = date.today() - timedelta(days=30)
        pedidoArray = [
            ['D-00', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-01', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-02', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-03', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-04', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-05', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-06', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-07', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-08', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-09', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-10', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-11', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-12', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-13', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-14', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-15', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-16', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-17', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-18', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-19', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-20', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-21', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-22', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-23', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-24', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-25', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-26', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-27', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-28', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-29', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-30', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['D-31', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['TOTAL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        for orderInPeriod in order.objects.filter(created_at__gt=dateRange):
            diferencaDias = date.today() - orderInPeriod.created_at.date()
            hora = orderInPeriod.created_at.hour

            pedidoArray[diferencaDias.days][hora + 1] += 1
            pedidoArray[diferencaDias.days][25] += 1
            pedidoArray[32][hora + 1] += 1
            pedidoArray[32][25] += 1
        context['tabelaPedidos'] = pedidoArray
        context['usuario'] = self.request.user
        return context

def saveItemInDatabse(i):
    #TODO Testar
    if 'cost' in i:
        cost = i['cost']
    else:
        cost = 0
    try:
        newItem = itemObject.objects.create(
                product_id=i['product_id'],
                sku=i['sku'],
                name=i['name'],
                cost=cost,
                price=i['price'],
                )
    except Exception as e:
        newItem = None
    return newItem

def saveOrderItemInDatabse(order, orderItemToSave):
    try:
        itemToSave = itemObject.objects.get(sku=int(orderItemToSave['sku']))
    except Exception as e:
        itemToSave = saveItemInDatabse(orderItemToSave)
    newOrderItem = orderItem.objects.create(
        item=itemToSave,
        order=order,
        quantidade=float(orderItemToSave['qty_ordered']),
        created_at=orderItemToSave['created_at'],
        updated_at=orderItemToSave['updated_at'],
    )
    return newOrderItem

def saveOrderInDatabase(o):
    print 'Saving Order: %s' % o['increment_id']
    try:
        databaseOrder = order.objects.get(increment_id=o['increment_id'])
        print('Order in database: %s' % databaseOrder.increment_id)
        return 'NaBase'
    except:
        createdAt = datetime.strptime(o['created_at'], '%Y-%m-%d %H:%M:%S')
        createdAt = make_aware(createdAt, utc)
        updated_at = datetime.strptime(o['updated_at'], '%Y-%m-%d %H:%M:%S')
        updated_at = make_aware(updated_at, utc)
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
                                            order_id=o['order_id'])
        for itemInOrder in o['items']:
            saveOrderItemInDatabse(databaseOrder, itemInOrder)

        return 'Importado'

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
                     'qty_complete', 'qty_fraud', 'qty_fraud2', 'qty_complete2', 'status'])
    dateMinus30 = dateRangeEnd - timedelta(days=30)
    for item in productList:
        qtd_holded = getQtyHolded(item, dateRangeEnd)

        vmd = getVMD(item, dateRangeInDays)

        VMD30 = getVMD30(item, dateMinus30, dateRangeEnd)

        writer.writerow([item[0].encode('UTF-8'), item[1].encode('utf-8', 'replace'), item[2].encode('utf-8', 'replace')
                        , item[3], item[4], qtd_holded, vmd, VMD30, item[6], item[7], item[8], item[9], item[10]])
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

def importAllProducts(request):
    if request.method == 'POST':
        print('-- Start Product import')
        salesReport = Magento()
        salesReport.connect()
        quantidadeImportada = 0
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

def importAllOrders(request):
    if request.method == 'POST':
        naBase = 0
        importado = 0
        dateStart = request.POST.get('dataInicio').split('-')
        dateEnd = request.POST.get('dataFim').split('-')
        print('-- Start Order import')
        salesReport = Magento()
        salesReport.connect()
        formatedDateInit = dateStart[2] + '-' + dateStart[1]  + '-' +  dateStart[0]
        formatedDateEnd = dateEnd[2] + '-' + dateEnd[1]  + '-' +  dateEnd[0]

        orders = salesReport.listOrdersSinceStatusDate('holded', formatedDateInit, formatedDateEnd) + \
                salesReport.listOrdersSinceStatusDate('processing', formatedDateInit, formatedDateEnd) + \
                salesReport.listOrdersSinceStatusDate('complete', formatedDateInit, formatedDateEnd) + \
                salesReport.listOrdersSinceStatusDate('fraud', formatedDateInit, formatedDateEnd) + \
                salesReport.listOrdersSinceStatusDate('fraud2', formatedDateInit, formatedDateEnd) + \
                salesReport.listOrdersSinceStatusDate('complete2', formatedDateInit, formatedDateEnd)

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