# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'akiokio'

from datetime import datetime
import sys, csv
from salesReport.models import orderItem, order

###### Create .csv file with the orders products by date ######
###### DEVELOPER VERSION ########


def getOrderPerPeriod():
    from restinmagento.oauth import OAuth
    from restinmagento.resource import Resource
    #Tokens crap
    #rim-tmptoken --url=http://127.0.0.1:8888/oauth/initiate --clientkey=m2vngld7caw6duujfwybeaw14yw1wpii --clientsecret=k9jqcq36oi65ee70nzjxbo71u6x5f87u
    #http://127.0.0.1/oauth/initiate?oauth_token=5jp0pqbfgfk052agmef6zp4mf90l58e2&oauth_verifier=mnpzepksyf0mf4qb9no90nrs6cowsmeu
    # Obtained a temporary token.
    # Temporary key: 5jp0pqbfgfk052agmef6zp4mf90l58e2
    # Temporary secret: z24yaqadmo6dv6e1dqrtvurms7w4lavh

    #rim-resourcetoken --url=http://127.0.0.1/oauth/token --clientkey=m2vngld7caw6duujfwybeaw14yw1wpii --clientsecret=k9jqcq36oi65ee70nzjxbo71u6x5f87u --tmpkey=5jp0pqbfgfk052agmef6zp4mf90l58e2 --tmpsecret=z24yaqadmo6dv6e1dqrtvurms7w4lavh --verifier=mnpzepksyf0mf4qb9no90nrs6cowsmeu

    # Obtained a resource token.
    # Resource key: wf1kk0nyfcme7oucc5pwjmiedx3e3z9l
    # Resource secret: ipqdilrnqi3xo48911q1gde3pm09hi12

    oauth = OAuth(client_key=u'm2vngld7caw6duujfwybeaw14yw1wpii',
                  client_secret=u'k9jqcq36oi65ee70nzjxbo71u6x5f87u',
                  resource_owner_key=u'wf1kk0nyfcme7oucc5pwjmiedx3e3z9l',
                  resource_owner_secret=u'ipqdilrnqi3xo48911q1gde3pm09hi12')

    # resource = Resource(u'http://127.0.0.1/api/rest/orders', oauth)
    # params = dict(limit=100, page=1)
    # response = resource.get(params=params)
    # if response.status_code == 200:
    #     products = response.json()

    # print products

    #Using Magento like ORM
    from restinmagento.backend import set_default_backend
    from restinmagento.model import Product, Order, Customer, StockItem
    from restinmagento.operators import lt_, range_, gt_


    set_default_backend(url=u'http://127.0.0.1/api/rest', oauth=oauth)

    # product = Product.objects.get(pk="139")

    #GET ALL PRODUCTS
    # all_products = Product.objects.all()
    # print all_products

    # order = Order.objects.get(pk=134)

    # GET ALL ORDERS
    all_orders_list = Order.objects.list(maxitems=1, buffer=100)
    # all_orders_list = Order.objects.filter(gt_('created_at', u'2012-11-14 19:03:15'))
    #Sold Itens Array
    soldItemList = []
    #Order parser
    for order in all_orders_list:
        created_at = datetime.strptime(order['created_at'], '%Y-%m-%d %H:%M:%S')
        if order['status'] and order['status'] == 'processing':
            for orderItem in order['order_items']:
                soldItemList.append([orderItem['sku'], orderItem['name']])

    print soldItemList.__len__()

    return soldItemList

def getOrders(client, session, filters):
    #Main Logic
    orderArray = []
    print 'Retrieve Order - Status: Starting at %s' % datetime.now()
    orderList = client.service.salesOrderList(session, filters=filters)
    for order in orderList:
        orderArray.append(order.increment_id)
    print 'Retrieve Order - Status: End at %s' % datetime.now()

    #Return array with orderId
    return orderArray


def getOrderInfo(client, session, orderId):
    return client.service.salesOrderInfo(session, orderId)


def generateSalesReport():
    #import Libraries
    import suds
    import csv
    from suds.client import Client

    #Report
    salesReport = {}
    itemsHash = []

    #Main logic
    wsdl_file = 'http://127.0.0.1/api/v2_soap?wsdl=1'
    user = 'akiokio'
    password = 'aKiO2102'
    client = Client(wsdl_file) #load the wsdl file
    print 'Trying login....'
    session = client.service.login(user, password) #login and create a session
    print 'New Session: %s' % session
    filters = {'filter': [{'key': 'status',
                           'value': ['pending', 'holded']}, {
                            'key': 'created_at',
                            'value': '2013-11-04'
                         }]
    }
    filter = [{"created_at": {"gt":'2001-11-25 12:12:07'}, "status": {"eq": ['pending', 'holded']}}]

    orderArray = getOrders(client, session, filter)
    print 'Total Orders Recovered: %s' % orderArray.__len__()
    for orderId in orderArray:
        print 'Getting Order Details: %s' % orderId
        order = getOrderInfo(client, session, orderId)
        if order.status == 'pending':
            for item in order.items:
                if item.sku not in itemsHash:
                    salesReport[item.sku] = {'sku': item.sku,
                                             'name': item.name,
                                             'qty': 1,
                                             'qty_holded': 0,
                    }
                    itemsHash.append(item.sku)
                else:
                    salesReport[item.sku]['qty'] += 1
        elif order.status == 'holded':
            for item in order.items:
                if item.sku not in itemsHash:
                    salesReport[item.sku] = {'sku': item.sku,
                                             'name': item.name,
                                             'qty': 0,
                                             'qty_holded': 1,
                    }
                    itemsHash.append(item.sku)
                else:
                    salesReport[item.sku]['qty_holded'] += 1

    #Save csv file
    with open('salesReport.csv', 'wb') as file:
        spamwriter = csv.writer(file, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in salesReport:
            spamwriter.writerow([salesReport[item]['sku'], salesReport[item]['name'].encode('utf-8', 'replace')
                , salesReport[item]['qty']])

    return salesReport