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

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        #Em caso dos filtros
        if self.request.GET.get('dataInicio') and self.request.GET.get('dataFim'):
            dateInicio = datetime.strptime(self.request.GET.get('dataInicio'), '%d-%m-%Y') - timedelta(days=1)
            dateFim = datetime.strptime(self.request.GET.get('dataFim'), '%d-%m-%Y')
        else:
            dateInicio = datetime.today() - timedelta(days=30) - timedelta(hours=3)
            dateFim = datetime.today()

        #Cria a tabela da dashboard limpa
        pedidoArray = []
        qtd_linhas = dateFim.date() - dateInicio.date()
        tempData = dateFim
        for day in range(0, qtd_linhas.days):
            pedidoArray.append([
                str(tempData.day) + '-' + str(tempData.month), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ])
            tempData -= timedelta(days=1)
        pedidoArray.append(['TOTAL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        #Preenche a tabela com os pedidos
        for orderInPeriod in order.objects.filter(created_at__range=[dateInicio.date(), dateFim.date()]):
            #Ajuste de UTC para GMT-3
            orderInPeriod.created_at -= timedelta(hours=3)
            diferencaDias = dateFim.date() - orderInPeriod.created_at.date()

            #Soma a coluna de dias
            pedidoArray[diferencaDias.days][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[diferencaDias.days][25] += 1

            #Soma a coluna Totais
            pedidoArray[-1][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[-1][25] += 1
        context['tabelaPedidos'] = pedidoArray
        context['usuario'] = self.request.user
        return self.render_to_response(context)


def getFaturamentoForDay(date, totalArr):
    inicioDoDia = date.replace(hour=0, minute=0, second=0) - timedelta(hours=3)
    fimDoDia = date.replace(hour=23, minute=59, second=59) - timedelta(hours=3)

    orders = orderNaBase.objects.filter(updated_at__range=[inicioDoDia, fimDoDia]).filter(status__in=['complete', 'complete2'])
    today = str(date.day) + '-' + str(date.month),


    numeroDePedidos = len(orders)
    valorBrutoFaturado = 0
    receitaFrete = 0
    valorDesconto = 0
    valorBonificado = 0
    valorBonificadoPedido = 0
    valorLiquidoProdutos = 0
    custoProdutos = 0
    valorFrete = 0
    valorTaxaCartao = 0
    somatoriaProdutos = 0

    #Não existem pedidos nesse dia
    if len(orders) == 0:
        return [today[0],0,0,0,0,0,0,0,0,0,0,0,0,0]

    for order in orders:
        valorBrutoFaturado += order.valorBrutoFaturado
        receitaFrete += order.receitaFrete
        valorDesconto += order.valorDesconto
        custoProdutos += order.custoProdutos
        valorBonificado += order.valorBonificado
        valorBonificadoPedido += order.valorBonificadoPedido
        somatoriaProdutos += order.somatoriaProdutos
        valorLiquidoProdutos += order.valorLiquidoProdutos
        valorFrete += order.valorFrete
        valorTaxaCartao += order.valorTaxaCartao

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
        if totalArr[1]:
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
        itens = itemObject.objects.all().order_by('sku')

        #Filtros
        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__icontains=self.request.GET.get('nome'))

        if self.request.GET.get('marca'):
            itens = itens.filter(brand_name__icontains=self.request.GET.get('marca'))
        #Filter Only for status
        if self.request.GET.get('status'):
            itens = itens.filter(status=self.request.GET.get('status'))

        #ordenacao
        if self.request.GET.get('order_by'):
            itens = itens.order_by(self.request.GET.get('order_by'))

        self.request.session['product_list'] = itens

        #paginacao
        paginator = Paginator(itens, 300)
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

        if self.request.POST.get('cmm_novo'):
            produto.cmm = ((produto.cmm * produto.estoque_atual) + (float(self.request.POST.get('cmm_novo').replace(',','.')) * float(self.request.POST.get('qtd_a_posicionar')))) \
                          / (float(produto.estoque_atual) + float(self.request.POST.get('qtd_a_posicionar')))

        if self.request.POST.get('qtd_a_posicionar'):
            produto.estoque_atual += int(self.request.POST.get('qtd_a_posicionar'))
            produto.estoque_disponivel += int(self.request.POST.get('qtd_a_posicionar'))
        produto.save()

        get_attr = self.request.META.get('HTTP_REFERER').split('?')[-1]
        return HttpResponseRedirect(reverse('cmm') + "?%s" % get_attr)

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

                        # produto.price = values[2]
                        produto.specialPrice = values[2]
                        produto.estoque_atual = values[4]
                        #o que estiver com estoque zero, deve ficar com custo zero tbm ok?
                        if int(values[4]) == 0:
                            produto.cost = 0
                        else:
                            produto.cost = values[3]
                        produto.cmm = produto.cost
                        produto.margem = 1 - (float(produto.cost) / float(produto.specialPrice))

                        dateMinus8 = datetime.today() - timedelta(days=8)
                        qtd_produtos_comprometidos = len(orderItem.objects.filter(item__sku=values[0]).filter(order__status='holded').filter(created_at__gt=dateMinus8))
                        produto.estoque_empenhado = qtd_produtos_comprometidos
                        produto.estoque_disponivel = int(values[4]) - qtd_produtos_comprometidos
                        produto.save()
                except Exception as e:
                    print e

        return redirect(reverse('cmm'))
    else:
        return HttpResponseForbidden()

class lista_estoque(TemplateView):
    template_name = 'lista_estoque.html'


    def get(self, *args, **kwargs):
        context = self.get_context_data()
        itens = itemObject.objects.all().order_by('sku')

        #Filtros
        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__icontains=self.request.GET.get('nome'))

        if self.request.GET.get('marca'):
            itens = itens.filter(brand_name__icontains=self.request.GET.get('marca'))
        #Filter Only for status
        if self.request.GET.get('status'):
            itens = itens.filter(status=self.request.GET.get('status'))

        #ordenacao
        if self.request.GET.get('order_by'):
            itens = itens.order_by(self.request.GET.get('order_by'))

        self.request.session['product_list'] = itens

        paginator = Paginator(itens, 300)
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
        context = super(lista_estoque, self).get_context_data(**kwargs)
        return context

    def post(self, *args, **kwargs):
        produto = itemObject.objects.get(sku=self.request.POST.get('sku'))



        if self.request.POST.get('qtd_a_posicionar'):
            produto.estoque_atual = int(self.request.POST.get('qtd_a_posicionar'))
            produto.estoque_disponivel = int(self.request.POST.get('qtd_a_posicionar')) - len(orderItem.objects.filter(item__sku=produto.sku).filter(order__status='holded'))
        if self.request.POST.get('price'):
            produto.price = self.request.POST.get('price').replace(',', '.')
        if self.request.POST.get('specialPrice'):
            produto.specialPrice = self.request.POST.get('specialPrice').replace(',', '.')
        if self.request.POST.get('cmm'):
            produto.cmm = self.request.POST.get('cmm').replace(',', '.')
            produto.margem = 1 - (float(produto.cmm) / float(produto.specialPrice))
        produto.save()

        get_attr = self.request.META.get('HTTP_REFERER').split('?')[-1]
        return HttpResponseRedirect(reverse('lista_estoque') + "?%s" % get_attr)

def exportar_lista_produto(request):
    return generateXLS(request.session.get('product_list'))

def generateXLS(modelData):
    from datetime import datetime, date
    from django.http import HttpResponse
    import xlwt


    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('product_list')

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    values_list = modelData.values_list('sku', 'name', 'specialPrice', 'cmm', 'estoque_atual')

    #CABECALHO
    headers = ['sku', 'name', 'specialPrice', 'cmm', 'estoque_atual']
    values_list = [headers] + list(values_list)

    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime):
                style = datetime_style
            elif isinstance(val, date):
                style = date_style
            else:
                style = default_style

            sheet.write(row, col, val, style=style)

    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=export.xls'
    book.save(response)
    return response