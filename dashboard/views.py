# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.models import order as orderNaBase, orderItem, brands, item as itemNaBase
from datetime import date, timedelta, datetime
from salesReport.models import order, orderItem, item as itemObject
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from xlrd import open_workbook
from django.shortcuts import redirect


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

                return render_to_response('registration/login.html',
                                          {'error': 'Usuario ou senha incorreta'},
                                          context_instance=RequestContext(request))
                # Return a 'disabled account' error message
        else:
            return render_to_response('registration/login.html',
                                          {'error': 'Usuario ou senha incorreta'},
                                          context_instance=RequestContext(request))
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
    inicioDoDia = date.replace(hour=0, minute=0, second=0) - timedelta(hours=3)
    fimDoDia = date.replace(hour=23, minute=59, second=59) - timedelta(hours=3)

    orders = orderNaBase.objects.filter(updated_at__range=[inicioDoDia, fimDoDia]).filter(status__in=['complete', 'complete2'])
    # orders = orderNaBase.objects.filter(created_at__range=[inicioDoDia, fimDoDia]).filter(status__in=['complete', 'complete2'])
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

    #Não existem pedidos nesse dia
    if len(orders) == 0:
        return [today[0],0,0,0,0,0,0,0,0,0,0,0,0,0]

    for order in orders:
        tmp_valorBrutoFaturado, tmp_receitaFrete, tmp_valorDesconto, tmp_custoProdutos, tmp_valorBonificado, \
        tmp_valorBonificadoPedido, tmp_somatoriaProdutos, tmp_valorLiquidoProdutos, tmp_valorFrete, tmp_valorTaxaCartao = order.getBillingInfo()

        valorBrutoFaturado += tmp_valorBrutoFaturado
        receitaFrete += tmp_receitaFrete
        valorDesconto += tmp_valorDesconto
        valorBonificado += tmp_valorBonificado
        valorLiquidoProdutos += tmp_valorLiquidoProdutos
        custoProdutos += tmp_custoProdutos
        valorFrete += tmp_valorFrete
        valorTaxaCartao += tmp_valorTaxaCartao
        somatoriaProdutos += tmp_somatoriaProdutos


    margemBrutaSoProdutos = (1 - (custoProdutos / valorLiquidoProdutos)) * 100
    margemBrutaCartaoFrete = (1 - ((custoProdutos + valorFrete + valorTaxaCartao) / (valorLiquidoProdutos + receitaFrete))) * 100
    ticketMedio = valorLiquidoProdutos / numeroDePedidos
    nuemroPedidosProdutos = round(somatoriaProdutos / numeroDePedidos, 2)

    totalArr[1] += numeroDePedidos
    totalArr[2] += round(valorBrutoFaturado, 2)
    totalArr[3] += round(receitaFrete, 2)
    totalArr[4] += round(valorDesconto, 2)
    totalArr[5] += round(valorBonificado, 2)
    totalArr[6] += round(valorLiquidoProdutos, 2)
    totalArr[7] += round(custoProdutos, 2)
    totalArr[8] += round(valorFrete, 2)
    totalArr[9] += round(valorTaxaCartao, 2)
    totalArr[10] = (totalArr[10] + round(margemBrutaSoProdutos, 2)) /2
    totalArr[11] = (totalArr[11] + round(margemBrutaCartaoFrete, 2)) /2
    totalArr[12] = (totalArr[12] + round(ticketMedio, 2)) / 2
    totalArr[13] += somatoriaProdutos

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
        totalArr = ['TOTAL',0,0,0,0,0,0,0,0,0,0,0,0,0]

        today = datetime.now()
        #range define a quantidade de dia que a tabela deve ter
        for day in range(0, 90):
            tabela.append(getFaturamentoForDay(today, totalArr))
            today -= timedelta(days=1)

        #Finaliza linha de totais
        totalArr[13] = totalArr[13] / float(totalArr[1])
         #Arredonda os valores
        totalArr[1] = round(totalArr[1], 2)
        totalArr[2] = round(totalArr[2], 2)
        totalArr[3] = round(totalArr[3], 2)
        totalArr[4] = round(totalArr[4], 2)
        totalArr[5] = round(totalArr[5], 2)
        totalArr[6] = round(totalArr[6], 2)
        totalArr[7] = round(totalArr[7], 2)
        totalArr[8] = round(totalArr[8], 2)
        totalArr[9] = round(totalArr[9], 2)
        totalArr[10] = round(totalArr[10], 2)
        totalArr[11] = round(totalArr[11], 2)
        totalArr[12] = round(totalArr[12], 2)
        totalArr[13] = round(totalArr[13], 2)
        tabela.append(totalArr)

        context['tabelaFaturamento'] = tabela
        return context

def importar(request):
    return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))

def daterange(start_date, end_date):
    dateRange = end_date - start_date
    if dateRange.days == 0:
            dateRange += timedelta(days=1)
    for n in range(int (dateRange.days)):
        yield start_date + timedelta(n)

@csrf_exempt
def filtrarFaturamento(request):
    if request.method == 'POST':
        tabela = []
        totalArr = ['TOTAL',0,0,0,0,0,0,0,0,0,0,0,0,0]

        dataInicio = datetime.strptime(request.POST.get('dataInicio'), '%d-%m-%Y')
        dataFim = datetime.strptime(request.POST.get('dataFim'), '%d-%m-%Y')
        dataFim += timedelta(days=1)

        for single_date in daterange(dataInicio, dataFim):
            print single_date
            tabela.append(getFaturamentoForDay(single_date, totalArr))

        #Finaliza linha de totais
        totalArr[13] = totalArr[13] / float(totalArr[1])
        #Arredonda os valores
        totalArr[1] = round(totalArr[1], 2)
        totalArr[2] = round(totalArr[2], 2)
        totalArr[3] = round(totalArr[3], 2)
        totalArr[4] = round(totalArr[4], 2)
        totalArr[5] = round(totalArr[5], 2)
        totalArr[6] = round(totalArr[6], 2)
        totalArr[7] = round(totalArr[7], 2)
        totalArr[8] = round(totalArr[8], 2)
        totalArr[9] = round(totalArr[9], 2)
        totalArr[10] = round(totalArr[10], 2)
        totalArr[11] = round(totalArr[11], 2)
        totalArr[12] = round(totalArr[12], 2)
        totalArr[13] = round(totalArr[13], 2)

        tabela.append(totalArr)
        return HttpResponse(simplejson.dumps(tabela))

class cmm(TemplateView):
    template_name = 'cmm.html'


    def get(self, *args, **kwargs):
        context = self.get_context_data()
        itens = itemObject.objects.all().filter(status=True).order_by('sku')

        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__contains=self.request.GET.get('nome'))

        if self.request.GET.get('marca'):
            itens = itens.filter(brand_name__contains=self.request.GET.get('marca'))

        paginator = Paginator(itens, 10)
        page = self.request.GET.get('page')
        try:
            itens = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            itens = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            itens = paginator.page(paginator.num_pages)

        context['itens'] = itens
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(cmm, self).get_context_data(**kwargs)
        return context

    def post(self, *args, **kwargs):
        produto = itemObject.objects.get(sku=self.request.POST.get('sku'))
        if self.request.POST.get('qtd_a_posicionar'):
            produto.estoque_atual += int(self.request.POST.get('qtd_a_posicionar'))
            produto.estoque_disponivel += int(self.request.POST.get('qtd_a_posicionar'))
        if self.request.POST.get('cmm_novo'):
            produto.cmm = ((produto.cmm * produto.estoque_atual) + (float(self.request.POST.get('cmm_novo').replace(',','.')) * float(self.request.POST.get('qtd_a_posicionar')))) \
                          / (float(produto.estoque_atual) + float(self.request.POST.get('qtd_a_posicionar')))
        produto.save()
        return redirect(reverse('cmm'))

def importarQuantidadeEstoque(request):
    if request.method == "POST":
        file = request.FILES['docfile']
        wb = open_workbook(file_contents=file.read())
        for s in wb.sheets():
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                try:
                    if values[0] != 0:
                        produto = itemNaBase.objects.get(sku=values[0])
                        produto.estoque_atual = values[1]
                        #Litle hack for fist cmm
                        qtd_produtos_comprometidos = len(orderItem.objects.filter(item__sku=values[0]).filter(order__status='holded'))
                        produto.cmm = produto.cost
                        produto.estoque_empenhado = qtd_produtos_comprometidos
                        produto.estoque_disponivel = int(values[1]) - qtd_produtos_comprometidos
                        produto.save()
                except Exception as e:
                    print e

        return redirect(reverse('cmm'))
    else:
        return HttpResponseForbidden()