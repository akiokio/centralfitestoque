# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.http import HttpResponseRedirect
from salesReport.models import order as orderNaBase, orderItem, brands, item as itemNaBase
from datetime import date, timedelta, datetime
from salesReport.models import order, orderItem, item as itemObject
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


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

class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        dateRange = datetime.today() - timedelta(days=30) - timedelta(hours=3)
        #Cria a tabela da dashboard limpa
        pedidoArray = []
        today = date.today()
        for day in range(0, 31):
            pedidoArray.append([
                str(today.day) + '-' + str(today.month), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ])
            today -= timedelta(days=1)
        pedidoArray.append(['TOTAL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        #Preenche a tabela com os pedidos
        for orderInPeriod in order.objects.filter(created_at__gt=dateRange):
            #Ajuste de UTC para GMT-3
            orderInPeriod.created_at -= timedelta(hours=3)
            diferencaDias = date.today() - orderInPeriod.created_at.date()

            #Soma a coluna de dias
            pedidoArray[diferencaDias.days][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[diferencaDias.days][25] += 1
            #Soma a coluna Totais
            pedidoArray[31][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[31][25] += 1
        context['tabelaPedidos'] = pedidoArray
        context['usuario'] = self.request.user
        return context

def getFaturamentoForDay(date, totalArr):
    inicioDoDia = date.replace(hour=0, minute=0, second=0)
    fimDoDia = date.replace(hour=23, minute=59, second=59)
    orders = orderNaBase.objects.filter(created_at__range=[inicioDoDia, fimDoDia]).filter(status__in=['complete', 'complete2'])
    today = str(date.day) + '-' + str(date.month),
    numeroDePedidos = len(orders)
    valorBrutoFaturado = 0
    receitaFrete = 0
    valorDesconto = 0
    valorBonificado = 0
    valorLiquidoProdutos = 0
    custoProdutos = 0
    valorFrete = 0
    valorTaxaCartao = 0
    somatoriaProdutos = 0

    if len(orders) == 0:
        return [today[0],0,0,0,0,0,0,0,0,0,0,0,0,0]

    for order in orders:
        valorBrutoFaturado += order.grand_total
        receitaFrete += order.shipping_amount
        valorDesconto += order.discount_amount

        valorBonificadoPedido = 0
        for item in order.orderitem_set.all():
            #Para produtos com tipos especiais somar o custo somente dos produtos simples
            #Somente produtos simples são somados no variavel somatoria de produtos para calcular o # de produtos pedidos
            if item.productType == 'simple':
                custoProdutos += item.item.cost * item.quantidade
                somatoriaProdutos += item.quantidade
            #Para o valor bonificado somar somente os produtos simples (filhos)
            if item.price == 0.0 and item.is_child == False:
                valorBonificado += item.item.price
                valorBonificadoPedido += item.item.price

        valorLiquidoProdutos += order.grand_total - order.shipping_amount - order.discount_amount - valorBonificadoPedido
        valorFrete += order.shipping_amount_centralfit

        if order.payment_method == 'BoletoBancario':
            valorTaxaCartao += 2.2
        else:
            valorTaxaCartao += (order.grand_total * 0.029)

    margemBrutaSoProdutos = 1 - (custoProdutos / valorLiquidoProdutos)
    margemBrutaCartaoFrete = 1 - ((custoProdutos + valorFrete + valorTaxaCartao) / (valorLiquidoProdutos + receitaFrete))
    ticketMedio = valorLiquidoProdutos / numeroDePedidos
    nuemroPedidosProdutos = round(somatoriaProdutos / numeroDePedidos, 2)

    #fix negative sign in vlr_desconto
    valorDesconto = valorDesconto * (-1)

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

class Faturamento(TemplateView):
    template_name = 'faturamento.html'

    def get_context_data(self, **kwargs):
        context = super(Faturamento, self).get_context_data(**kwargs)
        #Cria a tabela da dashboard limpa
        tabela = []
        totalArr = []
        today = datetime.now()
        #range define a quantidade de dia que a tabela deve ter
        for day in range(0, 7):
            tabela.append(getFaturamentoForDay(today, totalArr))
            today -= timedelta(days=1)
        tabela.append(['TOTAL'])

        context['tabelaFaturamento'] = tabela
        return context

def importar(request):
    return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))