# -*- coding: utf-8 -*-
__author__ = 'akiokio'

from django_cron import CronJobBase, Schedule
import datetime
from django.core.mail import send_mail
from centralFitEstoque.settings import LISTA_REMETENTES_EMAIL, RUN_EVERY_MINS
from salesReport.views import timeInGMT, timeInUTC, updateLast7daysOrderStatus, importOrders, generateCsvFileCron

class MyCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        inicioJob = datetime.datetime.now()

        dateInit = datetime.datetime.today().replace(hour=0, minute=0, second=0) - datetime.timedelta(days=1)
        dateEnd = datetime.datetime.today().replace(hour=23, minute=59, second=59) - datetime.timedelta(days=1)

        #Import yesterday orders
        naBase = 0
        importado = 0

        dateInitInUtc = timeInUTC('%s-%s-%s 00:00:00' % (dateInit.year, dateInit.month, dateInit.day))
        dateEndInUtc = timeInUTC('%s-%s-%s 23:59:59' % (dateEnd.year, dateEnd.month, dateEnd.day))

        importado, naBase = importOrders(dateEndInUtc, dateInitInUtc, importado, naBase)

        #Update Last 7 days order status
        atualizado = updateLast7daysOrderStatus()

        #Save fisic archive
        url_relatorio = generateCsvFileCron(dateInitInUtc, dateEndInUtc)

        fimJob = datetime.datetime.now()
        #Jobs is done, tell everyone
        msgString = '''
                    Range Inicio: %s,
                    Range Fim: %s,
                    Pedidos importados: %s,
                    Pedidos na base: %s,
                    Pedidos com status atualizados: %s,
                    iniciado as: %s, finalizado as: %s,
                    url_relatorio: %s
                    ''' % \
                    (dateInit, dateEnd, importado, naBase, atualizado, inicioJob, fimJob, url_relatorio)

        send_mail('WebAPP Estoque - Status Importacao de produtos', msgString, 'akio.xd@gmail.com',
                LISTA_REMETENTES_EMAIL, fail_silently=False)



