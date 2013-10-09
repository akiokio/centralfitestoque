# -*- coding: utf-8 -*-
__author__ = 'akiokio'
import cronjobs
from django_cron import CronJobBase, Schedule
import datetime
from django.core.mail import send_mail
from centralFitEstoque.settings import LISTA_REMETENTES_EMAIL
from salesReport.views import timeInGMT, timeInUTC, updateLast7daysOrderStatus, importOrders, generateCsvFileCron,\
    removeOldHoldedOrdersFrom, updateItemDetail, getVMD30ForDatabaseItem, updateVMDCron, updateVlrFaturadoDiaCron,\
    updateABCValues
from salesReport.models import item as product

@cronjobs.register
def periodic_task():
    inicioJob = datetime.datetime.now()

    dateInit = datetime.datetime.today().replace(hour=0, minute=0, second=0) - datetime.timedelta(days=1) - datetime.timedelta(hours=3)
    dateEnd = datetime.datetime.today().replace(hour=23, minute=59, second=59) - datetime.timedelta(days=1) - datetime.timedelta(hours=3)

    #Import yesterday orders
    naBase = 0
    importado = 0

    dateInitInUtc = timeInUTC('%s-%s-%s 00:00:00' % (dateInit.year, dateInit.month, dateInit.day))
    dateEndInUtc = timeInUTC('%s-%s-%s 23:59:59' % (dateEnd.year, dateEnd.month, dateEnd.day))

    importado, naBase = importOrders(dateEndInUtc, dateInitInUtc, importado, naBase)

    #Update Last 7 days order status
    atualizado = updateLast7daysOrderStatus()
    #Remove Old itens from reserved stock
    pedidos_com_itens_liberados = removeOldHoldedOrdersFrom(30, 8)
    #Atualiza os precos dos produtos se necessario
    print('calling updateItemDetail')
    qtd_produtos_com_precos_atualizados = updateItemDetail()
    #Atualiza o VMD de todos os itens
    updateVMDCron()
    #Atualiza o VMD de todos os itens
    updateVlrFaturadoDiaCron()
    #Update ABC values
    print 'Updating ABC'
    updateABCValues()

    #Save fisic archive
    url_relatorio = generateCsvFileCron(dateInitInUtc, dateEndInUtc)

    fimJob = datetime.datetime.now()
    #Jobs is done, tell everyone
    msgString = u'''
                Range Inicio: %s,
                Range Fim: %s,
                Pedidos importados: %s,
                Pedidos na base: %s,
                Pedidos com status atualizados: %s,
                iniciado as: %s, finalizado as: %s,
                url_relatorio: http://hom.centralfit.com.br:8080%s,
                Pedidos com itens liberados do estoque: %s,
                Quantidade de produtos com preços atualizados: %s
                ''' % \
                (dateInit,
                 dateEnd,
                 importado,
                 naBase,
                 atualizado,
                 inicioJob,
                 fimJob,
                 url_relatorio,
                 pedidos_com_itens_liberados,
                 qtd_produtos_com_precos_atualizados,
                 )

    print 'Enviando Email'
    send_mail('WebAPP Estoque - Status Importacao de produtos', msgString, 'akio.xd@gmail.com',
            LISTA_REMETENTES_EMAIL, fail_silently=False)


@cronjobs.register
def updateABC_task():
    print 'Starting update process'
    updateABCValues()
    print 'Finished update process'